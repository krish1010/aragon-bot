"""Gangs of Wassepur dialogues."""

import random
from card import make_card

THUMBNAIL = 'https://freaky5.com/wp-content/uploads/2018/07/SARDAR_KHAN-768x512.jpg'

WASSEPUR_DIALOGUES = [
    'Maarenge nahin saale ko. Keh ke lenge uski.',
    'Aad chahe jitna bada ho jaaye, laad ke neeche rehta hai.',
    'Beta, tumse na ho paayega.',
    'Jaise loha lohe ko kaat ta hai, waise chutiya hi toh chutiye ko kaatega na?',
    'Tumhein yaad kar kar ke, haath dukh gaya humara.',
    'Yeh Wasseypur hai. Yahan kabootar bhi ek pankh se '
    'udta hai, aur doosre se apna ijjat bachata hai.',
    'Har chedah mein bandook daalo. '
    'Aur itna goli maaro ki Faisal Khan ke qila ko Hawa Mahal bana do.',
    'Saala chaabhi kahan hai? Gaand mein ghusa diye ho kya chaabhi sab?',
    'Jab tak iss desh mein saneema hai, tab tak log chutiye bante rahenge.',
    'Baap ka, dada ka, bhai ka; sabka badla lega re tera Faisal.',
    'Eee dhande mein do cheezon pe kabhi bharosa nahin karna chahiye. '
    'Ek toh khud se paida hone waale khauff pe, '
    'aur doosra kisi ke saath pe. Ek hi toh jaan hai. Ya toh Allah lega ya mohalla lega.',
    'Hum aapka dukna lootne ke liye aaye hain. Police ko phone mat karna, warna goli maar denge.',
    'Sach bol de bhosdi ke! Ab toh sach bol de bhosdi ke!',
    'Khana khao, taqat aayega. Bahar jaake bezzatti mat karana.',
    'Sardar Khan naam hai humara. Bata dijiyega sabko.',
]


def choose_dialog():
    """Return random dialogues from Gangs of Wassepur.
    
    Returns
    -------
        card: discord.Embed
            Card containing random dialogue from Gangs of Wassepur.
    """
    title = random.choice(WASSEPUR_DIALOGUES)
    color = 0xF5C518
    card = make_card(title=title, color=color, thumbnail=THUMBNAIL)
    return card
