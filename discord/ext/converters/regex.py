import re
from typing import Optional

from discord.ext import commands


class MatchConverter(commands.Converter):
    def __init__(self, pattern, flags) -> None:
        self.pattern = pattern
        self.flags = flags

    async def convert(self, ctx, argument: str) -> re.Match:
        match: Optional[re.Match] = re.fullmatch(
            self.pattern, argument, flags=self.flags
        )
        if match:
            raise commands.BadArgument(
                "{0} does not match in the regex pattern ({1})".format(
                    argument, self.pattern
                )
            )
        return match
