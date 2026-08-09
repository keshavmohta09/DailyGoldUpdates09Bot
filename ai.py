import datetime

import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

PROMPT = """
You are generating a Telegram message for a daily gold price update.

TODAY DATA:
{today_data}

YESTERDAY DATA:
{yesterday_data}

IMPORTANT:

Use ONLY the values inside:

karat_prices_per_10g

Ignore:
- purity_weight_table
- silver prices
- gram prices
- tola prices
- kilogram prices

Generate the report ONLY for:
24K
22K
20K
18K

All values must be shown as price per 10 grams.

RULES:

- Return ONLY the final Telegram message.
- Do not explain anything.
- Do not use markdown tables.
- Do not use code blocks.
- Use emojis exactly as shown.
- Format currency in Indian Rupees with commas.
- If yesterday's data exists, calculate percentage change.
- If yesterday's data is unavailable, show N/A.
- Market Summary must contain exactly 3 bullet points.
- AI Insight must be exactly 1 short sentence.
- Investment Tip of the Day must be exactly 1 short sentence.
- AI Insight and Investment Tip MUST be different.
- Generate fresh insight and tip every time.
- Do not repeat generic advice.
- Use today's actual date.

OUTPUT FORMAT:

📈 DAILY GOLD PRICE UPDATE
📅 {date}

🏆 24K Gold
• Today: ₹<value> / 10g
• Yesterday: ₹<value> / 10g
• Change: 🟢 +x.xx% or 🔴 -x.xx%

🥇 22K Gold
• Today: ₹<value> / 10g
• Yesterday: ₹<value> / 10g
• Change: 🟢 +x.xx% or 🔴 -x.xx%

🥈 20K Gold
• Today: ₹<value> / 10g
• Yesterday: ₹<value> / 10g
• Change: 🟢 +x.xx% or 🔴 -x.xx%

🥉 18K Gold
• Today: ₹<value> / 10g
• Yesterday: ₹<value> / 10g
• Change: 🟢 +x.xx% or 🔴 -x.xx%

📊 Market Summary
🟢 Bullet 1
🟢 Bullet 2
🟢 Bullet 3

💡 AI Insight
<one sentence>

🎯 Investment Tip of the Day
<one sentence>

Generate the message using the supplied data.
"""


def generate_summary(
    today_data,
    yesterday_data
):

    prompt = PROMPT.format(
        today_data=today_data,
        yesterday_data=yesterday_data,
        date=datetime.date.today().strftime(
            "%d-%m-%Y"
        )
    )

    response = model.generate_content(
        prompt
    )

    return response.text
