import discord
import random
import sys
import os
import psutil
import pprint
import requests
import json
import nltk
import eightball_responses
import datetime
from nltk.corpus import wordnet
from urbandict import urbandict
from configparser import ConfigParser
from enum import Enum
from discord.ext import commands
from zalgo_text import zalgo
from pathlib import Path

# prefixes
client = commands.Bot(command_prefix=['ok. ', 'Ok. ', 'oK. ', 'OK. ', 'ok! ', 'Ok! ', 'oK! ', 'OK! ', 'ok.', 'Ok.', 'oK.', 'OK.', 'ok!', 'Ok!', 'oK!', 'OK!'])

# config start

config = ConfigParser()
config.read('data.ini')

instance = config.getint('main', 'instance')
status = config.get('main', 'status')

instance += 1  # increase instance integer by 1 on launch

config.set('main', 'instance', str(instance))


def write():
    with open('data.ini', 'w+') as configfile:
        config.write(configfile)


write()

# config end


class Emoji():  # for easy access
    hamiltonConfuse = '<:okHamiltonConfuse:630553287145422871>'
    hamiltonWoke = '<:okHamiltonWoke:630553285488803850>'
    hamiltonDread = '<:okHamiltonDread:630553286986039356>'
    hamiltonOWO = '<:okHamiltonOwO:630553287111737354>'
    hamiltonEyeroll = '<:okHamiltonEyeroll:630553283890642974>'
    hamiltonWisdom = '<:okHamiltonWisdom:636473613238665227>'
    hamiltonGem = '<:okHamiltonGem:669100365311901698>'


class Methods():

    def chkLerrific(ctx):
        return ctx.author.id == 259536485340938242

    async def searchUrban(self, ctx, *, word: str):
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

        embed = discord.Embed(title=f'{word}', description=f'{definition}', color=0x55ffff)
        embed.add_field(name=f'Example', value=f'{example}', inline=False)
        embed.add_field(name=f'Author', value=f'{author}', inline=False)
        await ctx.send(embed=embed)


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
            await ctx.send(':x: You do not have the permissions to perform this command!')
        else:
            print(f'Something went wrong. Error: \n{error, type(error)}\nTime of error: {datetime.datetime.now()}')


class Commands():

    @client.command(aliases=['info'])
    async def _info(ctx):
        embed = discord.Embed(title=f'{Emoji.hamiltonGem} Info',
                              description=f'*You want me to tell you about myself? Well of course. I am Hamilton, your almighty god. Any questions? No? OK.*\n\n**Status:** What the hell are you saying? I am up and running. Perfectly healthy... What about you? You are nothing but a frail clump of mortal flesh. The only way to completely redeem your pathetic existence is to serve me!\n\n**How much cheese I own:** In my home dimension, I have cut all cheese trade throughout the entire universe, practically making the mice population there extinct. I own only {random.randrange(1337)} cheese wheels in this realm though.\n\n**Favorite number:** It is eight.\n\n**Favorite colour:** Do you really have to ask? What do you think, ORANGE? It\'s baby blue obviously.\n\n**My colour palette (in hex):** [123456 - Fur / Pupils] [55ffff - Gem] [fad420 - Eyes] [ff55aa - Mouth]\n\n**Owner:** I belong to no one. Although I have a particular affinity for lerrific#6574.\n\n**Bot creation date:** 10:00 AM 01-Feb-20\n\n**Total system CPU usage:** {psutil.cpu_percent()}%\n\n**Total system memory usage:** {dict(psutil.virtual_memory()._asdict()).get("percent")}%\n\n**Bot instance:** {instance}', color=0x55ffff)
        await ctx.send(embed=embed)

    @client.command(aliases=['status'])
    @commands.has_role(584267156385169419)
    async def _status(ctx, *, status: str):
        config.set('main', 'status', str(status))
        write()
        await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await ctx.send(f'Status set to **{status}**')

    @client.command(aliases=['ping'])
    async def _ping(ctx):
        embed = discord.Embed(title=f'Latency', description=f'{round(client.latency * 1000)}ms', color=0x55ffff)
        await ctx.send(embed=embed)

    @client.command(aliases=['restart'])
    @commands.check(Methods.chkLerrific)
    async def _restart(ctx):
        await ctx.send(f'I will come back...')
        os.execl(sys.executable, sys.executable, * sys.argv)

    @client.command(aliases=['stop', 'die', 'kill', 'quit'])
    @commands.check(Methods.chkLerrific)
    async def _stop(ctx):
        await ctx.send(f'{Emoji.hamiltonEyeroll} Just for now...')
        sys.exit()

    @client.command(aliases=['8ball', 'eightball'])
    async def _8ball(ctx, *, question: str):
        answer = eightball_responses.responses(question)

        embed = discord.Embed(title=f'🔮 What is it that troubles you?', description=f'{Emoji.hamiltonConfuse} You ask the question, \"**{question.capitalize()}?**\"\n\n{Emoji.hamiltonWisdom} and I answer... \"**{random.choice(answer)}**\"', color=0x55ffff)
        await ctx.send(embed=embed)

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
        embed = discord.Embed(title=f'Temperature conversion', description=f'{temperature}°C **Celsius to Fahrenheit:** {round(CtoF,2)}°F\n\n{temperature}°F **Fahrenheit to Celsius:** {round(FtoC,2)}°C', color=0x55ffff)
        await ctx.send(embed=embed)

    @client.command(aliases=['urban', 'ud', 'urbandictionary'])
    async def _urban(ctx, *, word: str):
        methods = Methods()
        await methods.searchUrban(ctx=ctx, word=word)

    @client.command(aliases=['define'])
    async def _define(ctx, *, word: str):
        # in all honesty i didn't really bother to try and understand this
        # https://pythonprogramming.net/wordnet-nltk-tutorial/
        syns = wordnet.synsets(word)
        if json.dumps(syns) == '[]':
            await ctx.send(f':x: There is no definition for **{word}**.')
            await ctx.send(f'Searching urban dictionary for a definition...')
            methods = Methods()
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

        embed = discord.Embed(title=f'{word}', description=f'{definition}', color=0x55ffff)
        if examplesList:
            embed.add_field(name=f'Examples', value=f'{examples}', inline=False)
        if synonymsList:
            embed.add_field(name=f'Synonyms', value=f'{synonyms}', inline=False)
        if antonymsList:
            embed.add_field(name=f'Antonyms', value=f'{antonyms}', inline=False)
        await ctx.send(embed=embed)


class Errors():

    @Commands._say.error
    async def _say_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._status.error
    async def _status_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._8ball.error
    async def _8ball_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._zalgo.error
    async def _zalgo_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.']
            await ctx.send(f':x: {random.choice(r)}')

    @Commands._temperature.error
    async def _temperature_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.']
            await ctx.send(f':x: {random.choice(r)}')


token = open(Path("../token.txt")).read()
client.run(token)
