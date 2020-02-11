import json

import discord
from discord.ext import commands
from nltk.corpus import wordnet
from zalgo_text import zalgo

from cogs.urbandict import UrbanDict
from other.utils import Emoji, Utils


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['cursed'])
    @commands.has_role(584267156385169419)
    async def zalgo(self, ctx, *, text: str):
        await ctx.send(zalgo.zalgo().zalgofy(text))
        await ctx.message.delete()

    @commands.command(aliases=['echo', 'speak'])
    @commands.has_role(584267156385169419)
    async def say(self, ctx, *, text: str):
        await ctx.send(text)
        await ctx.message.delete()

    @commands.command(aliases=['temp'])
    async def temperature(self, ctx, *, temperature: float):
        CtoF = (temperature * 9 / 5) + 32
        FtoC = (temperature - 32) * 5 / 9
        await Utils.embed(ctx, f'Temperature conversion', f'**{temperature}°C** Celsius to Fahrenheit: **{round(CtoF,2)}°F\n\n{temperature}°F** Fahrenheit to Celsius: **{round(FtoC,2)}°C**')

    @commands.command(aliases=['def'])
    # @commands.cooldown(rate=3)
    async def define(self, ctx, *, word: str):
        # in all honesty i didn't really bother to try and understand this
        # https://pythonprogramming.net/wordnet-nltk-tutorial/
        try:
            await ctx.send(f'Searching for a definition of **{word}**...')

            syns = wordnet.synsets(word)

            definition = syns[0].definition()
            examplesList = syns[0].examples()
            synonymsList = []
            antonymsList = []

            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonymsList.append(l.name())
                    synonymsList = list(dict.fromkeys(synonymsList))
                    if l.antonyms():
                        antonymsList.append(l.antonyms()[0].name())

            synonyms = json.dumps(synonymsList).replace("\"", "").replace("[", "").replace("]", "").replace("_", " ")
            antonyms = json.dumps(antonymsList).replace("\"", "").replace("[", "").replace("]", "").replace("_", " ")
            examples = json.dumps(examplesList).replace("\'", "").replace("[", "").replace("]", "")

            # await ctx.send(f'word: {word}  definition: {definition}')

            embed = discord.Embed(title=f'{word}', description=f'{definition}', color=0x55ffff)
            if examplesList:
                embed.add_field(name=f'Examples', value=f'{examples}', inline=True)
            if synonymsList:
                embed.add_field(name=f'Synonyms', value=f'{synonyms}', inline=False)
            if antonymsList:
                embed.add_field(name=f'Antonyms', value=f'{antonyms}', inline=False)
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send(f'{Emoji.hamiltonSleep} There is no definition for **{word}**.')
            await ctx.send(f'Searching urban dictionary for a definition...')
            await UrbanDict(commands.Cog).searchUrban(ctx=ctx, word=word)


def setup(client):
    client.add_cog(Fun(client))
