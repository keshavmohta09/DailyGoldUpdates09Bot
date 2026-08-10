# 🥇 DailyGoldUpdates09Bot

DailyGoldUpdates09Bot is a GenAI-powered financial insights assistant that combines live gold market data with Google's Gemini AI to generate intelligent market analysis and investment guidance.

Unlike traditional price alert bots, the system does more than fetch and forward data. It interprets market movements, compares historical prices, identifies trends, generates contextual insights, and delivers human-readable investment intelligence directly to Telegram.

The project demonstrates how Generative AI can be integrated into real-world data pipelines to transform raw financial information into actionable insights.

---

## ✨ Features

- 📈 Live Gold Price Monitoring
- 🏆 Supports 24K, 22K, 20K and 18K Gold
- 💰 Prices per Gram and per 10 Grams
- 📊 Day-over-Day Comparison
- 📉 Percentage Increase / Decrease Analysis
- 🤖 AI-Powered Market Summary using Google Gemini
- 💡 Daily Investment Tip
- 📬 Telegram Notifications
- ☁️ Automated using GitHub Actions
- 🆓 Runs on Free Tiers

---

## 📱 Sample Output

```text
📈 DAILY GOLD PRICE UPDATE
📅 09 Aug 2026

🏆 24K Gold
• Today: ₹132,936 / 10g
• Yesterday: ₹131,450 / 10g
• Change: 🟢 +1.13%

🥇 22K Gold
• Today: ₹121,858 / 10g
• Yesterday: ₹120,900 / 10g
• Change: 🟢 +0.79%

🥈 20K Gold
• Today: ₹110,780 / 10g
• Yesterday: ₹109,900 / 10g
• Change: 🟢 +0.80%

🥉 18K Gold
• Today: ₹99,702 / 10g
• Yesterday: ₹99,100 / 10g
• Change: 🟢 +0.61%

📊 Market Summary

🟢 Gold prices continue to trade near record highs.
🟢 All major purities registered gains today.
🟢 Investor sentiment remains positive.

💡 AI Insight

Gold continues to show strength as a long-term wealth preservation asset.

🎯 Investment Tip of the Day

Invest consistently rather than attempting to time short-term market movements.
```

---

## 🏗️ Architecture

```text
GoldAPI
   │
   ▼
Python Bot
   │
   ▼
Load Previous Data
   │
   ▼
Google Gemini
   │
   ▼
Generate AI Analysis
   │
   ▼
Telegram Bot
   │
   ▼
Send Notification
```

---


## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/keshavmohta09/DailyGoldUpdates09Bot.git
cd DailyGoldUpdates09Bot
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

### Windows

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Required API Keys

### GoldAPI

Create a free account:

https://www.goldapi.io/

Generate:

```text
GOLD_API_KEY
```

---

### Google Gemini

Generate API key:

https://aistudio.google.com/app/apikey

Generate:

```text
GEMINI_API_KEY
```

---

### Telegram Bot

Create a bot:

https://t.me/BotFather

Generate:

```text
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
GOLD_API_KEY=your_goldapi_key

GEMINI_API_KEY=your_gemini_api_key

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

TELEGRAM_CHAT_ID=your_telegram_chat_id
```

---

## ▶️ Run Locally

```bash
python bot.py
```

If everything is configured correctly, you should receive a Telegram message containing:

- Current Gold Rates
- Daily Comparison
- AI Market Summary
- AI Investment Tip

---

## ☁️ GitHub Actions Setup

Navigate to:

```text
Repository
→ Settings
→ Secrets and Variables
→ Actions
```

Add the following secrets:

```text
GOLD_API_KEY

GEMINI_API_KEY

TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID
```

---


## 🛠 Tech Stack

- Python 3.12
- GoldAPI
- Google Gemini
- Telegram Bot API
- GitHub Actions

---

## 🎯 Future Enhancements

- 📈 Historical Trend Charts
- 🌍 City-wise Gold Rates
- 📊 Weekly and Monthly Reports

---

## 👨‍💻 Author

**Keshav Mohta**

Built to automate gold price tracking, AI analysis, and Telegram delivery using free cloud services.
