import os
import sys

import discord
from discord.ext import commands

import bot
from other.utils import Emoji, Utils


class OwnerCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(Utils.owner)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'**Unloaded {extension}**')

    @commands.command()
    @commands.check(Utils.owner)
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f'**Loaded {extension}**')

    @commands.command(aliases=['rl'])
    @commands.check(Utils.owner)
    async def reload(self, ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.client.unload_extension(f'cogs.{filename[:-3]}')
                self.client.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send(f'**Reloaded all cogs!**')

    @commands.command(aliases=['playing'])
    @commands.check(Utils.owner)
    async def status(self, ctx, *, status: str):
        bot.CFG.set('main', 'status', str(status))
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
    client.add_cog(OwnerCommands(client))
