

"""
1~50頁文章標題爬取
"""

import requests, urllib
from bs4 import BeautifulSoup

"""
url = "https://bitcointalk.org/index.php?board=1.0"
res = requests.get(url).text
res = BeautifulSoup(res, "lxml")

list = res.findAll("a", {"class":"navPages"})

web_list = []
for element in list:
	web_list.append(element["href"])

for target_url in web_list:
	res = requests.get(target_url).text
	res = BeautifulSoup(res, "lxml")

	for i in res.findAll("td", {"class":"windowbg", "valign":"middle", "align":""}):
		print(i.text)
		print(i.span.a["href"])
"""

url = "https://bitcointalk.org/index.php?board=1.40"
res = BeautifulSoup(requests.get(url).text, "lxml")

title = []
title_url = []
for i in res.findAll("td", {"class":"windowbg", "valign":"middle", "align":""}):
	title.append(i.text.strip())
	title_url.append(i.span.a["href"])

list = []
for i in res.findAll("td", {"class":"windowbg", "valign":"middle", "width":"4%", "align":"center"}):
	list.append(i.text)

replies = []
x = 0
for x in range(0, len(list)):
	replies.append(list[x].strip())
	x += 2
print(replies)

views = []
x = 0
for x in range(1, len(list)):
	views.append(list[x].strip())
	x += 2

started_by = []
for i in res.findAll("td", {"class":"windowbg2", "valign":"middle", "width":"14%"}):
	started_by.append(i.a.text)

dict = {"title":[], "title_url":[], "replies":[], "views":[], "started_by":[]}

print(len(title))
print(len(replies))
print(len(views))
print(len(started_by))

