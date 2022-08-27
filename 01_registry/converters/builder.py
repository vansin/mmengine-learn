# model/builder.py
from mmengine import Registry
# 创建转换器的注册器
CONVERTERS = Registry('converter')



# 创建一个构建方法
def build_converter(cfg, registry, *args, **kwargs):
    cfg_ = cfg.copy()
    converter_type = cfg_.pop('type')
    if converter_type not in registry:
        raise KeyError(f'Unrecognized converter type {converter_type}')
    else:
        converter_cls = registry.get(converter_type)

    converter = converter_cls(*args, **kwargs, **cfg_)
    return converter


# 创建一个用于转换器的注册器，并将 `build_converter` 传递给 `build_func` 参数
CONVERTERS_CUSTOM = Registry('converter', build_func=build_converter)
