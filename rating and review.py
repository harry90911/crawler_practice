from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, csv, re


resto_list = []
# 1. 輸入你想要尋找的餐廳表單的路徑
with open("/Users/harry/Desktop/Uber project/resto.csv", encoding='utf-8') as f:
	resto_csv = csv.reader(f)
	resto = []
	for index in resto_csv:
		resto.append(index[0])
	print(resto)

# 2. 輸入儲存chromedriver的路徑
driver = webdriver.Chrome("/Users/harry/anaconda/selenium/webdriver/chromedriver")
match1 = "https://zh-tw.facebook.com/"
match2 = "https://www.foodpanda.com.tw"

for index in resto:
	driver.get("https://www.google.com.tw/")

	search = driver.find_element_by_name('q')
	search.send_keys("{}".format(index))
	search.send_keys(Keys.RETURN)

	timeout = 0.5
	try:
		element_present = EC.presence_of_element_located((By.XPATH, "//*[@id='rhs_block']/div/div[1]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/span[1]"))
		WebDriverWait(driver, timeout).until(element_present)
	except TimeoutException:
		pass
	
	resto = {"resto name":[], "google rating":[], "facebook rating":[], "google review":[], "facebook review":[], "resto phone":[], "panda":[]}
	soup = BeautifulSoup(driver.page_source, "lxml")


	if soup.find("a",{"class":"_B2n"}) is not None:
		facebook_rating = soup.find("a",{"class":"_B2n"}).find("span",{"class":"_G2n _N2n"}).text
		facebook_review = soup.find("a",{"class":"_B2n"}).find("span",{"class":"_G2n _d3n"}).text
		resto["facebook rating"] = facebook_rating
		resto["facebook review"] = facebook_review
	else:
		print("can't find facebook")

	if soup.select('div[class="_mr"]') is not None:
		resto["panda"] = "Yes"
	else:
		resto["panda"] = "No"


	try:
		resto["resto name"] = index

		google_rating = soup.find("span",{"class":"rtng"}).text
		resto["google rating"] = google_rating

		google_review = soup.find("a",{"data-async-trigger":"reviewDialog"}).text
		resto["google review"] = google_review

		resto_phone = soup.find("span", {"data-dtype":"d3ph"}).text
		resto["resto phone"] = resto_phone

	except AttributeError as e:
		print("some tag not be found")
		pass

	resto_list.append(resto)
	print(resto)

print(resto_list)

with open("/Users/harry/Desktop/Uber project/ipeen_ratn&revw.csv", "w", newline="", encoding='utf-8') as f:
		  # 3. 你需要變更成自己存放檔案的位置，這個位置是我電腦上的位置
	writer = csv.writer(f)
	writer.writerow(resto_list[0].keys())
	for row in resto_list:
		writer.writerow(row.values())

driver.quit()


