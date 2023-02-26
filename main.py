import os
import telegram


import requests
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(telegram_token)
    print(bot.get_me())
    bot.send_message(chat_id='-1001680271761', text='First message')