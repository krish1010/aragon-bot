import base64
import json

import discord
import requests
from card import make_card

API_KEY = 'a5358b5d5b0fb2728cd24f13bbbb01'
GENERATE_MEME = 'https://memebuild.com/api/1.0/generateMeme'
MEME_GENERATED_PATH = 'attachment://image.jpg'

IMAGES = {
    'ida': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/i-dont-always.jpg',
    'granny': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/granny.jpg',
    'success': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/success-kid.jpg',
    'why': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/why-would-you.jpg',
    'obama': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/obama.jpg',
    'evil': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/evil-kid.jpg',
    'cry': 'https://s3-us-west-2.amazonaws.com/memebuilder/default/first-world-probs.jpg',
}


def meme_builder(name, *args):
    text = ' '.join(args).split(',')

    headers = {
        'API-KEY': API_KEY
    }
    body = {
        "topText": text[0],
        "bottomText": text[1],
        "imgUrl": IMAGES.get(name)
    }
    response = requests.post(GENERATE_MEME, data=json.dumps(body), headers=headers)
    image = response.text.split(',', 1)[1].encode('utf-8')

    file = build_image(image)
    card = make_card(title='Here you go...', colour=0xF5C518, image=MEME_GENERATED_PATH)
    return file, card


def build_image(image):
    recovered = base64.decodebytes(image)
    with open('image.jpg', 'wb') as f:
        f.write(recovered)

    file = discord.File("image.jpg")
    return file
