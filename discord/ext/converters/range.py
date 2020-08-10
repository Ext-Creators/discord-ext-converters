from typing import Union, Tuple

from discord.ext import commands


class InRangeConverter(commands.Converter):
    def __init__(self, *, range_tuple: Tuple) -> None:
        self.range = range(*range_tuple)

    async def convert(self, ctx, argument: str) -> str:
        if argument in self.range:
            return argument
        raise commands.BadArgument("{argument} not in range".format(argument=argument))
