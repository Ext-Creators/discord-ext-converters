from typing import Any, Type, TypeVar

import copy

from discord.ext import commands


_CCT = TypeVar('_CCT', bound='CustomConverter')


class CustomConverter(commands.Converter):
    _value: Any

    def __class_getitem__(cls: Type[_CCT], value: Any) -> _CCT:
        cls = copy.deepcopy(cls)
        cls._value = value
        return cls
