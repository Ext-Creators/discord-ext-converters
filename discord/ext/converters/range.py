from typing import Tuple

from discord.ext import commands


class InRangeConverter(commands.Converter):
    def __init__(self, *args, **kwargs) -> None:
        self.range = range(*args, **kwargs)

    async def convert(self, ctx, argument: str) -> int:
        if argument.isnumeric() and int(argument) in self.range:
            return int(argument)
        raise commands.BadArgument("{0} not in range".format(argument))
