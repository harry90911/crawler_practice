
from bs4 import BeautifulSoup
import requests, random, time

resto_list = []
for page in range(0,200):
#只抓第0頁到第99頁，當然也可以抓到兩三百頁，可是怕被愛評網封鎖ip
	time.sleep(random.randint(0,1))
	print("已經抓到第{}頁".format(page),"，","還有{}頁".format(200 - page))

	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 
		  # 1. 網址輸入的位置
	url = 'http://www.ipeen.com.tw/search/all/000/0-100-0-0/?p={}&adkw=%E5%A4%A7%E5%AE%89%E5%8D%80&so=commno'.format(page)
	response = requests.get(url, headers = headers)  

	soup = BeautifulSoup(response.content, "lxml")
	for num in range(0, 16):

		k = soup.findAll("div", {"class":"serShop"})[num]

		try:
			resto_name = k.find("a", {"data-label":"店名"}).text
			phone_id = k.find("img", {"alt":"電話號碼"})["src"]

			image_url = "http://www.ipeen.com.tw/{}".format(phone_id)
			phone_image = requests.get(image_url)
			with open("/Users/harry/Desktop/ipeen_phone/{}.jpg".format(resto_name), "wb") as f:
				f.write(phone_image.content)

		except AttributeError:
			print("Some tags was not found")
		except TypeError:
			print("phone number was not be found")
