import csv
import pandas as pd 



location = pd.read_csv('/Users/harry/Desktop/election project/voteData/2008 立委/不分區政黨/elbase(merged).csv', names = ['省別', '縣市別', '選區別', '鄉鎮市區', '村里別', '地名'], dtype = object)
vote = pd.read_csv('/Users/harry/Desktop/election project/voteData/2008 立委/不分區政黨/elctks.csv', index_col = False, names = ['省別', '縣市別', '選區別', '鄉鎮市區', '村里別', '投開票所', '政黨號次', '得票數', '得票率','當選註記'], dtype = object)
print(location)
print(vote)

res = pd.merge(location, vote, on = ['省別', '縣市別', '鄉鎮市區', '村里別'], how = 'right', indicator = True)

res.to_csv('/Users/harry/Desktop/election project/2008 立委.csv', sep='\t', encoding='utf-8')

party = pd.read_csv('/Users/harry/Desktop/election project/voteData/2008 立委/不分區政黨/elcand.csv', index_col = False, names = ['政黨號次', '政黨名稱', '政黨代碼'], dtype = object, encoding='utf-8')

res.sort_values(by = ['政黨號次'])
print(res)

res2 = pd.merge(res, party, on = '政黨號次', how = 'left')
print(res2)
res2.to_csv('/Users/harry/Desktop/election project/2008 立委.csv', sep='\t', encoding='utf-8')


vote = pd.read_csv('/Users/harry/Desktop/election project/voteData/20120114-總統及立委/區域立委/elctks.csv', index_col = False, names = ['省別', '縣市別', '選區別', '鄉鎮市區', '村里別', '投開票所', '政黨號次', '得票數', '得票率','當選註記'], dtype = object)
print(vote)


