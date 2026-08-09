import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-3.6-flash"
)


def generate_summary(
    today_data,
    yesterday_data
):

    prompt = f"""
You are generating a Telegram message for a daily gold price update.

TODAY DATA:
{today_data}

YESTERDAY DATA:
{yesterday_data}

RULES:

- Return ONLY the final Telegram message.
- Do not explain anything.
- Do not use markdown tables.
- Do not use code blocks.
- Use emojis exactly as shown.
- Format currency in Indian Rupees with commas.
- Show prices per 10 grams.
- If yesterday's data exists, calculate percentage change.
- If yesterday's data is unavailable, show N/A.
- Market Summary must contain exactly 3 bullet points.
- AI Insight must be 1-2 sentences.
- Investment Tip of the Day must be exactly 1 sentence.
- Keep the response concise and professional.
- Use today's actual date.

FOLLOW THIS EXACT STYLE:

📈 DAILY GOLD PRICE UPDATE
📅 09 Aug 2026

🏆 24K Gold
• Today: ₹132,936 / 10g
• Yesterday: N/A
• Change: N/A

🥇 22K Gold
• Today: ₹121,858 / 10g
• Yesterday: N/A
• Change: N/A

🥈 20K Gold
• Today: ₹110,780 / 10g
• Yesterday: N/A
• Change: N/A

🥉 18K Gold
• Today: ₹99,702 / 10g
• Yesterday: N/A
• Change: N/A

📊 Market Summary
🟢 Gold prices remain elevated.
🟢 24K continues to be the benchmark investment grade.
🟢 Historical comparison unavailable today.

💡 AI Insight
Consider SIP-style gold accumulation instead of timing daily fluctuations.

🎯 Investment Tip of the Day
Invest regularly and focus on long-term accumulation rather than short-term price movements.

Generate the message using the supplied data.
"""

    response = model.generate_content(
        prompt
    )

    return response.text