
# Mr AI Signal Generator Bot
# Requirements: pip install flask python-telegram-bot==13.15
from flask import Flask, request
import telegram

app = Flask(__name__)
bot = telegram.Bot(token="8239899760:AAHm7ThLqGEVuYz2yZ9hSLiX56-Z9ra-HmA")

# Replace this with your own chat_id if needed (optional hardcoding)
# chat_id = "YOUR_CHAT_ID"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Expecting TradingView alert message in this format:
    # {
    #   "symbol": "EURUSD",
    #   "action": "BUY",
    #   "sl": 1.0823,
    #   "tp": 1.0860,
    #   "time": "12:45 PM"
    # }
    symbol = data.get("symbol", "Unknown")
    action = data.get("action", "WAIT").upper()
    sl = data.get("sl", None)
    tp = data.get("tp", None)
    time = data.get("time", "")

    msg = "📡 *Mr AI Signal Generator*\n"
    msg += f"🧠 Action: *{action}* on `{symbol}`\n"
    if sl and tp:
        msg += f"🎯 TP: `{tp}` | 🛡 SL: `{sl}`\n"
    if time:
        msg += f"🕒 Time: {time}\n"

    bot.send_message(chat_id="@your_channel_or_user_id", text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    return "ok", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
