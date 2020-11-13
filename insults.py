import requests

from card import make_card

INSULT_URL = 'https://insult.mattbas.org/api/insult.txt?who='


def generate_insult(name):
    response = requests.get(f'{INSULT_URL}{name}')
    card = make_card(title=response.text, colour=0xF5C518)
    return card
