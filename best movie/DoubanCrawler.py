import expanddouban as ed
from bs4 import BeautifulSoup as bs
import csv

#任务1:获取每个地区、每个类型页面的URL

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""

def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
    return url

#test
#print(getMovieUrl('剧情','美国'))

#任务2: 获取电影页面 HTML

#url = getMovieUrl('剧情','美国')

#html = ed.getHtml(url, loadmore = "true")

#print(html)#test

#任务3: 定义电影类
class Movie:
    """name, rate, location, category, info_link, cover_link for Movie"""
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link
    def listing(self):
    	return [self.name, self.rate, self.location, self.category, self.info_link, self.cover_link]


#任务4: 获得豆瓣电影的信息
"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	#get url
    url = getMovieUrl(category, location)
    #get html
    html = ed.getHtml(url, loadmore = 'true')
    #analysis
    soup = bs(html, 'html.parser')
    movies = soup.find(class_="list-wp")
    moviesInfo = []
    #print(movies.find_all('a'))
    
    for i in movies.find_all('a'):
    	name = i.find(class_ = 'title').string
    	rate = i.find(class_ = 'rate').string
    	info_link = i.get('href')
    	cover_link = i.find('img').get('src')
    	print(name, rate, info_link, cover_link)
        
    	moviesInfo.append(Movie(name, rate, category, location, info_link, cover_link).listing())

    for i in moviesInfo:
    	print(i)
    return moviesInfo

#print(list(getMovies('剧情','美国')))
getMovies('剧情','美国')

#任务5: 构造电影信息数据表

#任务6: 统计电影数据