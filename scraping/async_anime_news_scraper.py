# import httpx
# from parsel import Selector
# import asyncio
#
#
# class AsyncAnimeNewsScraper:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#         'Accept-Language': 'en-GB,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Referer': "https://www.sportskeeda.com/anime/news",
#         'Connection': 'keep-alive',
#     }
#     MAIN_URL = "https://animecorner.me/category/news/anime-news/"
#     LINK_XPATH = '//li[@class="list-post pclist-layout"]//div/a/@href'
#     IMG_XPATH = '//li[@class="list-post pclist-layout"]//div/a[@class="penci-image-holder"]'
#     PLUS_URL = "https://animecorner.me/"
#
#     TEMPLATE_CONTAINS_XPATH = '//div[@class="primary-nav-items"]//li[@class=""]/a[contains(@id, href)]'
#     CATEGORIES_XPATH = '//div[@class="primary-nav-items"]//li[@class=""]/a/text()'
#
#     async def async_generator(self, limit):
#         for page in range(1, limit + 1):
#             yield page
#
#     async def parse_pages(self):
#         async with httpx.AsyncClient(headers=self.headers) as client:
#             gathered_data = []
#             async for page in self.async_generator(limit=3):
#                 response = await client.get(url=self.MAIN_URL.format(page=page))
#                 print("response: ", response)
#                 data = await self.scrape_responses(response)
#                 gathered_data.extend(data)
#
#             return gathered_data
#
#     async def scrape_responses(self, response):
#         tree = Selector(text=response.text)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         scraped_data = [self.PLUS_URL + link for link in links]
#         return scraped_data
#
#     async def get_url(self, client, url):
#         response = await client.get(url=url)
#         print("response: ", response)
#         await self.scrape_responses(response)
#
#
#
# if __name__ == "__main__":
#     scraper = AsyncAnimeNewsScraper()
#     scraper.parse_pages()
