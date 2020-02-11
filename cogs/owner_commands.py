from discord.ext import commands
import discord
from other.utils import *
import bot
import os
import sys


class Owner_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['playing'])
    @commands.check(Utils.owner)
    async def status(self, ctx, *, status: str):
        bot.config.set('main', 'status', str(status))
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await ctx.send(f'Status set to **{status}**')
        bot.write()

    @commands.command(aliases=['ooh', 'oooooh', 'ooooh'])
    @commands.check(Utils.owner)
    async def oooh(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/489965104784474124/676295367343472640/oooooooooooooooooh.jpg')
        await ctx.message.delete()

    @commands.command(aliases=['rs', 're'])
    @commands.check(Utils.owner)
    async def restart(self, ctx):
        await ctx.send(f'I will come back...')
        os.execl(sys.executable, sys.executable, * sys.argv)

    @commands.command(aliases=['die', 'kill', 'quit'])
    @commands.check(Utils.owner)
    async def stop(self, ctx):
        await ctx.send(f'{Emoji.hamiltonEyeroll} Just for now...')
        sys.exit()


def setup(client):
    client.add_cog(Owner_Commands(client))
