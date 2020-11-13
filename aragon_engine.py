"""Discord Aragon-Bot."""

from discord.ext import commands

from coin import flip
from constants import BOT_TOKEN
from covid import covid_stats
from insults import generate_insult
from meme import meme_builder
from potter_spells import choose_spell
from shkabuse import generate_abuse
from wassepur import choose_dialog
from star_wars_quotes import generate_quote
from yoda_translate import generate_translation

bot = commands.Bot(command_prefix='$')


@bot.command(name='allah', help='A greeting message')
async def allah(ctx):
    """Greeting message.

    Parameters
    -----------
        ctx: object
            channel from which command is called.
    Returns
    -------
        message: str
            Greeting message.
    """
    message = 'Bismillah, ar-Rahman, ar-Rahim'

    await ctx.send(message)


@bot.command(name='covid', help='Latest COVID-19 statistics. Usage: $covid (country_name)')
async def covid(ctx, *args):
    """COVID-19 statistics.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
        *args: Tuple
            Name of country
    Returns
    --------
        card: discord.Embed
            Card containing COVID-19 information for a particular country.
    """
    card = covid_stats(*args)
    await ctx.send(embed=card)


@bot.command(name='hazrat', help="Relive some og Gangs of Wassepur's best dialogues!")
async def hazrat(ctx):
    """Generate random dialogues from Gangs of Wassepur.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        card: discord.Embed
            Card cointaining random dialogue from Gangs of Wassepur.
    """
    card = choose_dialog()
    await ctx.send(embed=card)


@bot.command(name='toss', help="Can't decide what to do? $toss is there just to get you out of misery.")
async def toss(ctx):
    """Toss a coin.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        card: discord.Embed
            Card cointaining Heads/Tails along with a picture.
    """
    card = flip()
    await ctx.send(embed=card)


@bot.command(name='meme', help='Memes commands available: ida, granny, success, why, obama, evil, cry. Usage: $meme (top_text), (bottom_text)')
async def meme(ctx, name, *args):
    """Generate meme with arguments.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
        *args: Tuple
            Top and bottom text for memes.
    Returns
    --------
        card: discord.Embed
            Card cointaining generated meme.
    """
    file, card = meme_builder(name, *args)
    await ctx.send(file=file, embed=card)


@bot.command(name='shakeabuse', help='How would Shakespeare abuse someone?...Hmm?...')
async def shakeabuse(ctx):
    """Generate random abuses.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        card: discord.Embed
            Card cointaining an abuse.
    """
    card = generate_abuse()
    await ctx.send(embed=card)


@bot.command(name='pic', help='See your awesome display picture!')
async def pic(ctx):
    """Display profile picture.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        url: str
            Profile picture.
    """
    sender = ctx.message.author
    await ctx.send(sender.avatar_url)


@bot.command(name='insult', help='Want to insult someone? Type $insult (name) and enjoy!')
async def insult(ctx, name):
    """Generate random insults.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
        name: str
            Name of the person to be insulted.
    Returns
    --------
        card: discord.Embed
            Card cointaining an insult.
    """
    card = generate_insult(name)
    await ctx.send(embed=card)


@bot.command(name='spell', help='Are you a muggle or a wizard? Hit $spell and try!')
async def spell(ctx):
    """Generate random spells from Harry Potter.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        card: discord.Embed
            Card cointaining spell and its explanation.
    """
    card = choose_spell()
    await ctx.send(embed=card)


@bot.command(name='jedi')
async def jedi(ctx):
    """Generate random quotes from Star Wars.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
    Returns
    --------
        card: discord.Embed
            Card cointaining random quote from Star Wars.
    """
    card = generate_quote()
    await ctx.send(embed=card)


@bot.command(name='yoda', help='Translates text in a way Yoda would speak! ')
async def yoda(ctx, *args):
    """Translate message to Yodish.

    Parameters
    -----------
        ctx: object
            The channel from which command is called.
        *args: Tuple
            Message to be translated to Yodish.
    Returns
    --------
        card: discord.Embed
            Card cointaining 'Yodish' translated message.
    """
    card = generate_translation(*args)
    await ctx.send(embed=card)


bot.run(BOT_TOKEN)
