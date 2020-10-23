from yarl import URL

from discord.ext import commands


class URLConverter(commands.Converter):

    def __init__(self, require_scheme: bool = True):
        self.require_scheme = require_scheme

    async def convert(self, ctx, argument: str) -> URL:
        value = URL(argument)
        if not value.host or (self.require_scheme and not value.scheme):
            raise commands.BadArgument("{0} is not a valid URL".format(argument))

        return value

