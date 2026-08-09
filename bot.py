import logging
import traceback
import sys

from scrapers.allindiabullion import get_all_delhi_rates
from storage import (
    load_previous_data,
    save_current_data
)
from ai import generate_summary
from telegram_sender import send_message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def validate_response(response, service_name):

    if response is None:
        raise ValueError(
            f"{service_name} returned None"
        )

    if isinstance(response, dict):

        if response.get("error"):
            raise ValueError(
                f"{service_name} error: "
                f"{response['error']}"
            )

        if response.get("status") in [
            400,
            401,
            403,
            404,
            429,
            500
        ]:
            raise ValueError(
                f"{service_name} failed with "
                f"status {response['status']}"
            )

    return response


def validate_gold_data(data):

    if not isinstance(data, dict):
        raise ValueError(
            "Invalid gold data format"
        )

    required_fields = [
        "city",
        "currency",
        "karat_prices_per_10g"
    ]

    for field in required_fields:

        if field not in data:

            raise ValueError(
                f"Missing field: {field}"
            )

    required_karats = [
        "24K",
        "22K",
        "20K",
        "18K"
    ]

    prices = data["karat_prices_per_10g"]

    for karat in required_karats:

        if karat not in prices:

            raise ValueError(
                f"Missing {karat} price"
            )


try:

    logger.info(
        "========== GOLD BOT STARTED =========="
    )

    logger.info(
        "Fetching gold rates..."
    )

    current_data = get_all_delhi_rates()

    validate_response(
        current_data,
        "Gold Price Scraper"
    )

    validate_gold_data(
        current_data
    )

    logger.info(
        "Gold rates fetched successfully"
    )

    logger.info(
        f"Current prices: "
        f"{current_data['karat_prices_per_10g']}"
    )

    logger.info(
        "Loading previous day data..."
    )

    previous_data = load_previous_data()

    if not previous_data:

        logger.warning(
            "No previous data found. "
            "Running in first-time mode."
        )

    else:

        logger.info(
            f"Previous prices: "
            f"{previous_data.get('karat_prices_per_10g', {})}"
        )

    logger.info(
        "Generating Gemini summary..."
    )

    summary = generate_summary(
        current_data,
        previous_data
    )

    validate_response(
        summary,
        "Gemini"
    )

    logger.info(
        "Summary generated successfully"
    )

    logger.info(
        "Sending Telegram message..."
    )

    telegram_response = send_message(
        summary
    )

    if telegram_response:

        validate_response(
            telegram_response,
            "Telegram"
        )

    logger.info(
        "Telegram message sent"
    )

    logger.info(
        "Saving current data..."
    )

    save_current_data(
        current_data
    )

    logger.info(
        "Current data saved"
    )

    logger.info(
        "========== BOT COMPLETED =========="
    )

except Exception as e:

    logger.error(
        "========== BOT FAILED =========="
    )

    logger.error(str(e))

    logger.error(
        traceback.format_exc()
    )

    sys.exit(1)
