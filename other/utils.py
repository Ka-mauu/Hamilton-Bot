import discord
import random


class Emoji():
    hamiltonConfuse = '<:okHamiltonConfuse:630553287145422871>'
    hamiltonWoke = '<:okHamiltonWoke:630553285488803850>'
    hamiltonDread = '<:okHamiltonDread:630553286986039356>'
    hamiltonOWO = '<:okHamiltonOwO:630553287111737354>'
    hamiltonEyeroll = '<:okHamiltonEyeroll:630553283890642974>'
    hamiltonWisdom = '<:okHamiltonWisdom:636473613238665227>'
    hamiltonGem = '<:okHamiltonGem:669100365311901698>'
    hamiltonCool = '<:okHamiltonCool:635747888672145408>'
    heads = '<:okHeads:676292505427247104>'
    tails = '<:okTails:676292506832601099>'
    wisp = '<:okWilloWisp:676253396545568770>'


class Utils():

    async def embed(self, ctx, title: str, description: str):
        await ctx.send(embed=discord.Embed(title=title, description=description, color=color))
