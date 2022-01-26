from scrapy import signals
import requests

import jum_bo.values


class NLProxyListMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        try:
            request.meta['proxy'] = self.proxy_list[0]
        except IndexError:
            pass

        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        """
        The proxy changes if we catch an exception
        """
        try:
            self.proxy_list.pop(0)
            request.meta['proxy'] = self.proxy_list[0]
            return request
        except IndexError:
            pass

    def spider_opened(self, spider):
        """
        Get proxy list from Netherlands
        """
        r = requests.get("https://proxy.webshare.io/api/proxy/list/?page=1&countries=NL",
                         headers={"Authorization": jum_bo.values.PROXY_API})
        response_json = r.json()
        self.proxy_list = [f"https://{el['username']}:{el['password']}@{el['proxy_address']}:{el['ports']['socks5']}"
                           for el in response_json['results']]

        spider.logger.info('Spider opened: %s' % spider.name)
