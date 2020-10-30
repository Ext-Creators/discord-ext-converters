import inspect
import typing
import importlib

import discord
from discord.ext.commands import converter, Context
from .converter import CustomConverter


BASE_CONVERTERS = {
    discord.CategoryChannel: converter.CategoryChannelConverter,
    discord.Colour:          converter.ColourConverter,
    discord.Emoji:           converter.EmojiConverter,
    discord.Game:            converter.GameConverter,
    discord.Invite:          converter.InviteConverter,
    discord.Member:          converter.MemberConverter,
    discord.Message:         converter.MessageConverter,
    discord.PartialEmoji:    converter.PartialEmojiConverter,
    discord.Role:            converter.RoleConverter,
    discord.TextChannel:     converter.TextChannelConverter,
    discord.User:            converter.UserConverter,
    discord.VoiceChannel:    converter.VoiceChannelConverter,
}


class ConverterDict(dict):
    def __init__(self):
        super().__init__(BASE_CONVERTERS)
    
    def __setitem__(self, k: typing.Any, v: typing.Any):
        if not (issubclass(v, converter.Converter) or inspect.isbuiltin(v)):
            raise TypeError("Excepted value of type 'Converter' or built-in, received {}".format(v.__name__))
        super().__setitem__(k, v)
    
    def set(self, _type: typing.Any, converter: str) -> 'ConverterDict':
        self.__setitem__(_type, converter)
        return self
    
    def get(self, _type: typing.Any, default: typing.Any = None) -> 'ConverterDict':
        if inspect.isclass(_type):
            return super().get(_type, default)
        else:
            _converter = super().get(type(_type), default)

            if issubclass(_converter, CustomConverter):
                _converter = _converter[_type]
            
            return _converter
    
    def register(self, _type: type) -> converter.Converter:
        def predicate(handler: typing.Union[typing.Callable[[Context, str], typing.Awaitable[typing.Any]], converter.Converter]):
            # _type is what is should convert to.

            _converter = handler

            if inspect.iscoroutinefunction(handler):
                _converter = type(
                        '{}Converter'.format(_type.__name__),
                        (converter.Converter,),
                        {
                            'convert': lambda s, c, a: handler(c, a) # should mean it's a coroutine.
                        }
                    )
                
                self.set(_type, _converter)
            else:
                self.set(_type, _converter)
            
            return _converter
        return predicate

    def load(self, *_converters: str):
        for c in _converters:
            importlib.import_module('discord.ext.converters.custom_converters.{}'.format(c)).setup(self)
