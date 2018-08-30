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
print(choiceCategories)
#print(random.choices(categories, k=3))
#print(locations)

moviesOutput = []
#moviesOutput = [['光荣的日子', '9.1', '喜剧', '法国', 'https://movie.douban.com/subject/3724036/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1112469352.jpg'], ['加油,法国队!', '9.0', '喜剧', '法国', 'https://movie.douban.com/subject/3700124/', 'https://img3.doubanio.com/view/subject/l/public/s3754010.jpg'], ['Emilie Muller', '9.0', '喜剧', '法国', 'https://movie.douban.com/subject/5094893/', 'https://img3.doubanio.com/view/subject/l/public/s9087505.jpg'], ['我是海尔姆特', '9.4', '喜剧', '德国', 'https://movie.douban.com/subject/5360245/', 'https://img3.doubanio.com/view/subject/l/public/s4533690.jpg'], ['美丽人生', '9.5', '喜剧', '意大利', 'https://movie.douban.com/subject/1292063/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p510861873.jpg'], ['流浪者之歌', '9.0', '喜剧', '意大利', 'https://movie.douban.com/subject/1303525/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2384320756.jpg'], ['三傻大闹宝莱坞', '9.2', '喜剧', '印度', 'https://movie.douban.com/subject/3793023/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p579729551.jpg'], ['彩虹', '9.0', '喜剧', '加拿大', 'https://movie.douban.com/subject/1971485/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p503390374.jpg'], ['汉纳·加斯比：娜奈特', '9.5', '喜剧', '澳大利亚', 'https://movie.douban.com/subject/30253080/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2525732775.jpg'], ['土豆工厂', '9.4', '喜剧', '澳大利亚', 'https://movie.douban.com/subject/1793083/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2233036824.jpg'], ['迪兰·莫兰：是什么？', '9.2', '喜剧', '澳大利亚', 'https://movie.douban.com/subject/4850732/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2517976810.jpg'], ['Tim Minchin: So Live', '9.0', '喜剧', '澳大利亚', 'https://movie.douban.com/subject/3893420/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2509370314.jpg'], ['克拉姆一家2', '9.0', '喜剧', '丹麦', 'https://movie.douban.com/subject/1775004/', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2512170335.jpg']]

for category in choiceCategories:
	for location in locations:
		movies = getMovies(category, location)
		moviesOutput += movies

print(list(moviesOutput))

print(moviesOutput[0])
print(moviesOutput[1][0])
print(moviesOutput[1][1])
with open("movies.csv", "w", newline="") as csvfile:
    movies_writer = csv.writer(csvfile, delimiter=",")
    for i in moviesOutput:
        movies_writer.writerow([i[0], i[1], i[2], i[3], i[4], i[5]])
csvfile.close()


#任务6: 统计电影数据

