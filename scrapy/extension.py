"""
The Extension Manager

See documentation in docs/topics/extensions.rst
"""

from scrapy.middleware import MiddlewareManager

from scrapy.utils.conf import build_component_list

# 扩展中间件
class ExtensionManager(MiddlewareManager):
    component_name = 'extension'

    @classmethod
    def _get_mwlist_from_settings(cls, settings):
        return build_component_list(settings.getwithbase('EXTENSIONS'))
