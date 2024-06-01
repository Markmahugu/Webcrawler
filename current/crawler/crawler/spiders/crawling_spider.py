import scrapy


class CrawlingSpider(scrapy.Spider):
    name = "mycrawler"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/?q=Boston+Bruins"]

    def parse(self, response):
        # Find links to detail pages
        links = response.xpath("//a[@class='team-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_team_page)

    def parse_team_page(self, response):
        # Extract team name and stats from the detail page
        team_name = response.xpath("//h3[contains(@class, 'team-name')]/text()").get()
        team_stats = response.xpath("//div[contains(@class, 'team-stats')]/p/text()").getall()

        if not team_name:
            team_name = "No Team Name Found"

        item = {
            'team_name': team_name,
            'team_stats': team_stats
        }

        self.logger.info('Extracted item: %s', item)
        yield item
