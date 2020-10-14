from discord.ext import commands


class InRangeConverter(commands.Converter):
    def __init__(self, *args, **kwargs) -> None:
        self.range = range(*args, **kwargs)

    async def convert(self, ctx, argument: str) -> int:
        try:
            argument = int(argument)
        except ValueError:
            raise commands.BadArgument("{0} is not int".format(argument))

        if argument in self.range:
            return argument
        raise commands.BadArgument("{0} not in range".format(argument))
