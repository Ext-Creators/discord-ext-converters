import typing
from discord.ext import commands
import copy


class CustomConverter(commands.Converter):
    _value: typing.Any

    def __class_getitem__(cls, value: typing.Any):
        klass = copy.deepcopy(cls)
        klass._value = value
        return klass
