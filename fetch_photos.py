import requests
from fetch_config import *

FLICKR_URL = "https://api.flickr.com/services/rest/"

def get_photos():
    api_options = {
        "method": "flickr.photosets.getPhotos",
        "api_key": FLICKR_API_KEY,
        "photoset_id": FLICKR_ALBUM_ID,
        "format": "json",
        "nojsoncallback": "1",
    } 

    photos = requests.get(FLICKR_URL, params=api_options).json()
    return photos

print(get_photos())
