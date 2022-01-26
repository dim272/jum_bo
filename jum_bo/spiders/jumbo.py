import json
from json.decoder import JSONDecodeError
from datetime import datetime

import scrapy

import jum_bo.values
from jum_bo.items import JumboMainItem


class JumboSpider(scrapy.Spider):
    name = 'jumbo'
    url = "https://www.jumbo.com/api/graphql"

    def start_requests(self):
        categories = [
            "/producten/koek,-gebak,-snoep,-chips/chocolade/",
            "/producten/brood,-cereals,-beleg/brood/"
        ]

        for category in categories:
            body = jum_bo.values.REQUEST_BODY
            body['variables']["categoryUrl"] = category
            yield scrapy.http.JsonRequest(
                url=self.url,
                data=body,
                headers=jum_bo.values.HEADERS,
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response, **kwargs):
        try:
            data = json.loads(response.text)
            search_result = data['data']['searchResult']
            products = search_result['productsResultList']['products']
        except (TypeError, KeyError, JSONDecodeError) as e:
            self.logger.error(f"{e}\nData:{response.text[:100]}\n")
            return None

        for product in products:
            yield JumboMainItem(**dict(
                timestamp=datetime.timestamp(datetime.now()),
                RPC=product.get('id'),
                url=response.urljoin(product.get('link')) if product.get('link') else None,
                title=product.get('title'),
                marketing_tags=product.get('promotions'),
                brand=product.get('brand'),
                section=search_result.get('selectedRefinements', {}).get('refinementCrumbs'),
                price_data=product.get('prices'),
                stock=dict(in_stock=product.get('isAvailable', False)),
                assets=dict(main_image=product.get('image')) if product.get('image') else None
            ))

        # pagination
        products_result = search_result.get('productsResultList', {})
        total_products = products_result.get('totalNumRecs')
        offset = products_result.get('lastRecNum')
        if total_products and offset:
            if offset < total_products and offset < 100:
                new_body = json.loads(response.request.body)
                new_body['variables']['offSet'] = offset
                yield response.request.replace(data=new_body)
