"""
Scraper for live Delhi gold/silver rates from allindiabullion.com.

Fixes applied so far (kept here as comments so future edits don't reintroduce
the same bugs):

1. requests wasn't detecting UTF-8 correctly -> mangled "•" and "—" in the
   HTML -> force resp.encoding = "utf-8" before parsing.
2. The site writes karat labels as "24<!-- -->K" (an HTML comment between
   the digits and the K, presumably to deter naive scraping/translation
   widgets). BeautifulSoup drops the comment but get_text("\\n") still
   inserts a newline where it was, giving "24\\nK" instead of "24K" ->
   normalize that back together before matching.

Install deps:
    pip install requests beautifulsoup4

"""

import re
import json
import requests
from bs4 import BeautifulSoup

URL = "https://allindiabullion.com/gold-rate/delhi/delhi"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-IN,en;q=0.9",
}


def _fetch_text(url: str = URL) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text("\n")
    # Glue "24\nK" (etc.) back into "24K" — see module docstring, fix #2.
    text = re.sub(r"(\d)\s+(K\b)", r"\1\2", text)
    return text


def _slice_between(text: str, start_marker: str, end_marker: str) -> str:
    start = text.find(start_marker)
    if start == -1:
        raise ValueError(f"Could not find start marker: {start_marker!r} "
                          f"(page structure may have changed)")
    start += len(start_marker)
    end = text.find(end_marker, start)
    if end == -1:
        raise ValueError(f"Could not find end marker: {end_marker!r} "
                          f"(page structure may have changed)")
    return text[start:end]


def get_karat_prices_per_10g(text: str = None) -> dict:
    """
    Returns e.g.:
    {"24K": 148407, "23K": 142223, "22K": 135940,
     "20K": 123672, "18K": 111305, "14K": 86570}
    """
    text = text or _fetch_text()
    block = _slice_between(text, "Karat Prices", "AIB Reference Rate")

    pattern = re.compile(r"(\d{2}K)\s+([\d,]+)\s+per 10g")
    result = {k: int(v.replace(",", "")) for k, v in pattern.findall(block)}

    if not result:
        raise ValueError(
            "No karat prices parsed — page structure may have changed.\n"
            f"--- Debug: sliced block was ---\n{block[:1000]}"
        )
    return result


def get_purity_weight_table(text: str = None) -> dict:
    """
    Parses the 'Weight and Purity Table' (1g, 8g, 10g, 1 tola, 100g, 1kg)
    for 24K, 22K, 18K gold and 999 silver.
    """
    text = text or _fetch_text()
    block = _slice_between(text, "Weight and Purity Table", "1 kg gold price")

    weight_labels = ["1 gram", "8 gram", "10 gram", "1 tola", "100 gram", "1 kg"]
    purity_pattern = re.compile(
        r"(24K\s*\(1000\)|22K\s*\(916\)|18K\s*\(750\)|Silver\s*\(999\))"
        r".*?\n((?:\u20b9[\d,]+\s*\n?){6})",
        re.DOTALL,
    )

    result = {}
    for label, prices_block in purity_pattern.findall(block):
        clean_label = "Silver (999)" if "Silver" in label else re.sub(r"\s*\(.*\)", "", label)
        values = re.findall(r"\u20b9([\d,]+)", prices_block)
        result[clean_label] = {
            wl: int(v.replace(",", "")) for wl, v in zip(weight_labels, values)
        }

    if not result:
        raise ValueError(
            "No purity/weight table parsed — page structure may have changed.\n"
            f"--- Debug: sliced block was ---\n{block[:1500]}"
        )
    return result


def get_all_delhi_rates() -> dict:
    text = _fetch_text()
    return {
        "city": "Delhi",
        "currency": "INR",
        "karat_prices_per_10g": get_karat_prices_per_10g(text),
        "purity_weight_table": get_purity_weight_table(text),
    }
