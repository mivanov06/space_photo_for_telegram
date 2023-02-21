import os
import urllib
from urllib.parse import urlparse
from pathlib import Path
from datetime import datetime
import pprint as pp

import requests
from dotenv import load_dotenv


def download_image(url, folder, token):
    params ={
        'api_key': token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    a = urlparse(url)
    filename = os.path.basename(a.path)
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(filename)
    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    folder = 'images'
    print(len(image_links))
    for image_number, image_link in enumerate(image_links):
        download_image(image_link, folder)


def nasa_apod_photo(token):
    api_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count': 40
    }
    links_url = list()
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    for number, res in enumerate(response.json()):
        if res['media_type'] == 'image':
            links_url.append(res['hdurl'])
    return links_url


def get_img_extension(url):
    img_path = urllib.parse.urlsplit(url).path
    _, img_extension = os.path.splitext(img_path)
    return img_extension


def epic_photo(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': token
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    links = list()
    for link in response.json():
        photo_name = link["image"]
        photo_date = datetime.fromisoformat(link["date"]).strftime("%Y/%m/%d")
        links.append(f'https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{photo_name}.png')
    return links


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    folder = 'images'
    for photo_link in nasa_apod_photo(token):
        print(photo_link)
        download_image(photo_link, folder, token)
    for photo_link in epic_photo(token):
        print(photo_link)
        download_image(photo_link, folder, token)
