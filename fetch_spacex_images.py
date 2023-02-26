import argparse
import os

import requests
from dotenv import load_dotenv

from main_function import download_image


def fetch_spacex_last_launch(launch_id=None):
    if launch_id is None:
        api_url = 'https://api.spacexdata.com/v5/launches/latest'
    else:
        api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    folder = 'images'
    print(len(image_links))
    for image_number, image_link in enumerate(image_links):
        download_image(image_link, folder, token, prefix_name='spacex_launch')


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    parser = argparse.ArgumentParser(description='Download SpaseX photo')
    parser.add_argument('-i', '--id', help='launch id')
    args = parser.parse_args()
    id = args.id
    fetch_spacex_last_launch(id)
