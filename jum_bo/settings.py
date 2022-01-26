from datetime import datetime

BOT_NAME = 'jum_bo'
SPIDER_MODULES = ['jum_bo.spiders']
NEWSPIDER_MODULE = 'jum_bo.spiders'

FEED_URI = datetime.now().strftime('%Y-%m-%d_%H:%M:%S_') + 'result.json'
FEED_FORMAT = 'json'
FEED_EXPORTERS = {'json': 'scrapy.exporters.JsonItemExporter'}
FEED_EXPORT_ENCODING = 'utf-8'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
   'jum_bo.middlewares.NLProxyListMiddleware': 300,
}

ITEM_PIPELINES = {
   'jum_bo.pipelines.JumBoPipeline': 300,
}
