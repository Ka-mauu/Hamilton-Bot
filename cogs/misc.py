from discord.ext import commands
import discord
from other.utils import Utils
from other.utils import Emoji
import random
import psutil
import bot


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['information', 'botinfo'])
    async def info(self, ctx):
        await Utils.embed(ctx, f'{Emoji.hamiltonGem} Info', f'*You want me to tell you about myself? Well of course. I am Hamilton, your almighty god. Any questions? No? OK.*\n\n**Status:** What the hell are you saying? I am up and running. Perfectly healthy... What about you? You are nothing but a frail clump of mortal flesh. The only way to completely redeem your pathetic existence is to serve me!\n\n**How much cheese I own:** In my home dimension, I have cut all cheese trade throughout the entire universe, practically making the mice population there extinct. I own only {random.randrange(1337)} cheese wheels in this realm though.\n\n**Favorite number:** It is eight.\n\n**Favorite colour:** Do you really have to ask? What do you think, ORANGE? It\'s baby blue obviously.\n\n**My colour palette (in hex):** [123456 - Fur / Pupils] [55ffff - Gem] [fad420 - Eyes] [ff55aa - Mouth]\n\n**Owner:** I belong to no one. Although I have a particular affinity for lerrific#6574.\n\n**Bot creation date:** 10:00 AM 01-Feb-20\n\n**Total system CPU usage:** {psutil.cpu_percent()}%\n\n**Total system memory usage:** {dict(psutil.virtual_memory()._asdict()).get("percent")}%\n\n**Bot instance:** {bot.instance}')

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await Utils.embed(ctx, f'Latency', f'{round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Misc(client))
