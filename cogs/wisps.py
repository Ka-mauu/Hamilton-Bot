import asyncio
import random

import discord
from discord.ext import commands

import bot
from other.utils import Emoji, Utils


class Wisps(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def check_for_wisps(self, ctx):
        if not bot.CFG.has_option('wisps', f'{ctx.message.author.id}.bal'):
            await ctx.send(f':x: You do not have any wisps! Register yourself with `ok.wisps`')
            return False
        else:
            return True

    @commands.command(aliases=['balance', 'bal'])
    async def wisps(self, ctx):
        bot.read()

        if not bot.CFG.has_option('wisps', f'{ctx.message.author.id}.bal'):
            bot.CFG.set('wisps', f'{ctx.message.author.id}.bal', '100')
            bot.write()

        wisps = bot.CFG.getint('wisps', f'{ctx.message.author.id}.bal')

        await Utils.embed(ctx, f'{Emoji.wisp} Deposit', f'**{ctx.message.author.name}** has accumulated **{wisps}** will-o-wisps.')

    @commands.command(aliases=['cointoss'])
    async def coinflip(self, ctx, bet: int, coin: str):
        bot.read()

        if not await self.check_for_wisps(ctx):
            return

        wisps = bot.CFG.getint('wisps', f'{ctx.message.author.id}.bal')

        if bet > wisps:
            await ctx.send(f':x: You cannot bet more wisps than you own! You have {wisps} wisps.')
            return

        hamilton_bet = random.randrange(bet, bet * 1.5)

        def check(message):
            return message.content.lower() == 'ok'

        await Utils.embed(ctx, 'Are you sure you want to do this?', f'Do you wish to sacrifice **{bet}** will-o-wisps for a chance of a greater blessing? Or worse, a chance to lose it?\n\nType **OK** to continue...')
        try:
            await self.client.wait_for('message', check=check, timeout=7)
        except asyncio.TimeoutError:
            await ctx.send(':x: You did not respond in time, cancelling coin flip.')
            return

        if coin.lower() == 'heads':
            response = f'You bet **{bet}** on heads {Emoji.heads}. I bet **{hamilton_bet}** on tails! {Emoji.tails}'
        elif coin.lower() == 'tails':
            response = f'You bet **{bet}** on tails {Emoji.tails}. I bet **{hamilton_bet}** on heads! {Emoji.heads}'
        else:
            await ctx.send(':x: That is not a side of a coin, moron... Choose heads or tails.')
            return

        await Utils.embed(ctx, title=f'Coinflip', description=response)
        await asyncio.sleep(1)
        await ctx.send(embed=discord.Embed(title='Flipping...', color=0x55ffff))
        await asyncio.sleep(2)
        result = random.choice(['heads', 'tails'])
        if result == 'heads' and coin.lower() == 'heads':
            response2 = f'The coin landed on heads {Emoji.heads}, you win... {Emoji.hamiltonDread}\n**+ {hamilton_bet}** wisps was added to your account.'
            wisps += hamilton_bet + bet
            wisps -= bet
        elif result == 'heads' and coin.lower() == 'tails':
            response2 = f'The coin landed on heads {Emoji.heads}, I win! {Emoji.hamiltonCool}\n**- {hamilton_bet + bet}** wisps was taken from your account.'
            wisps -= hamilton_bet + bet
            wisps += bet
        elif result == 'tails' and coin.lower() == 'tails':
            response2 = f'The coin landed on tails {Emoji.tails}, you win... {Emoji.hamiltonDread}\n**+ {hamilton_bet}** wisps was added to your account.'
            wisps += hamilton_bet + bet
            wisps -= bet
        elif result == 'tails' and coin.lower() == 'heads':
            response2 = f'The coin landed on tails {Emoji.tails}, I win! {Emoji.hamiltonCool}\n**- {hamilton_bet + bet}** wisps was taken from your account.'
            wisps -= hamilton_bet + bet
            wisps += bet

        await Utils.embed(ctx, f'Coinflip Result', response2)

        bot.CFG.set('wisps', f'{ctx.message.author.id}.bal', str(wisps))
        bot.write()

    @commands.command(aliases=['chance'])
    async def odds(self, ctx, bet: int, chance: int):
        bot.read()

        if not await self.check_for_wisps(ctx):
            return

        wisps = bot.CFG.getint('wisps', f'{ctx.message.author.id}.bal')

        if bet > wisps:
            await ctx.send(f':x: You cannot bet more wisps than you own! You have {wisps} wisps.')
            return

        await ctx.send('wip')


def setup(client):
    client.add_cog(Wisps(client))
