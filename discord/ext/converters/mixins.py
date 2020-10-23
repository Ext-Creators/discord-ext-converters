from discord.ext.commands import Command
from discord.ext.commands.bot import BotBase

from .custom_converters import CONVERTERS


class ConvertersMixin(BotBase):

    def __init__(self, *args, **kwargs):
        self.converters = {type: converter for type, converter in CONVERTERS}
        super().__init__(*args, **kwargs)


_old_actual_conversion = Command._actual_conversion


def _actual_conversion(self, ctx, converter, argument, param):
    if isinstance(ctx.bot, ConvertersMixin):
        converter = ctx.bot.converters.get(converter, converter)
    return _old_actual_conversion(self, ctx, converter, argument, param)


Command._actual_conversion = _actual_conversion
