# import requests
# from parsel import Selector
#
# from Database.sql_commands import Database
#
#
# class AnimeNewsScraper:
#     headers = {
#         # ...
#     }
#     MAIN_URL = "https://www.sportskeeda.com/anime/news"
#     LINK_XPATH = '//div[@class="feed-item-secondary"]/div/a/@href'
#     IMG_XPATH = '//div[@class="feed-item-secondary"]/div/img/@src'
#     PLUS_URL = "https://www.sportskeeda.com"
#
#     def parse_data(self):
#         try:
#             html = requests.get(url=self.MAIN_URL, headers=self.headers).text
#             tree = Selector(text=html)
#             links = tree.xpath(self.LINK_XPATH).extract()
#             images = tree.xpath(self.IMG_XPATH).extract()
#             db = Database()
#
#             for link in links:
#                 print(self.PLUS_URL + link)
#                 db.sql_insert_news_element(self.PLUS_URL + link)
#             return links[:5]
#         except Exception as e:
#             print(f"Error occurred: {e}")
#             return []
#
#
# if __name__ == "__main__":
#     scraper = AnimeNewsScraper()
#     scraper.parse_data()
