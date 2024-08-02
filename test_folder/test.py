import numpy
import pandas as pd
import json
import csv

from nasapy import Nasa
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

#https://api.nasa.gov/
nasa = Nasa(key='DEMO_KEY')

#date = yyyy-mm-dd
picture = nasa.picture_of_the_day(date = '1999-01-19')
# print(picture)
print(picture['url'])

response = requests.get(picture['url'])
img = Image.open(BytesIO(response.content))
img.save('nasa_image.jpg')