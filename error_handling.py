"""import discord
from discord.ext import commands
import datetime
from other.utils import *
import random
import bot
from cogs.owner_commands import *
from cogs.fun import *
from cogs.eightball import *
from cogs.misc import *
from cogs.urbandict import *


class Error_Handling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            r = ['That is not a proper command..', 'I cannot perform a non-existent request.', 'Are you going to give me something to do, or what?', 'I cannot just sit here idly, what do you want me to do?']
            await ctx.send(f':x: {random.choice(r)}')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f':x: You do not have the permissions to perform this command!')
        elif isinstance(error, commands.MissingRequiredArgument):
            pass
        else:
            print(f'Something went wrong. Error: \n{error, type(error)}\nTime of error: {datetime.datetime.now()}')
            await ctx.send(f'Something went very wrong, let us laugh at Lerrific\'s incompetence... ```{error, type(error)}```')

    @Fun.say.error
    async def _say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.say [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Owner_Commands.status.error
    async def _status_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.status [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Eightball.eightball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.8ball [yes/no question]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Fun.zalgo.error
    async def _zalgo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.zalgo [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Fun.temperature.error
    async def _temperature_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.temperature [number]`']
            await ctx.send(f':x: {random.choice(r)}')

    @Fun.define.error
    async def _define_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.define [word]`']
            await ctx.send(f':x: {random.choice(r)}')

    @UrbanDict.urban.error
    async def _urban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.urban [word]`']
            await ctx.send(f':x: {random.choice(r)}')


def setup(client):
    client.add_cog(Error_Handling(client))
"""
