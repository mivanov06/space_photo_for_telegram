import os
import urllib
from urllib.parse import urlparse
from pathlib import Path
from datetime import datetime
import pprint as pp

import requests
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    folder = 'images'
