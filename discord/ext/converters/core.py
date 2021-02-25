from typing import Any, Callable, Optional, Type, TypeVar, Union

import copy

from discord.ext.commands import GroupMixin, Command

from .model import ConverterDict

__all__ = (
    'ConvertersCommand',
    'ConvertersGroupMixin',
    'ConvertersGroup',
    'command',
    'group',
)


_CCT = TypeVar('_CCT', bound='ConvertersCommand')
_CGT = TypeVar('_CGT', bound='ConvertersGroup')


class ConvertersCommand(Command):
    converters: ConverterDict

    async def _actual_conversion(self, ctx, converter, argument, param):
        converter = self.converters.get(converter, converter)
        return await super()._actual_conversion(ctx, converter, argument, param)


class ConvertersGroupMixin(GroupMixin):
    converters = ConverterDict()

    # redefine GroupMixin#command and GroupMixin#group to work with redefined decorators
    def command(self, *args, **kwargs) -> Callable[..., _CCT]:
        def decorator(func: Callable[..., Any]) -> _CCT:
            kwargs.setdefault('parent', self)
            result = command(*args, **kwargs)(func)
            result.converters = copy.copy(self.converters)
            self.add_command(result)
            return result
        
        return decorator
    
    def group(self, *args, **kwargs) -> Callable[..., _CCT]:
        def decorator(func: Callable[..., Any]) -> _CCT:
            kwargs.setdefault('parent', self)
            result = group(*args, **kwargs)(func)
            result.converters.update(copy.copy(self.converters))
            self.add_command(result)
            return result

        return decorator


class ConvertersGroup(ConvertersGroupMixin, ConvertersCommand):
    ...


def command(name: Optional[str] = None, cls: Type[_CCT] = ConvertersCommand, **attrs: Any) -> Callable[..., _CCT]:
    """A decorator that transforms a function into a :class:`.ConvertersCommand`.

    """

    def decorator(func: Callable[..., Any]) -> _CCT:
        if isinstance(func, ConvertersCommand):
            raise TypeError('Callback is already a command.')
        return cls(func, name=name, **attrs)

    return decorator


def group(name: Optional[str] = None, cls: Type[_CGT] = ConvertersGroup, **attrs: Any) -> Callable[..., _CGT]:
    """A decorator that transforms a function into a :class:`.ConvertersGroup`.

    This is similar to the :func:`.command` decorator but the ``cls``
    parameter is set to :class:`.ConvertersGroup` by default.

    .. versionchanged:: 1.1
        The ``cls`` parameter can now be passed.
    """

    return command(name=name, cls=cls, **attrs)
