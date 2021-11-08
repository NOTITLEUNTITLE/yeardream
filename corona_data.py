import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt,endCreateDt):
  url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
  params = {
    'serviceKey' : 'YqzCT78WB9xtv3oWKSRHVpxjxWnXqEvM5+CV7gO91i1BqlBrAa4TdlgSJdrsANJ8d92k1s0Ukb/6oN342K8I7w==',
    'pageNo' : '1',
    'numOfRows': 10,
    'startCreateDt': startCreateDt,
    'endCreateDt': endCreateDt
  }

  res = requests.get(url, params=params)

  # print(res.url)
  # test1 = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=YqzCT78WB9xtv3oWKSRHVpxjxWnXqEvM5%2BCV7gO91i1BqlBrAa4TdlgSJdrsANJ8d92k1s0Ukb%2F6oN342K8I7w%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200410&endCreateDt=20200410'
  # test2 = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=YqzCT78WB9xtv3oWKSRHVpxjxWnXqEvM5%2BCV7gO91i1BqlBrAa4TdlgSJdrsANJ8d92k1s0Ukb%2F6oN342K8I7w%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200410&endCreateDt=20200410'
  # flag = True
  # if len(test1) == len(test2):
  #   for i in range(len(test1)):
  #     if test1[i] != test2[i]:
  #       flag = False
  # print(flag)

  dict_data = xmltodict.parse(res.text)

  json_data = json.dumps(dict_data)

  dict_data = json.loads(json_data)
  total_count = dict_data['response']['body']['totalCount']
  if total_count == '0':
    return False




  pprint(dict_data['response']['body']['items']['item'])
  area_data = dict_data['response']['body']['items']['item']

  area_data.reverse()
  # for a in area_data:
  #   print(a)
  return area_data

