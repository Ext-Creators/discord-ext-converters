try:
    import zoneinfo
except ImportError:
    try:
        from backports import zoneinfo
    except ImportError:
        raise RuntimeError('Could not import zoneinfo module.')

from discord.ext import commands

from . import CONVERTERS


class ZoneInfoConverter(commands.Converter):

    async def convert(self, ctx, argument: str) -> zoneinfo.ZoneInfo:
        try:
            value = zoneinfo.ZoneInfo(argument)
        except (ValueError, zoneinfo.ZoneInfoNotFoundError):
            raise commands.BadArgument("{0} is not a valid IANA time zone".format(argument))

        return value


CONVERTERS[zoneinfo.ZoneInfo] = ZoneInfoConverter
