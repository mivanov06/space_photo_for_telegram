import os
import random

import telegram

from dotenv import load_dotenv


def get_random_image(folder):
    files = os.walk(folder)
    for root, dirs, files in files:
        ...
    return random.choice(files)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(telegram_token)
    folder = 'images'
    bot.send_photo(chat_id=chat_id, photo=open(f'{folder}/{get_random_image(folder)}', 'rb'))
