# converters/converter_func.py
from ..model.builder import CONVERTERS
from .converter_cls import Converter1


@CONVERTERS.register_module()
def converter3(a, b):
    return Converter1(a, b)
