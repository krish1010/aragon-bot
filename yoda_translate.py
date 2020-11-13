import requests
from card import make_card

TRANSLATE_URL = 'http://yoda-api.appspot.com/api/v1/yodish?text='
THUMBNAIL = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bbyoda-1575303784.jpeg?resize=768:*'


def generate_translation(*args):
    text = ' '.join(args)
    response = requests.get(f'{TRANSLATE_URL}{text}')
    quote = response.json()['yodish']
    color = 0x00ff00
    card = make_card(title=quote, colour=color, thumbnail=THUMBNAIL)
    return card
