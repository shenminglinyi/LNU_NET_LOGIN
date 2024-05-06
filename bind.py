# -*- coding: utf-8 -*-
# @Time    : 2022/9/25 13:21
# @Author  : Linyi
# @Site    :
# @File    : login.py
# @Software: PyCharm


import requests
import configparser
import os

# 创建一个配置文件解析器对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 读取配置文件中的值
ip = config.get('Network', 'IP')
v = config.get('Network', 'V')
jsessionid = config.get('Cookies', 'JSESSIONID')
username = config.get('User', 'username')
password = config.get('User', 'password')

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Host": "202.118.49.94:801",
    "Referer": "http://202.118.49.94/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
}

# url = f"http://202.118.49.94:801/eportal/portal/login?callback=dr1003&login_method=1&user_account={username}&user_password={password}&wlan_user_ip=" + ip + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=1&lang=zh-cn&v=" + v + "&lang=zh"
# 这个是简单版，失效可以尝试上边复杂的

url = f"http://202.118.49.94:801/eportal/portal/login?callback=dr1003&login_method=1&user_account={username}&user_password={password}"

# # 指定某个域名不用代理去处理
# os.environ['NO_PROXY'] = url


data = f"callback=dr1003&login_method=1&user_account={username}&user_password={password}&wlan_user_ip=" + ip + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.2&terminal_type=2&lang=zh-cn&v=" + v + "&lang=zh"
# res=requests.post(url=url,data=data,headers=headers)
res = requests.get(url=url)
print(res.text)
