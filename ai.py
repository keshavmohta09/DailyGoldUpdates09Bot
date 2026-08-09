import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-3.6-flash"
)
PROMPT = """
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
- AI Insight must be exactly 1 short sentence.
- Investment Tip of the Day must be exactly 1 short sentence.
- AI Insight and Investment Tip MUST be different from each other.
- AI Insight and Investment Tip MUST be generated fresh for every response.
- Do not repeat advice from previous sections.
- Base insights on today's prices, price changes, and market movement.
- Avoid generic statements.
- Keep the response concise and professional.
- Use today's actual date.

OUTPUT FORMAT:

📈 DAILY GOLD PRICE UPDATE
📅 <today date>

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
<one sentence generated from today's data>

🎯 Investment Tip of the Day
<one sentence generated from today's data>

Generate the message using the supplied data.
"""


def generate_summary(
    today_data,
    yesterday_data
):

    prompt = PROMPT.format(today_data=today_data,yesterday_data=yesterday_data)
    
    response = model.generate_content(
        prompt
    )

    return response.text
