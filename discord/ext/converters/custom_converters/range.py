from discord.ext import commands


class InRangeConverter(commands.Converter):
    def __init__(self, *args) -> None:
        self.range = range(*args)

    async def convert(self, ctx, argument: str) -> int:
        try:
            value = int(argument)
        except ValueError:
            raise commands.BadArgument("{0} is not int".format(argument))

        if value in self.range:
            return value
        raise commands.BadArgument("{0} not in range".format(argument))
