import discord
import random
import sys
import os
import psutil
import requests
import json
import eightball_responses
import datetime
import asyncio
from nltk.corpus import wordnet
from urbandict import urbandict
from discord.ext import commands
from zalgo_text import zalgo
from pathlib import Path
from configparser import ConfigParser
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# prefixes - for some reason the prefixes with spaces have to be first in the list.. /shrug
client = commands.Bot(command_prefix=['ok. ', 'Ok. ', 'oK. ', 'OK. ', 'ok! ', 'Ok! ', 'oK! ', 'OK! ', 'ok.', 'Ok.', 'oK.', 'OK.', 'ok!', 'Ok!', 'oK!', 'OK!'])

synonymsStupid = ['stupid', 'dense', 'thick', 'simple', 'dull', 'blockheaded', 'numskulled']

color = 0x55ffff

config = ConfigParser()
datafile = 'data.ini'
config.read(datafile)

instance = config.getint('main', 'instance')
status = config.get('main', 'status')

instance += 1  # increase instance integer by 1 on launch

config.set('main', 'instance', str(instance))


def write():  # after setting a value you need to call write()
    with open(datafile, 'w+') as configfile:
        config.write(configfile)


def read():  # before reading a value you need to call read()
    config.read(datafile)


write()


class Emoji():  # for easy access
    hamiltonConfuse = '<:okHamiltonConfuse:630553287145422871>'
    hamiltonWoke = '<:okHamiltonWoke:630553285488803850>'
    hamiltonDread = '<:okHamiltonDread:630553286986039356>'
    hamiltonOWO = '<:okHamiltonOwO:630553287111737354>'
    hamiltonEyeroll = '<:okHamiltonEyeroll:630553283890642974>'
    hamiltonWisdom = '<:okHamiltonWisdom:636473613238665227>'
    hamiltonGem = '<:okHamiltonGem:669100365311901698>'
    hamiltonCool = '<:okHamiltonCool:635747888672145408>'
    heads = '<:okHeads:676292505427247104>'
    tails = '<:okTails:676292506832601099>'
    wisp = '<:okWilloWisp:676253396545568770>'


class Methods():

    def owner(ctx):
        return ctx.author.id == 259536485340938242

    async def embed(self, ctx, title: str, description: str):
        await ctx.send(embed=discord.Embed(title=title, description=description, color=color))

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


methods = Methods()


class Events():

    @client.event
    async def on_ready():
        print('Hello!')
        # update status
        await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await client.get_channel(672942729864413184).send(f'<:okHamiltonOwO:630553287111737354> I have awakened! Serve me and I shall return the favour.')

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            r = ['That is not a proper command..', 'I cannot perform a non-existent request.', 'Are you going to give me something to do, or what?', 'I cannot just sit here idly, what do you want me to do?']
            await ctx.send(random.choice(r))
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f':x: You do not have the permissions to perform this command!')
        elif isinstance(error, commands.MissingRequiredArgument):
            pass
        else:
            print(f'Something went wrong. Error: \n{error, type(error)}\nTime of error: {datetime.datetime.now()}')
            await ctx.send(f'Something went very wrong, let us laugh at Lerrific\'s incompetence... ```{error, type(error)}```')


class Commands():

    @commands.check(Methods.owner)
    @client.command(aliases=['oooh', 'ooh', 'oooooh', 'ooooh'])
    async def _oooh(ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/489965104784474124/676295367343472640/oooooooooooooooooh.jpg')
        await ctx.message.delete()

    @client.command(aliases=['info'])
    async def _info(ctx):
        await methods.embed(ctx, f'{Emoji.hamiltonGem} Info', f'*You want me to tell you about myself? Well of course. I am Hamilton, your almighty god. Any questions? No? OK.*\n\n**Status:** What the hell are you saying? I am up and running. Perfectly healthy... What about you? You are nothing but a frail clump of mortal flesh. The only way to completely redeem your pathetic existence is to serve me!\n\n**How much cheese I own:** In my home dimension, I have cut all cheese trade throughout the entire universe, practically making the mice population there extinct. I own only {random.randrange(1337)} cheese wheels in this realm though.\n\n**Favorite number:** It is eight.\n\n**Favorite colour:** Do you really have to ask? What do you think, ORANGE? It\'s baby blue obviously.\n\n**My colour palette (in hex):** [123456 - Fur / Pupils] [55ffff - Gem] [fad420 - Eyes] [ff55aa - Mouth]\n\n**Owner:** I belong to no one. Although I have a particular affinity for lerrific#6574.\n\n**Bot creation date:** 10:00 AM 01-Feb-20\n\n**Total system CPU usage:** {psutil.cpu_percent()}%\n\n**Total system memory usage:** {dict(psutil.virtual_memory()._asdict()).get("percent")}%\n\n**Bot instance:** {instance}')

    @client.command(aliases=['status'])
    @commands.has_role(584267156385169419)
    async def _status(ctx, *, status: str):
        config.set('main', 'status', str(status))
        write()
        await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await ctx.send(f'Status set to **{status}**')

    @client.command(aliases=['ping'])
    async def _ping(ctx):
        await methods.embed(ctx, f'Latency', f'{round(client.latency * 1000)}ms')

    @client.command(aliases=['restart'])
    @commands.check(Methods.owner)
    async def _restart(ctx):
        await ctx.send(f'I will come back...')
        os.execl(sys.executable, sys.executable, * sys.argv)

    @client.command(aliases=['stop', 'die', 'kill', 'quit'])
    @commands.check(Methods.owner)
    async def _stop(ctx):
        await ctx.send(f'{Emoji.hamiltonEyeroll} Just for now...')
        sys.exit()

    @client.command(aliases=['8ball', 'eightball'])
    async def _8ball(ctx, *, question: str):
        answer = eightball_responses.responses(question)
        await methods.embed(ctx, f'🔮 What is it that troubles you?', f'{Emoji.hamiltonConfuse} You ask the question, \"**{question.capitalize()}?**\"\n\n{Emoji.hamiltonWisdom} and I answer... \"**{random.choice(answer)}**\"')

    @client.command(aliases=['zalgo', 'cursed'])
    @commands.has_role(584267156385169419)
    async def _zalgo(ctx, *, text: str):
        await ctx.send(zalgo.zalgo().zalgofy(text))
        await ctx.message.delete()

    @client.command(aliases=['say', 'echo', 'speak'])
    @commands.has_role(584267156385169419)
    async def _say(ctx, *, text: str):
        await ctx.send(text)
        await ctx.message.delete()

    @client.command(aliases=['temperature', 'temp'])
    async def _temperature(ctx, *, temperature: float):
        CtoF = (temperature * 9 / 5) + 32
        FtoC = (temperature - 32) * 5 / 9
        await methods.embed(ctx, f'Temperature conversion', f'**{temperature}°C** Celsius to Fahrenheit: **{round(CtoF,2)}°F\n\n{temperature}°F** Fahrenheit to Celsius: **{round(FtoC,2)}°C**')

    @client.command(aliases=['urban', 'ud', 'urbandictionary'])
    async def _urban(ctx, *, word: str):
        await methods.searchUrban(ctx=ctx, word=word)

    @client.command(aliases=['define'])
    async def _define(ctx, *, word: str):
        # in all honesty i didn't really bother to try and understand this
        # https://pythonprogramming.net/wordnet-nltk-tutorial/
        syns = wordnet.synsets(word)
        if json.dumps(syns) == '[]':
            await ctx.send(f':x: There is no definition for **{word}**.')
            await ctx.send(f'Searching urban dictionary for a definition...')
            await methods.searchUrban(ctx=ctx, word=word)
            return
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

        await ctx.send(f'word: {word}  definition: {definition}')

        embed = discord.Embed(title=f'{word}', description=f'{definition}', color=color)
        if examplesList:
            embed.add_field(name=f'Examples', value=f'{examples}', inline=False)
        if synonymsList:
            embed.add_field(name=f'Synonyms', value=f'{synonyms}', inline=False)
        if antonymsList:
            embed.add_field(name=f'Antonyms', value=f'{antonyms}', inline=False)
        await ctx.send(embed=embed)


class Points():

    async def checkForPoints(ctx):
        if not (config.has_option('points', f'{ctx.message.author.id}.bal')):
            await ctx.send(f':x: You do not have any wisps! Register yourself with `ok.wisps`')
            return False
        else:
            return True

    @client.command(aliases=['points', 'balance', 'bal', 'wisps'])
    async def _points(ctx):
        read()

        if not (config.has_option('points', f'{ctx.message.author.id}.bal')):
            config.set('points', f'{ctx.message.author.id}.bal', '100')
            write()

        points = config.getint('points', f'{ctx.message.author.id}.bal')

        await methods.embed(ctx, f'{Emoji.wisp} Deposit', f'**{ctx.message.author.name}** has accumulated **{points}** will-o-wisps.')
        """img = Image.open('resources\\points_balance.png')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('resources\\UASQUARE.TTF', 30)
        draw.text((100, 155), 'Test 12345', (0, 0, 0), font=font)
        img.save('resources\\points_balance_r.png')
        await ctx.send(file=discord.File('resources\\points_balance_r.png'))"""

    @client.command(aliases=['coinflip', 'cointoss'])
    async def _coinflip(ctx, bet: int, coin: str):
        read()

        if not await Points.checkForPoints(ctx):
            return

        points = config.getint('points', f'{ctx.message.author.id}.bal')

        if(bet > points):
            await ctx.send(f':x: You cannot bet more wisps than you own! You have {points} wisps.')
            return

        hamiltonBet = random.randrange(bet, bet * 1.5)

        def check(m):
            return m.content.lower() == 'ok'

        await methods.embed(ctx, 'Are you sure you want to do this?', f'Do you wish to sacrifice **{bet}** will-o-wisps for a chance of a greater blessing? Or worse, a chance to lose it?\n\nType **OK** to continue...')
        try:
            confirm = await client.wait_for('message', check=check, timeout=7)
        except asyncio.TimeoutError:
            await ctx.send(':x: You did not respond in time, cancelling coin flip.')
            return

        if(coin.lower() == 'heads'):
            response = f'You bet **{bet}** on heads {Emoji.heads}. I bet **{hamiltonBet}** on tails! {Emoji.tails}'
        elif(coin.lower() == 'tails'):
            response = f'You bet **{bet}** on tails {Emoji.tails}. I bet **{hamiltonBet}** on heads! {Emoji.heads}'
        else:
            await ctx.send(':x: That is not a side of a coin, moron... Choose heads or tails.')
            return

        await methods.embed(ctx, title=f'Coinflip', description=response)
        await asyncio.sleep(1)
        await ctx.send(embed=discord.Embed(title='Flipping...', color=color))
        await asyncio.sleep(2)
        result = random.choice(['heads', 'tails'])
        if(result == 'heads' and coin.lower() == 'heads'):
            response2 = f'The coin landed on heads {Emoji.heads}, you win... {Emoji.hamiltonDread}\n**+ {hamiltonBet}** wisps was added to your account.'
            points += hamiltonBet + bet
            points -= bet
        elif(result == 'heads' and coin.lower() == 'tails'):
            response2 = f'The coin landed on heads {Emoji.heads}, I win! {Emoji.hamiltonCool}\n**- {hamiltonBet + bet}** wisps was taken from your account.'
            points -= hamiltonBet + bet
            points += bet
        elif(result == 'tails' and coin.lower() == 'tails'):
            response2 = f'The coin landed on tails {Emoji.tails}, you win... {Emoji.hamiltonDread}\n**+ {hamiltonBet}** wisps was added to your account.'
            points += hamiltonBet + bet
            points -= bet
        elif(result == 'tails' and coin.lower() == 'heads'):
            response2 = f'The coin landed on tails {Emoji.tails}, I win! {Emoji.hamiltonCool}\n**- {hamiltonBet + bet}** wisps was taken from your account.'
            points -= hamiltonBet + bet
            points += bet

        await methods.embed(ctx, f'Coinflip Result', response2)

        config.set('points', f'{ctx.message.author.id}.bal', str(points))
        write()

    @client.command(aliases=['odds', 'chance'])
    async def _odds(ctx, bet: int, chance: int):
        read()

        if not await Points.checkForPoints(ctx):
            return

        points = config.getint('points', f'{ctx.message.author.id}.bal')

        if(bet > points):
            await ctx.send(f':x: You cannot bet more wisps than you own! You have {points} wisps.')
            return

        await ctx.send('e')


class Errors():

    @Commands._say.error
    async def _say_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.say [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._status.error
    async def _status_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.status [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._8ball.error
    async def _8ball_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.8ball [yes/no question]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._zalgo.error
    async def _zalgo_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.zalgo [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._temperature.error
    async def _temperature_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.temperature [number]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._define.error
    async def _define_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.define [word]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._urban.error
    async def _urban_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.urban [word]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Points._coinflip.error
    async def _coinflip_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = [f'You need to specify an amount of wisps you\'re willing to bet, then choose heads {Emoji.heads} or tails {Emoji.tails}. The usage goes as follows; `ok.coinflip [amount] [heads/tails]`']
            await ctx.send(f':x: {random.choice(r)}')


client.run(open(Path("../token.txt")).read())
