import random

import discord
import psutil
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

import bot
from other.utils import Emoji, Utils


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *cmd):
        if not cmd:
            img = Image.open("resources\\help.png")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("resources\\UASQUARE.TTF", 29)
            fun = "8ball\nurban\n"
            for c in self.client.get_cog('Fun').get_commands():
                if not c.hidden:
                    fun += f'{c.name}\n'
            draw.text((135, 150), fun, (255, 255, 255), font=font)
            misc = ""
            for c in self.client.get_cog('Misc').get_commands():
                if not c.hidden:
                    misc += f'{c.name}\n'
            draw.text((330, 150), misc, (255, 255, 255), font=font)
            wisps = ""
            for c in self.client.get_cog('Wisps').get_commands():
                if not c.hidden:
                    wisps += f'{c.name}\n'
            draw.text((525, 150), wisps, (255, 255, 255), font=font)
            img.save('resources\\help_.png')

            await ctx.send(file=discord.File('resources\\help_.png'))
        else:
            for cogs in self.client.cogs:
                for command in self.client.get_cog(cogs).get_commands():
                    if not command.hidden and (command.name == cmd[0] or cmd[0] in command.aliases):
                        help_str = command.help
                        if help_str == 'None':
                            await ctx.send(f'`ok.{self.get_command_signature(command=command)}`')
                        else:
                            await ctx.send(f'*{command.help}*\n`ok.{self.get_command_signature(command=command)}`')

    def get_command_signature(self, command):
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = '|'.join(command.aliases)
            fmt = '[%s|%s]' % (command.name, aliases)
            if parent:
                fmt = parent + ' ' + fmt
            alias = fmt
        else:
            alias = command.name if not parent else parent + ' ' + command.name

        return '%s %s' % (alias, command.signature)

    @commands.command(aliases=['information', 'botinfo'], help='Gives some information about the bot.')
    async def info(self, ctx):
        await Utils.embed(ctx, f'{Emoji.hamiltonGem} Info', f'*You want me to tell you about myself? Well of course. I am Hamilton, your almighty god. Any questions? No? OK.*\n\n**Status:** What the hell are you saying? I am up and running. Perfectly healthy... What about you? You are nothing but a frail clump of mortal flesh. The only way to completely redeem your pathetic existence is to serve me!\n\n**How much cheese I own:** In my home dimension, I have cut all cheese trade throughout the entire universe, practically making the mice population there extinct. I own only {random.randrange(1337)} cheese wheels in this realm though.\n\n**Favorite number:** It is eight.\n\n**Favorite colour:** Do you really have to ask? What do you think, ORANGE? It\'s baby blue obviously.\n\n**My colour palette (in hex):** [123456 - Fur / Pupils] [55ffff - Gem] [fad420 - Eyes] [ff55aa - Mouth]\n\n**Owner:** I belong to no one. Although I have a particular affinity for lerrific#6574.\n\n**Bot creation date:** 10:00 AM 01-Feb-20\n\n**Total system CPU usage:** {psutil.cpu_percent()}%\n\n**Total system memory usage:** {dict(psutil.virtual_memory()._asdict()).get("percent")}%\n\n**Bot instance:** {bot.INSTANCE}')

    @commands.command(aliases=['latency'], help='Gets bot response time.')
    async def ping(self, ctx):
        await Utils.embed(ctx, f'Latency', f'{round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Misc(client))
