# import converters

# from  import CONVERTERS
# import converters
# custom_imports = dict(
#     imports=['.converters'], allow_failed_imports=False)

from converters import CONVERTERS


converter_cfg = dict(type='Converter1', a=123, b=1213)
converter = CONVERTERS.build(converter_cfg)

print(1)
    # converter3_cfg = dict(type='converter3', a=213, b=2323)
    # converter3 = CONVERTERS.build(converter3_cfg)
