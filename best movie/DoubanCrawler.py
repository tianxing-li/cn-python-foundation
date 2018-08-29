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

#任务3: 定义电影类

#任务4: 获得豆瓣电影的信息

#任务5: 构造电影信息数据表

#任务6: 统计电影数据