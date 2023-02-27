import argparse
import requests

from main_function import download_image


def fetch_spacex_last_launch(launch_id='latest'):
    api_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(api_url)
    response.raise_for_status()
    image_links = response.json()['links']['flickr']['original']
    folder = 'images'
    for image_link in image_links:
        download_image(image_link, folder, prefix_name='spacex_launch')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download SpaseX photo')
    parser.add_argument('-i', '--id', help='launch id', default='latest')
    args = parser.parse_args()
    launch_id = args.id
    fetch_spacex_last_launch(launch_id)
