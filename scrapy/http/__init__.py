"""
Module containing all HTTP related classes

Use this module (instead of the more specific ones) when importing Headers,
Request and Response outside this module.
"""

# 头
from scrapy.http.headers import Headers

# 请求
from scrapy.http.request import Request
from scrapy.http.request.form import FormRequest
from scrapy.http.request.rpc import XmlRpcRequest

# 响应
from scrapy.http.response import Response
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.xml import XmlResponse
from scrapy.http.response.text import TextResponse
