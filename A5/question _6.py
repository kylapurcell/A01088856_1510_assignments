import requests
import json


def get_api_info():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=y1eJsAGH9K6MuftCjGwHq9Wm7znADIePqQiOzksD')
    response.raise_for_status()
    image = json.loads(response.text)
    return image


def get_image_url():
    image = get_api_info()
    return image['url']


def get_image_description():
    image = get_api_info()
    return image['explanation']


def website():
    name = input('What is your name? ')
    sentence = input('Enter a sentence about yourself for the webpage')
    with open('index.html', 'w') as file_object:
        line = '<!doctype html>' \
               '<html lang="en">' \
               '<head><meta charset="utf-8">' \
               '<title>Introduction</title>' \
               '<meta name="description" content="User’s Webpage">' \
               '<meta name="author" content= "Your name goes here ">' \
               '<link rel="stylesheet" href="css/styles.css?v=1.0">' \
               '</head>' \
               '<body>' \
               '<center>' \
               '<h1>' + name + '</h1>' \
               '</center>' \
                + sentence + \
               '<img src= ' + get_image_url() + '>'\
               '<p>' + get_image_description() + '</p>'\
               '</body>' \
               '</html>'
        file_object.write(line)

website()


website()

