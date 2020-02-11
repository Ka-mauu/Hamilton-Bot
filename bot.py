import os
from configparser import ConfigParser
from pathlib import Path

import discord
from discord.ext import commands

# prefixes - for some reason the prefixes with spaces have to be first in the list.. /shrug
BOT = commands.Bot(command_prefix=['ok. ', 'Ok. ', 'oK. ', 'OK. ', 'ok! ', 'Ok! ', 'oK! ', 'OK! ', 'ok.', 'Ok.', 'oK.', 'OK.', 'ok!', 'Ok!', 'oK!', 'OK!'])

CFG = ConfigParser()
DATAF = 'data.ini'
CFG.read(DATAF)

INSTANCE = CFG.getint('main', 'instance')
STATUS = CFG.get('main', 'status')

INSTANCE += 1  # increase instance integer by 1 on launch

CFG.set('main', 'instance', str(INSTANCE))


def write():  # after setting a value you need to call write()
    with open(DATAF, 'w+') as configfile:
        CFG.write(configfile)


def read():  # before reading a value you need to call read()
    CFG.read(DATAF)


write()


@BOT.command()
async def load(ctx, extension):
    BOT.load_extension(f'cogs.{extension}')
    await ctx.send('Loaded {extension}')


@BOT.command()
async def unload(ctx, extension):
    BOT.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        BOT.load_extension(f'cogs.{filename[:-3]}')


@BOT.event
async def on_ready():
    print('\nOnline!\n')
    # update status
    await BOT.change_presence(status=discord.Status.online, activity=discord.Game(STATUS))
    await BOT.get_channel(672942729864413184).send(f'<:okHamiltonOwO:630553287111737354> I have awakened! Serve me and I shall return the favour.')


BOT.run(open(Path("../token.txt")).read())
