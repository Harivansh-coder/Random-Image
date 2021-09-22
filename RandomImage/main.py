"""
 A simple python scripts to get random dog images.
 this is a simple demonstration for the use of following python library.

 1> Pillow (to open the image)
 2> Request (to retrieve data)
 3> JSON API implemented in python 
"""

import urllib.request
from PIL import Image

import requests


# the free api endpoint
URL= "https://dog.ceo/api/breeds/image/random"

# creating request
r = requests.get(url=URL)

# json response received
data = r.json()

# extracting image url from response
image_url = data['message']


# code to show the image
urllib.request.urlretrieve(
  image_url,
   "image.jpg")
  
img = Image.open("image.jpg")
img.show()
