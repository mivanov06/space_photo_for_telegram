import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from main_function import download_image


def epic_photo(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': token
    }
    folder = 'images'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    links = list()
    for link in response.json():
        photo_name = link["image"]
        photo_date = datetime.fromisoformat(link["date"]).strftime("%Y/%m/%d")
        links.append(f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_name}.png')
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_name}.png'
        print(f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_name}.png')
        download_image(image_link, folder, token, prefix_name='nasa')
    return links


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    epic_photo(token)
