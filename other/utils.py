import discord

COLOR = 0x55ffff


class Emoji():
    hamiltonConfuse = '<:okHamiltonThink:681792103311081497>'
    hamiltonWoke = '<:okHamiltonOwO2:679522022488801310>'
    hamiltonDread = '<:okHamiltonDread:630553286986039356>'
    hamiltonOWO = '<:okHamiltonOwO:679147317751709696>'
    hamiltonEyeroll = '<:okHamiltonEyeroll:679511451123449889>'
    hamiltonWisdom = '<:okHamiltonWisdom:681043734280011788>'
    hamiltonGem = '<:okBlueFluorite:669100365311901698>'
    hamiltonCool = '<:okHamiltonCool:681393198156873738>'
    hamiltonSleep = '<:okHamiltonSleep:636473614815723530>'
    heads = '<:okHeads:676292505427247104>'
    tails = '<:okTails:676292506832601099>'
    wisp = '<:okWilloWisp:676253396545568770>'


class Utils():

    synonymsStupid = ['stupid', 'dense', 'thick', 'simple', 'dull', 'blockheaded', 'numskulled', 'dimwitted', 'full of shit']

    def owner(ctx):
        return ctx.author.id == 259536485340938242

    async def embed(ctx, title: str, description: str):
        await ctx.send(embed=discord.Embed(title=title, description=description, color=COLOR))
