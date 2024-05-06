# -*- coding: utf-8 -*-
# @Time    : 2022/10/9 15:32
# @Author  : Linyi
# @Site    : 
# @File    : GetRes.py
# @Software: PyCharm
import requests
import config
from bs4 import BeautifulSoup

import configparser

# 创建一个配置文件解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 读取配置文件中的值
ip = config.get('Network', 'IP')
v = config.get('Network', 'V')
jsessionid = config.get('Cookies', 'JSESSIONID')

url="http://gatesrv.lnu.edu.cn/login/verify"
url1="http://gatesrv.lnu.edu.cn/"

s=requests.Session()

html=s.get(url1).text

# 使用Beautiful Soup解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 使用选择器选择具有name属性为"checkcode"的<input>元素
input_element = soup.find('input', {'name': 'checkcode'})

# 检查是否找到了<input>元素
if input_element:
    # 提取value属性的值
    value = input_element.get('value')
    # print("value:", value)
else:
    print("未找到具有name属性为'checkcode'的<input>元素")

val=str(value)
# print(s.cookies)

data={
"foo":"",
"bar":"",
"checkcode": val,
"account": "20211491514",
"password": "69111b77ae1a655a7380678848743e34",
"code":""
}

headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":
"max-age=0",
"Connection":
"keep-alive",
"Cookie":
s.cookies,
"Host":
"gatesrv.lnu.edu.cn",
"Referer":
"http://gatesrv.lnu.edu.cn/login/?302=LI",
"Upgrade-Insecure-Requests":
"1",
"User-Agent":
"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"
}

res=s.post(url=url,data=data,allow_redirects = False)

# result=res.text

cookies=res.cookies
# print("获取cookies如下:")
# print('Cookies', cookies)
# print(result)
# print("目前状态")
# print(res.status_code)
# print("---------------------------------------------------------------------------")
cookies={"JSESSIONID":jsessionid}
res1=requests.get(url=url1,cookies=cookies)
result1=res1.text
# print("目前网站")
# print(res1.url)
soup=BeautifulSoup(result1,'lxml')

# 使用CSS选择器选择所有匹配的<dl>元素
dl_elements = soup.select('body > div.view-main > div > div:nth-child(2) > div.col-md-9.col-sm-8.col-xs-12 > div > div > div:nth-child(1) > div > div:nth-child(2) > dl')

def ke():
    # 遍历每个<dl>元素并输出其中的<dt>和<dd>内容
    for dl_element in dl_elements:
        dt_element = dl_element.find('dt')
        dd_element = dl_element.find('dd')
        if dt_element and dd_element:
            used_data = dt_element.get_text(strip=True)
            value = dd_element.get_text(strip=True)
            print("类型:", value)
            print("数量:", used_data)

def yi():
    # 查找<dt>标签下的文本内容（已用流量）
    dt_element = soup.find('dt')
    used_data = dt_element.get_text(strip=True)

    # 查找<dd>标签下的文本内容（数值）
    dd_element = soup.find('dd')
    value = dd_element.get_text(strip=True)

    # 打印结果
    print("类型:", value)
    print("数量:", used_data)

