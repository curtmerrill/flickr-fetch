import json
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

    album_response = requests.get(FLICKR_URL, params=api_options)
    album_response.raise_for_status()
    album = album_response.json()
    if album["stat"] != "ok":
        raise Exception("error returned from Flickr")
    else:
        return album['photoset']['photo']


my_photos = []

for p in get_album():
    single_photo = {
        "title": p["title"],
        "img_sm": "http://farm{farm}.staticflickr.com/{server}/{id}_{secret}_n.jpg".format(**p),
        "img_lg": "http://farm{farm}.staticflickr.com/{server}/{id}_{secret}_c.jpg".format(**p),
    }
    my_photos.append(single_photo)

photos_json = json.dumps(my_photos)
print(photos_json)
