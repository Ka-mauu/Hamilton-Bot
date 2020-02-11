import discord
from discord.ext import commands
import json
import urllib.parse
import urllib.request
from other.utils import *

_URBANDICT_URL = "http://api.urbandictionary.com/v0/define?term="


def _run_urbandict(search):
    safe_search = ""
    words = ' '.join(search.split()).split(' ')
    for idx, word in enumerate(words):
        if len(words) == idx+1:
            safe_search += "%s" % urllib.parse.quote_plus(word)
        else:
            safe_search += "%s+" % urllib.parse.quote_plus(word)
    response = urllib.request.urlopen(_URBANDICT_URL + safe_search)
    return json.loads(response.read())


def urbandict(word):
    return _run_urbandict(word)


class UrbanDict(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def searchUrban(self, ctx, *, word: str):
        # this is why you dont code late at night - fix later...

        # get the list inside of a list
        urb = urbandict(word).get('list')
        # make it a string so we can modify it
        tostring = json.dumps(urb)
        if tostring == '[]':
            await ctx.send(f':x: There is no urban dictionary definition for **{word}**.')
            return
        if tostring.endswith(']'):
            tostring = tostring[1:-1]  # cut off the square brackets so it's readable as a list
        # give us the first result
        sep = ', {'
        rest = tostring.split(sep, 1)[0]
        # back in to a list
        u = json.loads(rest)
        word = u['word']
        author = u['author']
        definition = u['definition'].replace("[", "").replace("]", "")
        example = u['example'].replace("[", "").replace("]", "")

        embed = discord.Embed(title=f'{word}', description=f'{definition}', color=color)
        embed.add_field(name=f'Example', value=f'{example}', inline=True)
        embed.add_field(name=f'Author', value=f'{author}', inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['ud', 'urbandictionary'])
    # @commands.cooldown(rate=3)
    async def urban(self, ctx, *, word: str):
        await self.searchUrban(ctx=ctx, word=word)


def setup(client):
    client.add_cog(UrbanDict(client))
