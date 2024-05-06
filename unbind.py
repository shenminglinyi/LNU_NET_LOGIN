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
IP = config.get('Network', 'IP')
V = config.get('Network', 'V')
jsessionid = config.get('Cookies', 'JSESSIONID')
username = config.get('User', 'username')
password = config.get('User', 'password')

# url = f"http://202.118.49.94:801/eportal/portal/mac/unbind?callback=dr1003&user_account={username}&wlan_user_mac=000000000000&wlan_user_ip=" + IP + "&jsVersion=4.2&v=" + V + "&lang=zhַ"
# 这个是简单版，失效可以尝试上边复杂的
url = f"http://202.118.49.94:801/eportal/portal/mac/unbind?callback=dr1003&user_account={username}ַ"

# 指定某个域名不用代理去处理
os.environ['NO_PROXY'] = url

res = requests.get(url=url)
print(res.text)
