import os
import requests
from dotenv import load_dotenv

from main_function import download_image


def nasa_apod_photo(token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count': 35
    }
    folder = 'images'
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    for number, res in enumerate(response.json()):
        if res['media_type'] == 'image':
            image_link = res['hdurl']
            download_image(image_link, folder, token, prefix_name='nasa_apod')
    return


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    nasa_apod_photo(token)
