try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

from difflib import get_close_matches

from discord.ext.commands import BadArgument, Context, Converter

from ._converters import _ALL


class _ZoneInfoConverter(Converter):

    async def convert(self, ctx: Context, argument: str) -> zoneinfo.ZoneInfo:
        try:
            result = zoneinfo.ZoneInfo(argument)
        except zoneinfo.ZoneInfoNotFoundError:
            try:
                timezone = get_close_matches(argument, zoneinfo.available_timezones(), n=1, cutoff=0.5)[0]
            except IndexError:
                raise BadArgument('Could not find timezone with name {}'.format(argument))

            result = zoneinfo.ZoneInfo(timezone)
        return result


_ALL[zoneinfo.ZoneInfo] = _ZoneInfoConverter
