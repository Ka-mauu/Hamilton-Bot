import discord
import random
import bot


class Errors():

    commands = bot.Commands()

    @commands._say.error
    async def _say_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.say [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._status.error
    async def _status_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to set a status or what?', 'A status cannot contain nothing, bonehead.',  'Try setting my status to something that is not nothing.', 'That is not a proper status, dolt.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.status [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._8ball.error
    async def _8ball_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['Are you going to ask me a question or what?', 'What is it that you want to ask? I am waiting...',  'Ask me a question, dimwit.', 'Will you ask me a question, or no? Make up your mind.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.8ball [yes/no question]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._zalgo.error
    async def _zalgo_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['What do you need me to say? It cannot be nothing.', 'Give me something to say.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.zalgo [text]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._temperature.error
    async def _temperature_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot calculate a number that does not exist...', 'Give me something to calculate.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.temperature [number]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._define.error
    async def _define_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.define [word]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Commands._urban.error
    async def _urban_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = ['I cannot search for something that does not exist...', 'Give me something to search for.', f'Are you too {random.choice(synonymsStupid)} to get this? `ok.urban [word]`']
            await ctx.send(f':x: {random.choice(r)}')

    @bot.Points._coinflip.error
    async def _coinflip_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            r = [f'You need to specify an amount of wisps you\'re willing to bet, then choose heads {Emoji.heads} or tails {Emoji.tails}. The usage goes as follows; `ok.coinflip [amount] [heads/tails]`']
            await ctx.send(f':x: {random.choice(r)}')
