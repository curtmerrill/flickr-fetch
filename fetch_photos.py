import requests
from fetch_config import *

FLICKR_URL = "https://api.flickr.com/services/rest/"

# This gets the album details, which includes a list of photos
def get_album():

    api_options = {
        "method": "flickr.photosets.getPhotos",
        "api_key": FLICKR_API_KEY,
        "photoset_id": FLICKR_ALBUM_ID,
        "format": "json",
        "nojsoncallback": "1",
    } 

    album = requests.get(FLICKR_URL, params=api_options).json()
    return album

print(get_album())

# This loops through the list of photos fetched earlier and gets
# more detail for each photo
def get_photos():

    # Requires 2 calls per photo:
    # flickr.photos.getInfo for date, title, tags, etc.
    # flickr.photos.getSizes for thumbnail/full-size img urls

    api_options = {
        # "method": "flickr.photosets.getPhotos",
        "api_key": FLICKR_API_KEY,
        "photoset_id": FLICKR_ALBUM_ID,
        "format": "json",
        "nojsoncallback": "1",
    } 

    pass
