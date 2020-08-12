from typing import Any, Dict, Type
from discord.ext.commands.converter import Converter

_ALL: Dict[Type[Any], Type[Converter]] = {
    # This will be populated by loaded converters at runtime
}
