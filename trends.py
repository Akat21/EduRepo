from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Lewandowski"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='US', gprop='')
print(pytrends.interest_over_time())
print(pytrends.related_topics())