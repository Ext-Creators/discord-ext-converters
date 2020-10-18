import re
from typing import Optional

from discord.ext import commands


class MatchConverter(commands.Converter):
    def __init__(self, pattern, flags) -> None:
        self.pattern = pattern
        self.flags = flags

    async def convert(self, ctx, argument: str) -> re.Match:
        match: Optional[re.Match] = re.fullmatch(self.pattern, argument, self.flags)
        if match is None:
            raise commands.BadArgument(
                "{0} does not match the provided pattern".format(argument)
            )
        return match
