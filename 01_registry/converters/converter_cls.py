# converters/converter_cls.py
from .builder import CONVERTERS

# 使用注册器管理模块

@CONVERTERS.register_module()
class Converter1(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


@CONVERTERS.register_module()
class Converter2(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
