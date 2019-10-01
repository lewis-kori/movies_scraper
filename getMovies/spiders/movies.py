from scrapy import  Request,Spider
from ..items import GetmoviesItem
from .config import API_KEY
class moviesCrawl(Spider):
    name="movies"
    page_number=15

    url_link="https://www.themoviedb.org/movie?page=1"
    
    start_urls=['http://api.scraperapi.com/?api_key='+ API_KEY + '&url=' + url_link + '&render=true']

    def parse(self,response):
        movies=response.css("div.item.poster.card")
        items=GetmoviesItem()
        for movie in movies:
            items["title"]=movie.css('.title.result::text').extract()
            items["rating"]=movie.css(".user_score_chart::attr(data-percent)").extract()
            items["description"]=movie.css(".overview::text").extract()
            items["poster_link"]=movie.css('.poster.lazyload.fade::attr(data-src)').extract()

            yield items


        next_page_url = "https://www.themoviedb.org/movie?page="+ str(self.page_number)
        next_page='http://api.scraperapi.com/?api_key='+ API_KEY + '&url='+ next_page_url + '&render=true'

        if self.page_number<=2:
            self.page_number+=1
            yield response.follow(next_page,callback=self.parse)