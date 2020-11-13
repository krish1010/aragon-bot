import requests

from card import make_card

QUOTE_URL = 'http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote'
THUMBNAIL = 'https://cdn.pixabay.com/photo/2015/12/13/12/58/yoda-1091030_960_720.jpg'


def generate_quote():
    headers = {
        'accept': 'text/plain'
    }
    response = requests.get(QUOTE_URL, headers=headers)
    quote = response.json()['starWarsQuote']
    card = make_card(title=quote, colour=0xF5C518, thumbnail=THUMBNAIL)
    return card
