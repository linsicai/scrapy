"""
Scrapy core exceptions

These exceptions are documented in docs/topics/exceptions.rst. Please don't add
new exceptions here without documenting them there.
"""

# 内部异常

# 未配置
class NotConfigured(Exception):
    """Indicates a missing configuration situation"""
    pass

# HTTP and crawling

# 忽略请求
class IgnoreRequest(Exception):
    """Indicates a decision was made not to process a request"""

# 未关闭Spider
class DontCloseSpider(Exception):
    """Request the spider not to be closed yet"""
    pass

# 关闭Spider
class CloseSpider(Exception):
    """Raise this from callbacks to request the spider to be closed"""

    def __init__(self, reason='cancelled'):
        super(CloseSpider, self).__init__()
        self.reason = reason

# Items

# 抛弃项
class DropItem(Exception):
    """Drop item from the item pipeline"""
    pass

# 未支持
class NotSupported(Exception):
    """Indicates a feature or method is not supported"""
    pass

# Commands

# usage错误
class UsageError(Exception):
    """To indicate a command-line usage error"""
    def __init__(self, *a, **kw):
        self.print_help = kw.pop('print_help', True)
        super(UsageError, self).__init__(*a, **kw)

# 抛弃告警
class ScrapyDeprecationWarning(Warning):
    """Warning category for deprecated features, since the default
    DeprecationWarning is silenced on Python 2.7+
    """
    pass

# xx失败
class ContractFail(AssertionError):
    """Error raised in case of a failing contract"""
    pass
