import json
import os
import logging

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = os.path.join(
    BASE_DIR,
    "data",
    "latest.json"
)


def load_previous_data():
    """
    Load previous day's gold data.
    Returns {} if file does not exist or is invalid.
    """

    try:

        logger.info(
            f"Loading previous data from: {FILE_PATH}"
        )

        if not os.path.exists(FILE_PATH):
            logger.warning(
                "latest.json not found. "
                "First run detected."
            )
            return {}

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info(
            "Previous data loaded successfully."
        )

        return data

    except json.JSONDecodeError:

        logger.error(
            "latest.json is corrupted."
        )

        return {}

    except Exception as e:

        logger.error(
            f"Failed to load previous data: {e}"
        )

        return {}


def save_current_data(data):
    """
    Save current gold data for next run.
    """

    try:

        logger.info(
            f"Saving current data to: {FILE_PATH}"
        )

        os.makedirs(
            os.path.dirname(FILE_PATH),
            exist_ok=True
        )

        with open(
            FILE_PATH,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            "Current data saved successfully."
        )

    except Exception as e:

        logger.error(
            f"Failed to save current data: {e}"
        )

        raise
