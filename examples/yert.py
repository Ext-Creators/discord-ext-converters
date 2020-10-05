from discord.ext.converters import ConvertersBot

cbot = ConvertersBot(command_prefix='!')

class Yert:
    yert = 'yert'

@cbot.converters.register(Yert)
async def convert_yert(ctx, arg):
    return Yert()

@cbot.command()
async def yert(ctx, yert: Yert):
    await ctx.send(yert.yert)

cbot.run('token')
