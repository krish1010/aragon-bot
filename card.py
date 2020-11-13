import discord


def make_card(title, **kwargs):

    color = kwargs.get('color') or 0x191919
    thumbnail = kwargs.get('thumbnail')
    fields = kwargs.get('fields')
    image = kwargs.get('image')
    card = discord.Embed(title=title, color=color)
    if thumbnail:
        card.set_thumbnail(url=thumbnail)
    if fields:
        for key, value in fields.items():
            card.add_field(name=key, value=value)
    if image:
        card.set_image(url=image)
    return card
