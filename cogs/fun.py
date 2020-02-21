from datetime import datetime
from discord.ext import commands
from nltk.corpus import wordnet
from zalgo_text import zalgo

from cogs.urbandict import UrbanDict
from other.utils import Emoji, Utils


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['cursed'], help='Like the say command, except spookier.')
    # @commands.has_role(584267156385169419)
    async def zalgo(self, ctx, *, text: str):
        print(f'User {ctx.author.name} used zalgo to say "{text}" in channel {ctx.channel.name} at {datetime.now().time()}')
        await ctx.send(zalgo.zalgo().zalgofy(text))
        await ctx.message.delete()

    @commands.command(aliases=['echo', 'speak'], help='Make Hamilton say something.')
    # @commands.has_role(584267156385169419)
    async def say(self, ctx, *, text: str):
        print(f'User {ctx.author.name} used echo to say "{text}" in channel {ctx.channel.name} at {datetime.now().time()}')
        await ctx.send(text)
        await ctx.message.delete()

    @commands.command(aliases=['temp'], help='Calculates the given number to Fahrenheit and Celsius.')
    async def temperature(self, ctx, *, number: float):
        CtoF = (number * 9 / 5) + 32
        FtoC = (number - 32) * 5 / 9
        await Utils.embed(ctx, f'Temperature conversion', f'**{number}°C** Celsius to Fahrenheit: **{round(CtoF,2)}°F\n\n{number}°F** Fahrenheit to Celsius: **{round(FtoC,2)}°C**')

    @commands.command(aliases=['def'], help='Searches for a definiton of the given word.')
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
            urbandict = UrbanDict(client=self.client)
            await urbandict.search_urban(ctx=ctx, word=word)


def setup(client):
    client.add_cog(Fun(client))
