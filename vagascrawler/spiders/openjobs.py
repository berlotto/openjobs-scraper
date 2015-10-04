# -*- coding: utf-8 -*-
import scrapy
import re
import rethinkdb as r
from vagascrawler.items import VagaItem


class OpenjobsSpider(scrapy.Spider):
    name = "openjobs"
    allowed_domains = ["openjobs.com.br"]
    start_urls = (
        'http://www.openjobs.com.br/',
    )

    def striphtml(self, data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)

    def parse_body(self, response):
        body = self.striphtml(response.css("div.body").extract_first())
        data = response.meta['data']
        data['body'] = body
        data['datetime'] = r.now()
        item = VagaItem(data)
        yield item

    def parse(self, response):
        vagas = response.css("div.views-row")
        for vaga in vagas:
            data = {
                "link" : response.urljoin(vaga.css("h2.title a::attr(href)").extract_first()),
                "path" : vaga.css("h2.title a::attr(href)").extract_first(),
                "titulo" : vaga.css("h2.title a span::text").extract_first(),
                "empresa" : vaga.css("h3.company a::text").extract_first(),
                "cidade" : vaga.css("h4.city a::text").extract_first(),
                "categoria" : vaga.css("h4.category::text").extract_first().replace('\r\n','').strip(),
            }
            request = scrapy.Request(data['link'], callback=self.parse_body)
            request.meta['data'] = data
            yield request
