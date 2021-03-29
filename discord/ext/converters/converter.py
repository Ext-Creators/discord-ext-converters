import typing
from discord.ext import commands
import copy
import sys

if sys.version_info >= (3, 7):
    class CustomConverter(commands.Converter):
        _value: typing.Any

        def __class_getitem__(cls, value: typing.Any) -> 'CustomConverter':
            klass = copy.deepcopy(cls)
            klass._value = value
            return klass
else:
    class CustomConveterMeta(type):
        def __getitem__(cls, value: typing.Any) -> 'CustomConverter':
            klass = copy.deepcopy(cls)
            klass._value = value
            return klass
        
    class CustomConverter(commands.Converter, metaclass=CustomConveterMeta):
        _value: typing.Any
