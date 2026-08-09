import requests

from config import (
    BOT_TOKEN,
    CHAT_ID
)


def send_message(message):

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )

    requests.post(
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message, "parse_mode": "Markdown"
        },
        verify=False,
    )