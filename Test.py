import unittest
import requests
import DA_Team_3
class Test(unittest.TestCase):

    def test_successful(self):
        url = 'http://172.18.58.238/photography/'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

import scrapy

class NewSpider(scrapy.Spider):
     name = "new_spider"
     start_urls = ['http://wikipedia.org']
     def parse(self, response):
          css_selector = "img"
          for x in response.css(css_selector):
               newsel = '@src'
               yield {
                    'Image Link': x.xpath(newsel).extract_first(),
               }
          Page_selector = '.next a ::attr(href)'
          next_page = response.css(Page_selector).extract_first()
          if next_page:
               yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
               )

if __name__ == '__main__':
    unittest.main()
