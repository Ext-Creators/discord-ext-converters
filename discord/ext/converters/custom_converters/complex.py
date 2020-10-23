from discord.ext import commands


class ComplexConverter(commands.Converter):

    async def convert(self, ctx, argument: str) -> complex:
        try:
            value = complex(argument.lower().replace('i', 'j'))
        except ValueError:
            raise commands.BadArgument("{0} is not a complex number".format(argument))

        return value

