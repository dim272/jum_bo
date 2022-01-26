import re


class JumBoPipeline:

    def process_item(self, item, spider):
        # if int in title
        if item['title'] and re.search('[0-9]', item['title']):
            i = re.search('[0-9]', item['title'])
            index_for_split = i.regs[0][0]
            title = item['title'][:index_for_split - 1]
            item['title'] = f'{title.strip("-").strip()}, {item["title"][index_for_split:]}'

        # if item get promotion list
        if isinstance(item.get('marketing_tags'), list):
            tag_list = []
            for promotion in item['marketing_tags']:
                tags = promotion.get('tags', [])
                for tag in tags:
                    tag_name = tag.get('text')
                    tag_list.append(tag_name.strip()) if tag_name else None
            item['marketing_tags'] = tag_list

        # if item get category list
        if isinstance(item.get('section'), list):
            breadcrumbs = []
            for _ in item['section']:
                breadcrumbs.append(_.get('label')) if _.get('label') else None
                ancestors = _.get('ancestors', [])
                for ancestor in ancestors:
                    breadcrumbs.append(ancestor.get('label')) if ancestor.get('label') else None
            breadcrumbs.reverse()
            item['section'] = breadcrumbs

        # if item get price data
        if isinstance(item.get('price_data'), dict):
            prices = item['price_data']
            original = prices.get('price') / 100 if prices.get('price') else None
            current = prices.get('promoPrice') if prices.get('promoPrice') else original
            if current and original and current < original:
                sale_tag = f"Скидка {(original - current) * 100 / original}%"
            else:
                sale_tag = None
            item['price_data'] = dict(
                current=current,
                original=original,
                sale_tag=sale_tag
            )

        return item
