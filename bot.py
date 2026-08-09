from scraper import get_gold_rates
from storage import (
    load_previous_data,
    save_current_data
)
from ai import generate_summary
from telegram_sender import send_message


today_data = get_gold_rates()

yesterday_data = load_previous_data()

summary = generate_summary(
    today_data,
    yesterday_data
)

send_message(summary)

save_current_data(today_data)

print("Gold update sent")