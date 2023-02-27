import argparse
import os
import random
import time

import telegram

from dotenv import load_dotenv


def get_random_image(folder):
    files = os.listdir(folder)
    return random.choice(files)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(telegram_token)
    folder = 'images'
    parser = argparse.ArgumentParser(description='script for publishing photos in telegram channel')
    parser.add_argument('-d', '--delay', default=14400, type=int,
                        help='frequency of sending photos (in seconds)')
    args = parser.parse_args()
    delay = args.delay
    while True:
        image = get_random_image(folder)
        with open(f'{folder}/{image}', 'rb') as file:
            bot.send_photo(chat_id=chat_id, photo=file)
        time.sleep(delay)
