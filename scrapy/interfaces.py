from zope.interface import Interface

// 蜘蛛加载者
class ISpiderLoader(Interface):

    // 从配置生成实例
    def from_settings(settings):
        """Return an instance of the class for the given settings"""

    // 返回制定名字对应的蜘蛛类
    def load(spider_name):
        """Return the Spider class for the given spider name. If the spider
        name is not found, it must raise a KeyError."""

    // 返回所有蜘蛛名
    def list():
        """Return a list with the names of all spiders available in the
        project"""

    // 返回所有可以处理这个请求的蜘蛛类
    def find_by_request(request):
        """Return the list of spiders names that can handle the given request"""


# ISpiderManager is deprecated, don't use it!
# An alias is kept for backwards compatibility.
// 兼容性
ISpiderManager = ISpiderLoader
