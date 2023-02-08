import scrapy


class HhkzSpider(scrapy.Spider):
    name = "hhkz"
    allowed_domains = ["hh.kz"]
    start_urls = ["http://hh.kz/search/vacancy?text=python&salary=&area=160&ored_clusters=true&enable_snippets=true"]

    def parse(self, response):
        candit = response.css('div.vacancy-serp-item-body')
        for cand in candit:
            item = {
            'name' : cand.css('a::text').get(),
                #the title of the link
            'adress' : cand.css('a::attr(href)').get()        
                #the adress of the link
            }
            yield item
        next_page = response.css('a[data-qa="pager-next"]::attr(href)').get()
            #next page button
        if next_page is not None:
            #while there is a next page button
             yield response.follow(next_page,callback=self.parse)
