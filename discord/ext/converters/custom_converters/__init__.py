from typing import Dict, Tuple, Type

from discord.ext import commands


BUILTINS: Tuple[Type, ...] = (
    bool,
    str,
    int,
    float,
)


class _ConverterDict(dict):

    def __setitem__(self, k, v):
        if not issubclass(v, commands.Converter) or v in BUILTINS:
            raise TypeError('Excepted value of type \'Converter\' or built-in, received {}'.format(v.__name__))
        super().__setitem__(k, v)


CONVERTERS: Dict[Type, Type[commands.Converter]] = _ConverterDict()
