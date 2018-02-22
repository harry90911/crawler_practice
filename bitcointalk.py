

"""
1~50頁文章標題爬取
1. 先定義要爬的討論區（完成）
2. 再來爬底下的頁面（完成）
3. 最後進到單一文章裡面爬文字(完成)
"""

import requests, urllib, csv, re
from bs4 import BeautifulSoup


#從不同討論區拿取url
def getResponse(url):
	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 

	request = urllib.request.Request(url, headers = headers)  
	res = BeautifulSoup(urllib.request.urlopen(request), "lxml")
	return res

#get title
def title():
	title = []
	title_url = []
	for i in res.findAll("td", {"class":"windowbg", "valign":"middle", "align":""}):
		title.append(i.span.a.text.strip())
		title_url.append(i.span.a["href"])
	return title

#get list of replies and views, because they are sibling.
def replies_and_views(arg):
	list = []
	results =  res.findAll("td", {"class":"windowbg", "valign":"middle", "width":"4%", "align":"center"})
	for result in results:
		if len(result.attrs) == 4:
			list.append(result.text.strip())

	#retrive replies from list
	replies = []
	x = 0
	while x < len(list):
		replies.append(list[x])
		x += 2

	#retrive views from list
	views = []
	x = 1
	while x < len(list):
		views.append(list[x])
		x += 2

	if arg == "replies":
		return replies	
	elif arg == "views":
		return views
	else:
		print("input replies or views in this function")

#get poster(started_by)
def poster():
	started_by = []
	results =  res.findAll("td", {"class":"windowbg2", "valign":"middle", "width":"14%"})
	for result in results:
		if len(result.attrs) == 3:
			started_by.append(result.a.text)
	return started_by

def find_depth_of_tree(soup):
	if hasattr(soup, "contents") and soup.contents:
		return max([find_depth_of_tree(child) for child in soup.contents]) + 1
	else:
		return 0

def content(res):
	contents = res.findAll("div", {"class":"post"})
	c = []

	posters = res.findAll("td", {"class":"poster_info"})
	times = res.findAll("td", {"class":"td_headerandpost"})
	p = []
	t = []

	for time in times:
		if time.find("div", {"class":"smalltext"}).text.isdigit() == False:
			t.append(time.find("div", {"class":"smalltext"}).text)
		else:
			pass
	"""
	for ele in t:
		print(ele)
	
	print(len(t))
	"""

	for poster in posters:
		if poster.find("a", title = re.compile("View the profile of (.+)")).text.isdigit() == False:
			p.append(poster.find("a", title = re.compile("View the profile of (.+)")).text)
		else:
			pass
	"""
	for ele in p:
		print(ele)

	print(len(p))
	"""
	for content in contents:
		dict = {"quoteheader":[], "quote":[], "quote_info":[], "main_reply":""}
		if len(content.attrs) == 1 and content.text.isdigit() == False:
			if find_depth_of_tree(content) > 2:
				dict["main_reply"] = content.find(text=True, recursive=False)
				
				for i in content.findAll("div", {"class":"quoteheader"}):
					dict["quoteheader"].append(i.text)
				
				for i in content.findAll("div", {"class":"quote"}):
					dict["quote"].append(re.sub("Quote\sfrom.*\d{2}:\d{2}:\d{2}\s(AM|PM)", "", i.find(text=True, recursive=False)))

				for i in range(0, len(dict["quote"])):
					dict["quote_info"].append([dict["quoteheader"][i], dict["quote"][i]])

				del dict["quoteheader"]
				del dict["quote"]
				c.append(dict)
			else:
				dict["main_reply"] = content.find(text=True, recursive=False)	
				c.append(dict)
	"""
	print(len(c))
	for ele in c:
		print(ele["quoteheader"])
		print(ele["quote"])
	"""
	final_list = []
	for i in range(0, len(c)):
		dict = {}
		dict["time"] = t[i]
		dict["poster"] = p[i]
		dict["content"] = c[i]
		final_list.append(dict)
	print(final_list)

content(getResponse("https://bitcointalk.org/index.php?topic=2871276.0;all"))

"""
url = "https://bitcointalk.org/index.php?board=67.40"
res = BeautifulSoup(requests.get(url).text, "lxml")

list = res.findAll("a", {"class":"navPages"})

page_list = []
for index in list:
	page_list.append(index["href"])

final_list = []

number = 0
for url in page_list:
	number += 1
	print("page{}".format(number))
	getResponse(url)
	t = title()
	r = replies_and_views("replies")
	v = replies_and_views("views")
	p = poster()

	for i in range(0, len(t)):
		dict = {}
		dict["title"] = t[i]
		dict["replies"] = r[i]
		dict["views"] = v[i]
		dict["poster"] = p[i]
		final_list.append(dict)

keys = final_list[0].keys()
with open("/Users/harry/Desktop/COBINHOOD/bitcointalk_title.csv", "w") as csvfile:
	dict_writer = csv.DictWriter(csvfile, keys)
	dict_writer.writeheader()
	dict_writer.writerows(final_list)




article_list = []
for index in page_list:
	res = BeautifulSoup(requests.get(index).text, "lxml")
	article = []
	for i in res.findAll("td", {"class":"windowbg", "valign":"middle", "align":""}):
		article.append(i.span.a["href"])
		article.append(i.span.a.text.strip())
		article_list.append(article)

for element in article_list:
	for ele in element:
		print(ele)
"""




