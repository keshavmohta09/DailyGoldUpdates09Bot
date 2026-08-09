from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
GOLD_API_KEY = os.getenv("GOLD_API_KEY")