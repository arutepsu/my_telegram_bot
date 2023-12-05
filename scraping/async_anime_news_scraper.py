import httpx
from parsel import Selector
import asyncio

class AsyncNewsScraper:
    headers = {
        # ...
    }
    MAIN_URL = "https://www.sportskeeda.com/anime/news"
    LINK_XPATH = '//div[@class="feed-item-secondary"]/div/a/@href'
    IMG_XPATH = '//div[@class="feed-item-secondary"]/div/img/@src'
    PLUS_URL = "https://www.sportskeeda.com"

    TEMPLATE_CONTAINS_XPATH = '//a[contains(@id, "app-show-episode-title")]'

    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            async for page in self.async_generator(limit=3):
                await self.get_url(
                    client=client,
                    url=self.MAIN_URL.format(
                        page=page
                    )
                )

    async def get_url(self, client, url):
        response = await client.get(url=url)
        print("response: ", response)
        await self.scrape_responses(response)

    async def scrape_responses(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print("PLUS_URL: ", self.PLUS_URL + link)

if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    scraper.parse_pages()