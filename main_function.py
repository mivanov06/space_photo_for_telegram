import os
from pathlib import Path
from urllib.parse import urlparse

import requests


def download_image(url, folder, token, prefix_name=''):
    params = {
        'api_key': token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    a = urlparse(url)
    filename = os.path.basename(a.path)
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(filename)
    with open(f'{folder}/{prefix_name}_{filename}', 'wb') as file:
        file.write(response.content)

