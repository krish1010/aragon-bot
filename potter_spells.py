import random
from card import make_card

SPELLS = {
    "id": "harry_potter_spells_cheat_sheet",
    "name": "Harry Potter spells",
    "description": "List of Harry Potter spells",
    "metadata": {
        "sourceName": "Harrypotterspells",
        "sourceUrl": "http://harrypotterspells.net/"
    },
    "template_type": "reference",
    "section_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "W"],
    "sections": {
        "A": [{
            "key": "Accio",
            "val": "Brings an object to you"
        }, {
            "key": "Aguamenti",
            "val": "Creates a gush of water from the tip of the spell caster’s wand"
        }, {
            "key": "Alohomora",
            "val": "Opens locks"
        }, {
            "key": "Aparecium",
            "val": "Makes invisible ink become visible"
        }, {
            "key": "Avada Kedavra",
            "val": "The Unforgivable Curse, kills your opponent"
        }, {
            "key": "Avifors",
            "val": "Turns things into birds"
        }, {
            "key": "Avis",
            "val": "Makes birds fly out of the end of your wand"
        }], "B": [{
            "key": "Bombarda",
            "val": "Causes a small, locally contained explosion"
        }], "C": [{
            "key": "Colloportus",
            "val": "Closes a door and binds it so that it can’t be opened"
        }, {
            "key": "Confringo",
            "val": "The Blasting Curse; Causes the item targeted to explode"
        }, {
            "key": "Confundus",
            "val": "Confounds your target, or makes them temporarily confused"
        }, {
            "key": "Conjunctivitis",
            "val": "Damages the eyesight of your opponent, making them seem to have pink eye"
        }, {
            "key": "Crucio",
            "val": "The Second Unforgivable Curse, the Cruciatus Curse; Tortures your opponent mercilessly"
        }], "D": [{
            "key": "Deletrius",
            "val": "Erases the last spell cast by a wand so that it can’t be discovered"
        }, {
            "key": "Densaugeo",
            "val": "Makes teeth grow out of control"
        }, {
            "key": "Diffindo",
            "val": "Makes seams split open, severs an object into two pieces"
        }, {
            "key": "Dissendium",
            "val": "Opens a specific passageway into a cellar, may be useful in other instances; may be only a password"
        }, {
            "key": "Duro",
            "val": "Turns an item to stone"
        }], "E": [{
            "key": "Engorgio",
            "val": "Makes an item larger, as in swollen"
        }, {
            "key": "Episkey",
            "val": "Heals relatively minor wounds"
        }, {
            "key": "Evanesco",
            "val": "Causes an item to immediately dissolve away, as if it had never existed"
        }, {
            "key": "Expecto Patronum",
            "val": "Creates Patronus"
        }, {
            "key": "Expelliarmus",
            "val": "Disarms the target of the spell, such as knocking their wand out of their hand"
        }], "F": [{
            "key": "Fera Verto",
            "val": "Transforms animals into water goblets!"
        }, {
            "key": "Ferula",
            "val": "Binds a broken limb with a splint and bandages, tightly wrapped"
        }, {
            "key": "Fidelius",
            "val": "Allows a secret to be hidden within the secret keeper’s soul; very powerful spell"
        }, {
            "key": "Finite Incantatem",
            "val": "Stops any spell"
        }, {
            "key": "Flagrate",
            "val": "Allows the user to write or draw in the air with fire"
        }, {
            "key": "Flipendo",
            "val": "Also knows as the Knockback Jinx, pushes or flips something backwards"
        }, {
            "key": "Furnunculus",
            "val": "Causes a person to break out in boils"
        }], "G": [{
            "key": "Geminio",
            "val": "Creates a duplicate of an item (a twin, as in the zodiacal sign Gemini)"
        }], "H": [{
            "key": "Homorphus",
            "val": "Man-Shape; makes a werewolf or person disguised as an animal resume their human shape"
        }], "I": [{
            "key": "Immobulus",
            "val": "Immobilizes the target"
        }, {
            "key": "Impedimenta",
            "val": "Puts up an impediment that slows down something or someone that is coming toward you"
        }, {
            "key": "Imperio",
            "val": "The third unforgivable curse.  Allows the user to assume complete control of another person"
        }, {
            "key": "Impervius",
            "val": "Repels water from a surface"
        }, {
            "key": "Incarcerous",
            "val": "Conjures up ropes, which then bind an opponent"
        }, {
            "key": "Incendio",
            "val": "Lights a fire"
        }], "L": [{
            "key": "Legilimens",
            "val": "Allows the user to gain access to another’s mind and memories"
        }, {
            "key": "Levicorpus",
            "val": "Turns your opponent upside down and dangles them in thin air"
        }, {
            "key": "Liberacorpus",
            "val": "\"Liberates\", or frees a body that has been caught up by the levicorpus spell"
        }, {
            "key": "Locomotor Mortis",
            "val": "The Leg-Locker Curse; locks an opponent’s legs together"
        }, {
            "key": "Lumos",
            "val": "Creates light, usually by making the tip of the wand glow.  More light can be created using \"lumos maxima\""
        }], "M": [{
            "key": "Mobiliarbus",
            "val": "Used to move a tree from one place to another"
        }, {
            "key": "Mobilicorpus",
            "val": "Used to move a body from one place to another"
        }, {
            "key": "Morsmordre",
            "val": "Used to summon the Dark Mark"
        }, {
            "key": "Muffliato",
            "val": "Causes a buzzing noise to surround a limited area so that those in the area can carry on a private conversation"
        }], "N": [{
            "key": "Nox",
            "val": "Extinguishes light, used to douse the light created by “Lumos”"
        }], "O": [{
            "key": "Obliviate",
            "val": "Makes a person \"oblivious\", erasing their memories of an event"
        }, {
            "key": "Orchideous",
            "val": "Conjures a bunch of flowers from the user’s wand"
        }], "P": [{
            "key": "Petrificus Totalus",
            "val": "Total petrification; petrifies an opponent totally"
        }, {
            "key": "Point Me",
            "val": "The Four Point Spell; makes the user’s wand act like a compass"
        }, {
            "key": "Portus",
            "val": "Turns any item into a Portkey, which can then be used to transport a person or persons to another location."
        }, {
            "key": "Prior Incantato",
            "val": "Reveals to you the last spell that a wand was used to cast"
        }, {
            "key": "Protego",
            "val": "Protects the user, and sends a spell back on an opponent"
        }], "Q": [{
            "key": "Quietus",
            "val": "Makes things quiet, used to muffle \"Sonorus\""
        }], "R": [{
            "key": "Reducio",
            "val": "Shrinks an item"
        }, {
            "key": "Reducto",
            "val": "Blasts solid objects into pieces"
        }, {
            "key": "Relashio",
            "val": "Releases something from being constrained or held"
        }, {
            "key": "Rennervate",
            "val": "Means to energize or wake up"
        }, {
            "key": "Reparo",
            "val": "Repairs broken items"
        }, {
            "key": "Repello",
            "val": "Repels something"
        }, {
            "key": "Repello Muggletum",
            "val": "Makes an area invisible to Muggles"
        }, {
            "key": "Revelio",
            "val": "Causes something that is hidden to be revealed"
        }, {
            "key": "Rictusempra",
            "val": "Causes a person to curl up in laughter, as if being tickled"
        }, {
            "key": "Riddikulus",
            "val": "Makes a boggart assume a “ridiculous” form, thereby making it funny instead of terrifying"
        }], "S": [{
            "key": "Salvio Hexia",
            "val": "Strengthen other protective spells, or to deflect any hexes cast toward a specific location"
        }, {
            "key": "Scourgify",
            "val": "Used to clean dirt or other material off of a surface"
        }, {
            "key": "Sectumsempra",
            "val": "Causes lacerations to appear all over an opponent’s body, as if they had been cut by an invisible sword"
        }, {
            "key": "Serpensortia",
            "val": "Conjures a snake"
        }, {
            "key": "Silencio",
            "val": "Makes the target of the spell unable to make any sound"
        }, {
            "key": "Sonorus",
            "val": "Amplifies the user’s voice"
        }, {
            "key": "Stupefy",
            "val": "Stupefies an opponent, or knocks them insensible temporarily"
        }], "T": [{
            "key": "Tarantallegra",
            "val": "Forces an opponent’s legs to dance uncontrollably"
        }, {
            "key": "Tergeo",
            "val": "Scours something clean"
        }], "W": [{
            "key": "Waddiwasi",
            "val": "Removes a stuck object, as in a wad of gum that is stuck in a keyhole"
        }, {
            "key": "Wingardium Leviosa",
            "val": "Allows the user to make an object levitate; the first spell taught in the Harry Potter movies"
        }]
    }
}
THUMBNAIL = 'https://cdn.pixabay.com/photo/2017/05/10/18/11/harry-potter-2301464_960_720.png'


def choose_spell():
    spell = random.choice(SPELLS['sections'][random.choice(SPELLS['section_order'])])
    title = 'Wave your wand!'
    color = 0x2edd17
    fields = {
        'Spell': spell['key'],
        'Explanation': spell['val']
    }
    card = make_card(title=title, colour=color, thumbnail=THUMBNAIL, fields=fields)
    return card
