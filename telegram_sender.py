import logging

import requests

from config import (
    BOT_TOKEN,
    CHAT_IDS
)

logger = logging.getLogger(
    __name__
)


def send_message(message):

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )

    results = []

    for num, chat_id in enumerate(CHAT_IDS):

        try:

            response = requests.post(
                url,
                json={
                    "chat_id": chat_id,
                    "text": message,
                    "parse_mode": "Markdown"
                },
                verify=False,
                timeout=30
            )

            response_json = (
                response.json()
            )

            results.append(
                response_json
            )

            if response.ok:

                logger.info(
                    f"Message sent to chat id"
                    f"{num+1}"
                )

            else:

                logger.error(
                    f"Telegram error for chat id"
                    f"{num+1}: "
                    f"{response_json}"
                )

        except Exception as e:

            logger.error(
                f"Failed sending to chat id"
                f"{num+1}: {e}"
            )

            results.append({
                "chat_id": num+1,
                "error": str(e)
            })

    return results
