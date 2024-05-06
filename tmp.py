# -*- coding: utf-8 -*-
# @Time    : 2024/5/6 20:52
# @Author  : Linyi
# @Site    : 
# @File    : tmp.py
# @Software: PyCharm

import requests
import re
from lxml import etree
import hashlib
import configparser


def md5_lower(text):
    """计算字符串的MD5摘要，并以32位小写形式返回"""
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


session = requests.session()  # 实例化session对象

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.2261 SLBChan/10 "
}

url1 = "http://gatesrv.lnu.edu.cn/login/verify"
url2 = "http://gatesrv.lnu.edu.cn/login/?302=LI"
url3 = "http://gatesrv.lnu.edu.cn/dashboard"

data = {
    'foo': '',  # foo字段值
    'bar': '',  # bar字段值
    'checkcode': '',  # checkcode字段值
    'account': '',  # account字段值
    'password': '',  # password字段值
    'code': '',  # code字段值
    'mp_56ac2c299c42140f6d81dec2a4ea9a3c_mixpanel':{}
}

# 创建一个配置文件解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

username = config.get('User', 'username')
password = config.get('User', 'password')
md5_password = md5_lower(password)
token={"distinct_id": "4d45490c-9e96-4269-870a-b84d03d26c3b","$device_id": "18f4dee40cb5d2-0c98d78ea54554-26001d51-1fa400-18f4dee40cb5d3","$initial_referrer": "$direct","$initial_referring_domain": "$direct","__mps": {},"__mpso": {},"__mpus": {},"__mpa": {},"__mpu": {},"__mpr": [],"__mpap": [],"$user_id": "4d45490c-9e96-4269-870a-b84d03d26c3b"}

res1 = session.get(url2).text
# print(res1)
html_tree = etree.HTML(res1)

# 使用 XPath 表达式来选择所需的元素
xpath_expression = "/html/body/div[1]/div[2]/div/div/div[1]/div/div/form/div[1]/input[3]"
elements = html_tree.xpath(xpath_expression)
# 输出选择的元素
check_code = etree.tostring(elements[0], pretty_print=True).decode()

# 定义正则表达式模式
pattern = r'value="(\d+)"'
# 使用 re.search() 方法查找匹配的内容
# print(check_code)
match = re.search(pattern, check_code)

if match:
    value = match.group(1)  # 提取匹配到的value值
    print("匹配到check_code的value值为:\n", value)
    data['checkcode'] = value
    data['account'] = username
    data['password'] = md5_password
    data['']=token
    res2 = session.post(url1, data=data, allow_redirects=False)
    # print(res2.text)
    response = session.get(url3, allow_redirects=False)
    print(response.text)

else:
    print("Sorry~未匹配到任何内容check_code")
