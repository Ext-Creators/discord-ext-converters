from uuid import UUID
from discord.ext.commands import BadArgument, Context, Converter

from ._converters import _ALL


class _UUIDConverter(Converter):

    async def convert(self, ctx: Context, argument: str) -> UUID:

        try:
            value = UUID(argument)
        except ValueError:
            raise BadArgument('{} is not a valid UUID'.format(argument))

        return value


_ALL[UUID] = _UUIDConverter
