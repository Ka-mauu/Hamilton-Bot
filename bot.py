import discord
import random
import sys
import os
import psutil
import pprint
import requests
import json
import nltk
from nltk.corpus import wordnet
from urbandict import urbandict
from configparser import ConfigParser
from enum import Enum
from discord.ext import commands
from zalgo_text import zalgo

# prefix(es)
client = commands.Bot(command_prefix = ['ok. ', 'ok.'])

#config

config = ConfigParser()
config.read('data.ini')

instance = config.getint('main', 'instance')
status = config.get('main', 'status')

# increase instance integer by 1 on launch
instance += 1

config.set('main', 'instance', str(instance))

def write():
    with open('data.ini', 'w+') as configfile:
      config.write(configfile)

write()

#config end

# for easy access
class Emoji():
    hamiltonConfuse = '<:okHamiltonConfuse:630553287145422871>'
    hamiltonWoke =    '<:okHamiltonWoke:630553285488803850>'
    hamiltonDread =   '<:okHamiltonDread:630553286986039356>'
    hamiltonOWO =     '<:okHamiltonOwO:630553287111737354>'
    hamiltonEyeroll = '<:okHamiltonEyeroll:630553283890642974>'
    hamiltonWisdom =  '<:okHamiltonWisdom:636473613238665227>'
    hamiltonGem =     '<:okHamiltonGem:669100365311901698>'

@client.event
async def on_ready():
    print('Hello!')
    # update status
    await client.change_presence(status=discord.Status.online, activity= discord.Game(status))
    await client.get_channel(672942729864413184).send(f'<:okHamiltonOwO:630553287111737354> I am online!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        r = ['That is not a proper command..', 'I cannot perform a non-existent command.',  'Are you going to give me a command?']
        await ctx.send(random.choice(r))


@client.command(aliases=['info'])
async def _info(ctx):
    embed = discord.Embed(title=f'{Emoji.hamiltonGem} Info', description=f'*You want me to tell you about myself? Well of course. I am Hamilton, your almighty god. Any questions? No? OK.*\n\n**Status:** What the hell are you saying? I am up and running. Perfectly healthy... What about you? You are nothing but a frail clump of mortal flesh. The only way to completely redeem your pathetic existence is to serve me!\n\n**How much cheese I own:** In my home dimension, I have cut all cheese trade throughout the entire universe, practically making the mice population there extinct. I own only {random.randrange(1337)} cheese wheels in this realm though.\n\n**Favorite number:** It is eight.\n\n**Favorite colour:** Do you really have to ask? What do you think, ORANGE? It\'s baby blue obviously.\n\n**My colour palette (in hex):** [123456 - Fur / Pupils] [55ffff - Gem] [fad420 - Eyes] [ff55aa - Mouth]\n\n**Owner:** I belong to no one. Although I have a particular affinity for lerrific#6574.\n\n**Bot creation date:** 10:00 AM 01-Feb-20\n\n**System CPU usage:** {psutil.cpu_percent()}%\n\n**System memory usage:** {dict(psutil.virtual_memory()._asdict()).get("percent")}%\n\n**Bot instance:** {instance}', color=0x55ffff)
    await ctx.send(embed=embed)

@client.command(aliases=['status'])
async def _status(ctx, *, status:str):
    config.set('main', 'status', str(status))
    write()

    await client.change_presence(status=discord.Status.online, activity= discord.Game(status))
    await ctx.send(f'Status set to **{status}**')

@_status.error
async def _status_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.']
        await ctx.send(random.choice(r))

@client.command(aliases=['ping'])
async def _ping(ctx):
    embed = discord.Embed(title=f'Latency', description=f'{round(client.latency * 1000)}ms', color=0x55ffff)
    await ctx.send(embed=embed)

@client.command(aliases=['restart'])
async def _restart(ctx):
    # ghetto restart, can probably improve this
    await ctx.send(f'Restarting...')
    os.startfile('C:\\Users\\WT\\Downloads\\misc\\programming\\projects\\_DiscordHamiltonBot\\Hamilton-Bot\\bot.py')
    sys.exit()

@client.command(aliases=['stop','die','kill','quit'])
async def _stop(ctx):
    await ctx.send(f'{Emoji.hamiltonEyeroll} Just for now..')
    sys.exit()

@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question:str):
    answer = ['Ok, please ask me a real question. I will not be answering otherwise.', 'Ok, do not waste my precious time with your gibberish.', 'Ok, you are absolutely unfunny.', 'Ok, I am a bit iffy on these types of questions. I will therefore not be answering them.']

    if question.lower().startswith('should') or question.lower().startswith('can'):
        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, I cannot answer that at the moment...', 'Ok, yeah. That sounds good.', 'Ok, no. I really do pity you.', 'Ok, but venture only if you dare...', 'Ok, but do not come crying to me when you inevitably regret it.', 'Ok, I cannot believe how unfathomably dense you are. Goodbye.', 'Ok. That is a batshit crazy notion, but I am all for it.', 'Ok, but why are you asking me this?', 'Ok, I honestly could not care less about what you want to do.']
    if question.lower().startswith('am'):
        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, I cannot answer that at the moment...', 'Ok, you definitely show the symptoms, so yes.', 'Ok. you do not show the symptoms, fortunately.', 'Ok, the universe has decided so.']
    if question.lower().startswith('is') or question.lower().startswith('does') or question.lower().startswith('do i') or question.lower().startswith('do we'):
        answer = ['Ok, I cannot answer that at the moment...', 'Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, it is decidedly so.', 'Ok, I can say yes without a doubt.', 'Ok, I can say no without a doubt.', 'Ok... Well, no, unfortunately.', 'Ok... Well, yes, unfortunately.', 'Ok, I raise you a better question... Are you stupid?', 'Ok, the universe has decided so.']
    if question.lower().startswith('if') or question.lower().startswith('will') or question.lower().startswith('would') or question.lower().startswith('could') or question.lower().startswith('shall'):
        answer = ['Ok, I have no opinion on any of your trivial questions. Next!', 'Ok, no. I really do pity you.', 'Ok, I cannot answer that at the moment...', 'Ok, as I see it, you will. Just be cautious.', 'Ok, with all things considered, yes.', 'Ok, I cannot be certain, but I wish you luck.', 'Ok. Fortunately, no.',  'Ok, I do not think I can answer this for you.', 'Ok, I do not think you ever will, and it is not wise to try.', 'Ok, you are better off not doing that. I would like to see you try, though.', 'Ok, the universe has decided so.']

    if question.lower().startswith('are you ok') or question.lower().startswith('r u ok') or question.lower().startswith('are u ok') or question.lower().startswith('r you ok') or question.lower().startswith('are you okay'):
        answer = ['I am very OK!']
    if question.lower().startswith('am i ok') or question.lower().startswith('am i okay'):
        answer = ['You are very OK!']

    embed = discord.Embed(title=f'🔮 8ball', description=f'{Emoji.hamiltonConfuse} You ask the question, \"**{question.capitalize()}?**\"\n\n{Emoji.hamiltonWisdom} and I answer... \"**{random.choice(answer)}**\"', color=0x55ffff)
    await ctx.send(embed=embed)

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = ['Are you going to ask me a question or what?', 'What is it? I am waiting...',  'Ask me a real question, dimwit.', 'That is not a proper question...']
        await ctx.send(random.choice(r))

@client.command(aliases=['zalgo', 'cursed'])
async def _zalgo(ctx, *, text:str):
    await ctx.send(zalgo.zalgo().zalgofy(text))
    await ctx.message.delete()

@_zalgo.error
async def _zalgo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = ['What am I going to say? I cannot just say nothing.', 'Give me something to say. Do you have anything?']
        await ctx.send(random.choice(r))

@client.command(aliases=['say', 'echo', 'speak'])
async def _say(ctx, *, text:str):
    await ctx.send(text)
    await ctx.message.delete()

@_say.error
async def _say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = ['What am I going to say? I cannot just say nothing.', 'Give me something to say. Do you have anything?']
        await ctx.send(random.choice(r))

@client.command(aliases=['temperature','temp'])
async def _temperature(ctx, *, temperature:float):
    CtoF = (temperature * 9 / 5) + 32
    FtoC = (temperature - 32) * 5 / 9
    embed = discord.Embed(title=f'Temperature conversion', description=f'**Celsius to Fahrenheit:** {round(CtoF,2)}°F\n\n**Fahrenheit to Celsius:** {round(FtoC,2)}°C', color=0x55ffff)
    await ctx.send(embed=embed)

@_temperature.error
async def _temperature_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        r = ['I cannot calculate a number that does not exist..', 'Give me something to calculate.']
        await ctx.send(random.choice(r))

@client.command(aliases=['urban','ud','urbandictionary'])
async def _urban(ctx, *, word:str):
    # get the list inside of a list
    urb = urbandict(word).get('list')
    # make it a string so we can modify it
    tostring = json.dumps(urb)
    if tostring.endswith(']'):
        tostring = tostring[1:-1]
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

@client.command(aliases=['define'])
async def _define(ctx, *, word:str):
    # in all honesty i didn't really bother to try and understand this
    # https://pythonprogramming.net/wordnet-nltk-tutorial/
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
        embed.add_field(name=f'Examples', value=f'{examples}', inline=False)
    if synonymsList:
        embed.add_field(name=f'Synonyms', value=f'{synonyms}', inline=False)
    if antonymsList:
        embed.add_field(name=f'Antonyms', value=f'{antonyms}', inline=False)
    await ctx.send(embed=embed)


client.run('NjcyOTM1OTgwMjM1MjI3MTM3.XjSvGA.5VFQG3hV4CxiX_2_tPeio7YVvqA')
