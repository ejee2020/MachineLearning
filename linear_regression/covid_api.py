from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
import csv
import pandas as pd
from datetime import datetime,timedelta, date
from itertools import zip_longest
import xmltodict 

my_api_key = 'myxVj3oA9B2NCt0mWKotqwLqTt5%2FLuIbc%2BbVlR7EqNfT8ejQoP%2B6rh84JbFN0aaxADd%2FFLoFk3%2BlUUIdr9JLzQ%3D%3D'
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
days = []
sdate = date(2020, 2, 19)   # start date
e2date = date(2020, 3, 1)   # start date
e3date = date(2020, 8, 15)   # start date
edate = date(2021, 7, 16)   # end date
delta = e2date - sdate       # as timedelta
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    day = day.strftime("%Y%m%d")
    days.append(day)
nums = []
for i in range(len(days) - 1):
    yesterday = days[i]
    today = days[i + 1]
    queryParams = '?' + \
    'ServiceKey=' + '{}'.format(my_api_key) + \
    '&pageNo='+ '1' + \
    '&numOfRows='+ '999' + \
    '&startCreateDt={}&endCreateDt={}'.format(yesterday,today)
    result = requests.get(url + queryParams)
    result = result.content 
    jsonString = json.dumps(xmltodict.parse(result), indent = 4)
    jsonString = jsonString.replace('resultCode', '결과코드').replace('resultMsg', '결과메세지').replace('numOfRows', '한 페이지 결과 수').replace('pageNo', '페이지 수').replace('totalCount', '전체 결과 수').replace('seq', '게시글번호(감염현황 고유값)').replace('stateDt', '기준일').replace('stateTime', '기준시간').replace('decideCnt', '확진자 수').replace('clearCnt', '격리해제 수').replace('examCnt', '검사진행 수').replace('deathCnt', '사망자 수').replace('careCnt', '치료중 환자 수').replace('resutlNegCnt', '결과 음성 수').replace('accExamCnt', '누적 검사 수').replace('accExamCompCnt', '누적 검사 완료 수').replace('accDefRate', '누적 환진률').replace('createDt', '등록일시분초').replace('updateDt', '수정일시분초')
    js = json.loads(jsonString)
    js = js["response"]['body']['items']['item']
    pdata = pd.DataFrame(js)
    num_tested = int(pdata.loc[0][4]) - int(pdata.loc[1][4])
    nums.append(num_tested)
print("first round done")
print(nums)

days = []
delta = e3date - e2date 
for i in range(delta.days + 1):
    day = e2date + timedelta(days=i)
    day = day.strftime("%Y%m%d")
    days.append(day)
for i in range(len(days) - 1):
    yesterday = days[i]
    today = days[i + 1]
    queryParams = '?' + \
    'ServiceKey=' + '{}'.format(my_api_key) + \
    '&pageNo='+ '1' + \
    '&numOfRows='+ '999' + \
    '&startCreateDt={}&endCreateDt={}'.format(yesterday,today)
    result = requests.get(url + queryParams)
    result = result.content 
    jsonString = json.dumps(xmltodict.parse(result), indent = 4)
    jsonString = jsonString.replace('resultCode', '결과코드').replace('resultMsg', '결과메세지').replace('numOfRows', '한 페이지 결과 수').replace('pageNo', '페이지 수').replace('totalCount', '전체 결과 수').replace('seq', '게시글번호(감염현황 고유값)').replace('stateDt', '기준일').replace('stateTime', '기준시간').replace('decideCnt', '확진자 수').replace('clearCnt', '격리해제 수').replace('examCnt', '검사진행 수').replace('deathCnt', '사망자 수').replace('careCnt', '치료중 환자 수').replace('resutlNegCnt', '결과 음성 수').replace('accExamCnt', '누적 검사 수').replace('accExamCompCnt', '누적 검사 완료 수').replace('accDefRate', '누적 환진률').replace('createDt', '등록일시분초').replace('updateDt', '수정일시분초')
    js = json.loads(jsonString)
    js_check_count = js["response"]['body']['items']['item'][0]['검사진행 수']
    js = js["response"]['body']['items']['item']
    pdata = pd.DataFrame(js)
    num_tested = int(pdata.loc[0][7]) - int(pdata.loc[1][7])
    nums.append(num_tested)
print("second round done")
print(nums)
days = []
delta = edate - e3date 
for i in range(delta.days + 1):
    day = e3date + timedelta(days=i)
    day = day.strftime("%Y%m%d")
    days.append(day)
for i in range(len(days) - 1):
    yesterday = days[i]
    today = days[i + 1]
    queryParams = '?' + \
    'ServiceKey=' + '{}'.format(my_api_key) + \
    '&pageNo='+ '1' + \
    '&numOfRows='+ '999' + \
    '&startCreateDt={}&endCreateDt={}'.format(yesterday,today)
    result = requests.get(url + queryParams)
    result = result.content 
    jsonString = json.dumps(xmltodict.parse(result), indent = 4)
    jsonString = jsonString.replace('resultCode', '결과코드').replace('resultMsg', '결과메세지').replace('numOfRows', '한 페이지 결과 수').replace('pageNo', '페이지 수').replace('totalCount', '전체 결과 수').replace('seq', '게시글번호(감염현황 고유값)').replace('stateDt', '기준일').replace('stateTime', '기준시간').replace('decideCnt', '확진자 수').replace('clearCnt', '격리해제 수').replace('examCnt', '검사진행 수').replace('deathCnt', '사망자 수').replace('careCnt', '치료중 환자 수').replace('resutlNegCnt', '결과 음성 수').replace('accExamCnt', '누적 검사 수').replace('accExamCompCnt', '누적 검사 완료 수').replace('accDefRate', '누적 환진률').replace('createDt', '등록일시분초').replace('updateDt', '수정일시분초')
    js = json.loads(jsonString)
    print(js)
    js_check_count = js["response"]['body']['items']['item'][0]['검사진행 수']
    js = js["response"]['body']['items']['item']
    pdata = pd.DataFrame(js)
    print(pdata)
    print(pdata.loc[0][7])
    num_tested = int(pdata.loc[0][8]) - int(pdata.loc[1][8])
    nums.append(num_tested)
days = []
export_data = zip_longest(nums, fillvalue = '')
with open('./tested.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerows(export_data)


