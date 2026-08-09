import logging
import traceback
import sys

from scraper import get_gold_rates
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
    """
    Validate API responses that may not raise exceptions.
    """

    if response is None:
        raise ValueError(f"{service_name} returned None")

    if isinstance(response, dict):

        if response.get("error"):
            raise ValueError(
                f"{service_name} error: {response['error']}"
            )

        if response.get("status") in [400, 401, 403, 404, 429, 500]:
            raise ValueError(
                f"{service_name} failed with status "
                f"{response['status']}"
            )

    return response


try:

    logger.info("========== GOLD BOT STARTED ==========")

    logger.info("Fetching gold rates...")
    today_data = get_gold_rates()

    validate_response(
        today_data,
        "Gold API"
    )

    logger.info("Gold rates fetched successfully")

    logger.info("Loading previous day data...")
    yesterday_data = load_previous_data()

    if not yesterday_data:
        logger.warning(
            "No previous data found. "
            "Running in first-time mode."
        )

    logger.info("Generating Gemini summary...")

    summary = generate_summary(
        today_data,
        yesterday_data
    )

    validate_response(
        summary,
        "Gemini"
    )

    logger.info("Summary generated successfully")

    logger.info("Sending Telegram message...")

    telegram_response = send_message(summary)

    # Optional validation if your function returns response
    if telegram_response:
        validate_response(
            telegram_response,
            "Telegram"
        )

    logger.info("Telegram message sent")

    logger.info("Saving current data...")

    save_current_data(today_data)

    logger.info("Current data saved")

    logger.info("========== BOT COMPLETED ==========")

except Exception as e:

    logger.error(
        "========== BOT FAILED =========="
    )

    logger.error(str(e))

    logger.error(
        traceback.format_exc()
    )

    sys.exit(1)
