BOT_NAME = 'fang'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.25


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   # 'fang.pipelines.FangPipeline': 300,
   'fang.pipelines.MongoPipeline': 400,
   'fang.pipelines.MysqlTwistedPipline': 420,
}

DOWNLOADER_MIDDLEWARES = {
    'fang.middlewares.UserAgent': 300,
}

# 1、确保request存储到redis中
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True

# A、建立redis连接
# 设置连接redis信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

# B、建立MongoDB连接
MONGO_URL = 'mongodb://root:123456@127.0.0.1:27017'

# C、建立MySQL连接
MYSQL_HOST = '127.0.0.1'
MYSQL_DATABASE = 'fangtianxia'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'Sql_Lei'

