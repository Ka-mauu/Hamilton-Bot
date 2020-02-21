import random
import sys
import traceback

from discord.ext import commands

from other.utils import Emoji, Utils


class Error_Handling(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            reply = ['That is not a proper command..', 'I cannot perform a non-existent request.', 'Are you going to give me something to do, or what?', 'I cannot just sit here idly, what do you want me to do?']
            await ctx.send(f':x: {random.choice(reply)}')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send(f':x: You do not have the permissions to perform this command!')
        elif isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
            cmd = ctx.command.name.lower()
            if cmd == "say":
                reply = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.say [text]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "zalgo":
                reply = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.zalgo [text]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "status":
                reply = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.status [text]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "define":
                reply = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.define [word]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "urban":
                reply = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.urban [word]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "temperature":
                reply = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.temperature [number]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "eightball":
                reply = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.', f'Are you too {random.choice(Utils.synonymsStupid)} to get this? `ok.8ball [yes/no question]`']
                await ctx.send(f':x: {random.choice(reply)}')
            if cmd == "coinflip":
                reply = [f'You need to specify an amount of wisps you\'re willing to bet, then choose heads {Emoji.heads} or tails {Emoji.tails}. The usage goes as follows; `ok.coinflip [amount] [heads/tails]`']
                await ctx.send(f':x: {random.choice(reply)}')
        else:
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            await ctx.send(f'Something went very wrong, let us laugh at Lerrific\'s incompetence... ```{type(error), error, error.__traceback__}```'.format(file=sys.stderr))


def setup(client):
    client.add_cog(Error_Handling(client))
