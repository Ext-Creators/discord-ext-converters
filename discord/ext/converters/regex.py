import re
from typing import Union

from discord.ext import commands


class MatchConverter(commands.Converter):
    def __init__(self, *, pattern: str, exception: str = "No match found.") -> None:
        self.pattern = pattern
        self.exception = exception

    async def convert(self, ctx, argument: str) -> str:
        match: Union[re.Match, None] = re.match(self.pattern, argument)
        if match is None:
            raise commands.BadArgument(self.exception)
        return argument
