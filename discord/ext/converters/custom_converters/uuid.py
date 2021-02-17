from uuid import UUID

from discord.ext import commands

from . import CONVERTERS


class UUIDConverter(commands.Converter):

    async def convert(self, ctx, argument: str) -> UUID:
        try:
            value = UUID(argument)
        except ValueError:
            raise commands.BadArgument("{0} is not a valid UUID".format(argument))

        return value


CONVERTERS[UUID] = UUIDConverter
