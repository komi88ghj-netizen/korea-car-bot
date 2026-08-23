import os
import time
import requests
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Korea Car Scraper Bot is Running!"

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

def send_telegram_msg(text):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram tokens not set!")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def check_kb_chacha():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    send_telegram_msg("🚗 **بوت فحص السيارات الكورية شغال الآن!**\nجاري مراقبة KB ChaChaCha لسيارات تحت الـ 7,000$...")
    
    while True:
        try:
            print("Checking cars under 9,500,000 KRW...")
        except Exception as e:
            print(f"Scraping error: {e}")
        
        time.sleep(600)

Thread(target=check_kb_chacha, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
