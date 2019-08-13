"""
scrapy.linkextractors

This package contains a collection of Link Extractors.

For more info see docs/topics/link-extractors.rst
"""

import re

from six.moves.urllib.parse import urlparse

from parsel.csstranslator import HTMLTranslator

from w3lib.url import canonicalize_url

from scrapy.utils.misc import arg_to_iter
from scrapy.utils.url import (
    url_is_from_any_domain, url_has_any_extension,
)


# common file extensions that are not followed if they occur in links
IGNORED_EXTENSIONS = [
    # images
    'mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp', 'tif',
    'tiff', 'ai', 'drw', 'dxf', 'eps', 'ps', 'svg',

    # audio
    'mp3', 'wma', 'ogg', 'wav', 'ra', 'aac', 'mid', 'au', 'aiff',

    # video
    '3gp', 'asf', 'asx', 'avi', 'mov', 'mp4', 'mpg', 'qt', 'rm', 'swf', 'wmv',
    'm4a', 'm4v', 'flv',

    # office suites
    'xls', 'xlsx', 'ppt', 'pptx', 'pps', 'doc', 'docx', 'odt', 'ods', 'odg',
    'odp',

    # other
    'css', 'pdf', 'exe', 'bin', 'rss', 'zip', 'rar',
]


_re_type = type(re.compile("", 0))

# url 匹配任一正则即可
_matches = lambda url, regexs: any(r.search(url) for r in regexs)

# 判断是否合法url
_is_valid_url = lambda url: url.split('://', 1)[0] in {'http', 'https', 'file'}


class FilteringLinkExtractor(object):

    _csstranslator = HTMLTranslator()

    def __init__(self, link_extractor, allow, deny, allow_domains, deny_domains,
                 restrict_xpaths, canonicalize, deny_extensions, restrict_css):

        self.link_extractor = link_extractor

        # 黑白名正则名单
        self.allow_res = [x if isinstance(x, _re_type) else re.compile(x)
                          for x in arg_to_iter(allow)]
        self.deny_res = [x if isinstance(x, _re_type) else re.compile(x)
                         for x in arg_to_iter(deny)]

        # 黑白域名
        self.allow_domains = set(arg_to_iter(allow_domains))
        self.deny_domains = set(arg_to_iter(deny_domains))

        self.restrict_xpaths = tuple(arg_to_iter(restrict_xpaths))
        self.restrict_xpaths += tuple(map(self._csstranslator.css_to_xpath,
                                          arg_to_iter(restrict_css)))

        self.canonicalize = canonicalize

        # 拒绝后缀名
        if deny_extensions is None:
            deny_extensions = IGNORED_EXTENSIONS
        self.deny_extensions = {'.' + e for e in arg_to_iter(deny_extensions)}

    def _link_allowed(self, link):
        if not _is_valid_url(link.url):
            # 非法url
            return False
        if self.allow_res and not _matches(link.url, self.allow_res):
            # 不再允许规则里面
            return False
        if self.deny_res and _matches(link.url, self.deny_res):
            # 在拒绝规则里面
            return False

        # 解析url
        parsed_url = urlparse(link.url)
        if self.allow_domains and not url_is_from_any_domain(parsed_url, self.allow_domains):
            # 不再允许域名里面
            return False
        if self.deny_domains and url_is_from_any_domain(parsed_url, self.deny_domains):
            # 在拒绝域名里面
            return False
        if self.deny_extensions and url_has_any_extension(parsed_url, self.deny_extensions):
            # 在拒绝后缀名里面
            return False
        # 可以
        return True

    def matches(self, url):
        # 域名规则判断
        if self.allow_domains and not url_is_from_any_domain(url, self.allow_domains):
            return False
        if self.deny_domains and url_is_from_any_domain(url, self.deny_domains):
            return False

        # url 正则规则判断
        allowed = (regex.search(url) for regex in self.allow_res) if self.allow_res else [True]
        denied = (regex.search(url) for regex in self.deny_res) if self.deny_res else []
        return any(allowed) and not any(denied)

    def _process_links(self, links):
        # 过滤链接
        links = [x for x in links if self._link_allowed(x)]
        # 归一化链接
        if self.canonicalize:
            for link in links:
                link.url = canonicalize_url(link.url)
        # 处理链接
        links = self.link_extractor._process_links(links)
        return links

    def _extract_links(self, *args, **kwargs):
        return self.link_extractor._extract_links(*args, **kwargs)


# Top-level imports
# 链接提取器
from .lxmlhtml import LxmlLinkExtractor as LinkExtractor
