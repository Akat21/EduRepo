from tkinter.ttk import Separator
from pytrends.request import TrendReq
import pandas as pd
import time

startTime = time.time()
pytrend = TrendReq(hl='en-GB', tz=360)

colnames = ["keywords"]
df = pd.read_csv("keyword_list.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("Keywords")

dataset = []
dataset2 = []
for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe='2020-04-01 2020-05-01',
     geo='GB')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

def checker():
    for letter in keywords[0]:
        if ord(letter) == 32:
            return False
    return True
df3 = []

for y in range(0,len(df2)):
    keywords = [df2[y]]
    print(keywords)
    if checker() == False:
        continue
    print(keywords)
    pytrend.build_payload(
    kw_list=keywords,
    cat=0,
    timeframe='2020-04-01 2020-05-01',
    geo='GB')
    related = pytrend.related_queries()
    print(related[df2[y]]['top'])
    related = related[df2[y]].values()
    res = [el for el in related]
    dataset2.append(res[0]['query'])
    dataset2.append(res[0]['value'])
    df3.append(df2[y])

result = pd.concat(dataset, axis=1)
result.to_csv('search_trends.csv')

df4 = []
for el in df3:
    df4.append(el)
    df4.append(el + " search volume")

if len(dataset2) != 0:
    result = pd.concat(dataset2,axis=1)
    result.to_csv('search_trends.csv', mode = 'a', index = False, header = df4)

executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))