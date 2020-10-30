from discord.ext.converters import ConvertersBot

bot = ConvertersBot(command_prefix='!')

class Yert:
    yert = 'yert'

@bot.converters.register(Yert)
async def convert_Yert(ctx, arg):
    return Yert()

@bot.command()
async def yert(ctx, yert: Yert):
    await ctx.send(yert.yert)

bot.run('token')
