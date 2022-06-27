import scrapy
import lxml.etree as le
import pandas as pd
import numpy as np
import re
import json


url_level1 = 'https://www.carlist.my/used-cars-for-sale/bmw/malaysia'
url_level2 = 'https://www.carlist.my/used-cars-for-sale/{brands}/malaysia?page_number={number}&page_size=25'


class CarlistSpider(scrapy.Spider):
    name = 'carlist'
    #allowed_domains = ['carlist.my']


    def start_requests(self):
        yield scrapy.Request(
            url = url_level1,
            callback=self.parse_start
        )

    def parse_start(self, response):

        text = response.body.decode('gbk', 'ignore')
        text = text.replace("\n", "").replace("'", "")
        texts = le.HTML(text).xpath('//ul[@class="smenu__select smenu__select--brand"]//text()')

        conv = []
        for element in texts:
            conv.append(element.strip())

        while ("" in conv):
            conv.remove("")

        brands = conv[1::2]
        numbers = conv[0::2]
        dictionary = dict(zip(brands, numbers))
        first_pair = list(dictionary.items())

        for element in first_pair:
            brands = element[0].lower().replace(" ", "-")
            number = int(np.ceil(int(element[1].replace(",", "")) / 25))
            for page in range(1, number+1):
                yield scrapy.Request(
                    url=url_level2.format(brands=brands, number=page),
                    callback=self.parse1,
                )

    def parse1(self, response):

        text = response.body.decode('gbk', 'ignore')
        text = text.replace("\n", "").replace("'", "")
        json_str = re.findall('json">(.*?)</script>', text)[0]
        datas = json.loads(json_str)
        datas1 = datas[1]['itemListElement']
        df = pd.json_normalize(datas1)
        yield df.to_csv('out.csv',mode='a', index=True, header=False)

