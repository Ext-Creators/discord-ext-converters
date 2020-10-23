from discord.ext.commands.bot import BotBase

from .custom_converters import CONVERTERS


class ConvertersMixin(BotBase):

    def __init__(self, *args, **kwargs):
        self.converters = {type: converter for type, converter in CONVERTERS}

        super().__init__(*args, **kwargs)

    async def _actual_conversion(self, ctx, converter, argument, param):
        converter = self.converters.get(converter, converter)
        return await super()._actual_conversion(ctx, converter, argument, param)
