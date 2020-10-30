import dataclasses
import re

from discord.ext.converters import ConvertersBot
from discord.ext.commands import ConversionError
from discord.utils import get


bot = ConvertersBot(command_prefix='!')
bot.converters.load('range', 'regex')

@dataclasses.dataclass
class GameInfo:
    name: str
    price: float
    description: str

games = [
    GameInfo(name='Cool Game', price=2.99, description='A really cool game with guns'),
    GameInfo(name='Bad Game', price=299.99, description='A game where everything is lame'),
    GameInfo(name='Somewhat OK Game', price=-0.99, description='We give you 99 cents when you buy this game')
]

@bot.converters.register(GameInfo)
async def convert_GameInfo(ctx, arg):
    gi = get(games, name=arg)
    if gi:
        return gi
    else:
        raise Exception('Game Not Found!')

@bot.command()
async def info(ctx, *, game: GameInfo):
    await ctx.send("""```
Name: {0.name}
Price: ${0.price}
Description: {0.description}
```""".format(game))

@info.error
async def handle_info(ctx, err):
    if isinstance(err, ConversionError):
        await ctx.send(str(err.original))

@bot.command()
async def greet(ctx, num: range(1, 4)):
    choice_list = ['', 'Hello!', 'Heya!', "Oh, it's you again."]
    await ctx.send(choice_list[num])

@bot.command()
async def match(ctx, text: re.compile(r"hello\d+")):
    # slight caveat, it uses compile to match, which would return re.Match, not re.Pattern
    await ctx.send('`{}` is a match!'.format(text.group(0)))

bot.run('token')
