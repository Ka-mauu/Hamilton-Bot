import discord
import random
import sys
import os
import psutil
import requests
import datetime
from other.utils import *
from discord.ext import commands
from pathlib import Path
from configparser import ConfigParser

# prefixes - for some reason the prefixes with spaces have to be first in the list.. /shrug
client = commands.Bot(command_prefix=['ok. ', 'Ok. ', 'oK. ', 'OK. ', 'ok! ', 'Ok! ', 'oK! ', 'OK! ', 'ok.', 'Ok.', 'oK.', 'OK.', 'ok!', 'Ok!', 'oK!', 'OK!'])

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


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Loaded {extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print('\nOnline!\n')
    # update status
    await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
    await client.get_channel(672942729864413184).send(f'<:okHamiltonOwO:630553287111737354> I have awakened! Serve me and I shall return the favour.')


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


client.run(open(Path("../token.txt")).read())
