import discord
from discord.ext import commands
from other.utils import Utils


class Misc(commands.Cog):

    u = Utils()

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await u.embed(ctx, f'Latency', f'{round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Misc(client))
