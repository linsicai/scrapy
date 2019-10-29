"""
Scrapy signals

These signals are documented in docs/topics/signals.rst. Please don't add new
signals here without documenting them there.
"""

# 信号集合

# 引擎开始、结束
engine_started = object()
engine_stopped = object()

# 蜘蛛打开、空闲、关闭、错误
spider_opened = object()
spider_idle = object()
spider_closed = object()
spider_error = object()

# 请求调度、抛弃
request_scheduled = object()
request_dropped = object()

# 响应接收、下载
response_received = object()
response_downloaded = object()

# 项目爬取、抛弃
item_scraped = object()
item_dropped = object()

# for backwards compatibility
# 兼容性？
stats_spider_opened = spider_opened
stats_spider_closing = spider_closed
stats_spider_closed = spider_closed
item_passed = item_scraped
request_received = request_scheduled
