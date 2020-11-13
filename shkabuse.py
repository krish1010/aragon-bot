from shakeabuse import make_abuse
from card import make_card

THUMBNAIL = 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Shakespeare.jpg'


def generate_abuse():
    title = make_abuse.generate_random_abuse()
    color = 0xd6537a
    card = make_card(title=title, color=color, thumbnail=THUMBNAIL)
    return card
