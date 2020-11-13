import random
from card import make_card

COIN = {
    'Heads': 'https://jkscoinworld.com/wp-content/uploads/2018/05/floral-2-300x300.jpg',
    'Tails': 'https://pngimage.net/wp-content/uploads/2018/06/1-rupee-coin-png-.png'
}


def flip():
    print('here')
    key = random.choice(['Heads', 'Tails'])
    print(key)
    value = COIN[key]
    card = make_card(title=key, image=value)
    return card
