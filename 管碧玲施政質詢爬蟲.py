

from bs4 import BeautifulSoup
import urllib, csv
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 


#selenium拿到立法院網址

urls = {"page1":["https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?.9daf001F710030100000000000000006000000^100000002D000010544398"],
		"page2":["https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?.2a6107504101000D0000000000004000002000000001000014F103b7a#pgloc"], 
		"page3":["https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?.6abf001F4710510000002000D20000004000000000000000100053c4f#pgloc"],
		"page4":["https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?.30ba0F47101000300D000040000000000000200000001060005103bc3#pgloc"],
		"page5":["https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?.6bab00F710071000040000D2000040000000000000000001005413c74#pgloc"]}


for index in range(1, 6):
	request = urllib.request.Request(url = urls["page{}".format(index)][0], headers = headers)  
	response = urllib.request.urlopen(request) 
	soup = BeautifulSoup(response, "lxml")

	sumtr1_list = soup.findAll("tr", {"class":"sumtr1"})
	sumtr2_list = soup.findAll("tr", {"class":"sumtr2"})

	final_list_index = []
	for sumtr_list in [sumtr1_list, sumtr2_list]:
		for num in range(0, len(sumtr_list)):
			final_dict = {"case":[], "url":[]}

			case = sumtr_list[num].find("td", {"class":"sumtd2001"}).text
			case = ''.join(case.split())
			final_dict["case"] = case

			link_list = sumtr_list[num].findAll("a", {"class":"linkh"})
			for name in range(0, len(link_list)):
				if link_list[name].text == "管碧玲":
					url = "https://lis.ly.gov.tw{}".format(link_list[name].find_next_sibling("a", {"target":"pdftxt"})["href"])
					final_dict["url"] = url
			final_list_index.append(final_dict)

with open("/Users/harry/Desktop/election project/管碧玲施政質詢.csv", "w", newline="", encoding='utf-8') as f:
	writer = csv.writer(f)
	writer.writerow(["case", "url"])
	for index in range(1, 6):
		print(index)
		for row in final_list_index:
			writer.writerow(row.values())
