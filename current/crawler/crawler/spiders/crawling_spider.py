import scrapy

class CrawlingSpider(scrapy.Spider):
    name = "mycrawler"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/?q=Boston+Bruins"]

    def parse(self, response):
        # Update the XPath expressions to match the actual HTML structure of the page
        team_name = response.xpath("//h3[@class='team-name']/text()").get()
        team_stats = response.xpath("//div[@class='team-stats']/p/text()").getall()

        if not team_name:
            team_name = "No Team Name Found"

        item = {
            'team_name': team_name,
            'team_stats': team_stats
        }

        self.logger.info('Extracted item: %s', item)
        yield item
