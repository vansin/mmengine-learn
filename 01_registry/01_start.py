# import converters

# from  import CONVERTERS
# import converters
# custom_imports = dict(
#     imports=['.converters'], allow_failed_imports=False)

from converters import CONVERTERS

a_value = 'a_value'
b_value = 'b_value'

converter_cfg = dict(type='Converter1', a=123, b=1213)
converter = CONVERTERS.build(converter_cfg)

converter3_cfg = dict(type='converter3', a=a_value, b=b_value)
# returns the calling result
converter3 = CONVERTERS.build(converter3_cfg)
