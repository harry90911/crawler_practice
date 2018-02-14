
import csv, requests

with open("/Users/harry/Desktop/election project/管碧玲施政質詢.csv", "r", newline="", encoding='utf-8') as f:
	reader = csv.reader(f)
	my_list = list(reader)
	final_list = []
	for k in range(1, len(my_list)):
		my_dict = {"case":[], "url":[]}
		my_dict["url"] = my_list[k][0]
		my_dict["case"] = my_list[k][1]
		final_list.append(my_dict)
	print(final_list)

"""
for index in range(1, len(my_list)):
	url = final_list[index]["case"]
	headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 
	response = requests.get(url, headers = headers, stream = True)

	with open('/Users/harry/Desktop/election project/pdf/{}.pdf'.format(final_list[index]["url"]), 'wb') as f:
		f.write(response.content)
"""

url = "https://lis.ly.gov.tw/lylgmeetc/lgmeetkm?001F4751000E01010000040000000D200000003D000000000^IMG_lgimg_1^xdd!cecacec9cac6c7cbc6c881c6c8cecbcfcfc4cfcfcaccc4cfcfcac9"
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} 
r = requests.get(url, headers = headers, allow_redirects = True)
with open('/Users/harry/Desktop/election project/pdf/123.pdf', 'wb') as f:
	f.write(r.content)




