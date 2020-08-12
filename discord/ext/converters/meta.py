from ._converters import _ALL


class ConverterMixin:

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)

        for t, c in _ALL.items():
            self.converters[t] = c

        return self
