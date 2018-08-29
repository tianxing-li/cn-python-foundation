import expanddouban as ed
from bs4 import BeautifulSoup as bs
import csv
import random

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
        #print(name, rate, info_link, cover_link)
        
        moviesInfo.append(Movie(name, rate, category, location, info_link, cover_link).listing())

    return moviesInfo

#print(list(getMovies('剧情','美国')))
#getMovies('剧情','美国')

#任务5: 构造电影信息数据表

categories = ['剧情', '喜剧', '动作', '爱情', '科幻', '悬疑', '惊悚', '恐怖', '犯罪', '同性', '音乐', 
'歌舞', '传记', '历史', '战争', '西部', '奇幻', '冒险', '灾难', '武侠', '情色']
locations = ['中国大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '德国', '意大利',
'西班牙', '印度', '泰国', '俄罗斯', '伊朗', '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']

choiceCategories = random.choices(categories, k=3)
#print(choiceCategories)
#print(random.choices(categories, k=3))
#print(locations)

moviesOutput = []
#moviesOutput = [['云南映象', '9.4', '歌舞', '中国大陆', 'https://movie.douban.com/subject/2282457/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2173058485.jpg'], ['丝路花雨', '9.3', '歌舞', '中国大陆', 'https://movie.douban.com/subject/3804492/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2266845549.jpg'], ['齐天乐', '9.3', '歌舞', '中国大陆', 'https://movie.douban.com/subject/11498192/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2515927004.jpg'], ['极限公益联欢会', '9.1', '歌舞', '中国大陆', 'https://movie.douban.com/subject/26830080/', 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2369019019.jpg']]


for category in choiceCategories:
	for location in locations:
		movies = getMovies(category, location)
		moviesOutput += movies

print(list(moviesOutput))


with open("movies.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
    movies_writer = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    for i in moviesOutput:
        movies_writer.writerows([i])
csvfile.close()

#任务6: 统计电影数据

