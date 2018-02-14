
from bs4 import BeautifulSoup
import urllib.request, re, random, time, csv, re

resto_list = []
for page in range(0, 100):
#只抓第0頁到第99頁，當然也可以抓到兩三百頁，可是怕被愛評網封鎖ip
	time.sleep(random.randint(0,1))
	
	print("已經抓到第{}頁".format(page),"，還有{}頁".format(100 - page))

	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 
		  # 1. 網址輸入的位置
	url = 'http://www.ipeen.com.tw/search/all/000/0-100-0-0/?p={}&adkw=%E8%98%86%E6%B4%B2%E5%8D%80'.format(page)
	request = urllib.request.Request(url, headers = headers)  
	response = urllib.request.urlopen(request) 

	soup = BeautifulSoup(response, "lxml")
	for num in range(0, 16):
		resto = {"id":[], "resto name":[], "resto price":[], "resto address":[], "resto catagory":[], "resto review":[], "resto rating":[]}
		k = soup.findAll("div", {"class":"serShop"})[num]

		resto["id"] = str(page) + str(num)

		try:
			resto_name = k.find("a", {"data-label":"店名"}).text
			resto["resto name"] = resto_name

			resto_price = k.find("li", {"class":"costEmpty"}).text
			resto_price = ''.join(resto_price.split())
			resto["resto price"] = resto_price

			resto_address = k.find("span", {"style":"padding-left:3em;"}).text
			resto_address = ''.join(resto_address.split())
			resto["resto address"] = resto_address

			resto_catagory = k.find("a", {"data-label":"大分類"}).text
			resto["resto catagory"] = resto_catagory

			resto_review = k.find("a", {"data-label":"文章"}).text
			resto["resto review"] = resto_review

			resto_rating = soup.find("img", {"class":"star"})["alt"]
			resto_rating = re.sub("[^0-9]", "", resto_rating)
			resto["resto rating"] = resto_rating
		
		except AttributeError as e:
			print("Some tags was not found")

		resto_list.append(resto)
		
print(resto_list)

with open("/Users/harry/Desktop/Uber project/ipeen蘆洲.csv", "w", newline="", encoding='utf-8') as f:
		  # 2. 你需要變更成自己存放檔案的位置，這個位置是我電腦上的位置
	writer = csv.writer(f)
	writer.writerow(resto_list[0].keys())
	for row in resto_list:
		writer.writerow(row.values())







