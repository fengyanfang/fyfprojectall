#coding=utf8
from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.get("http://music.baidu.com/top/new")
dr.implicitly_wait(10)

ele=dr.find_element_by_id("songList")

ul = ele.find_element_by_tag_name("ul")
lis = ul.find_elements_by_tag_name("li")
for song in lis:
    #返回是列表，列表为空不会报异常
    if song.find_elements_by_class_name("up"):
        author = song.find_element_by_class_name("author_list").text

        snamestr = song.find_element_by_class_name("song-title")
        sname = snamestr.find_element_by_tag_name("a").text

        print u"10%s:%s"%(sname,author)




dr.quit()
