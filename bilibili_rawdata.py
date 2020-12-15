import requests
import re
import sys
import os
from bs4 import BeautifulSoup
import pandas
from time import sleep
import numpy as np
from tqdm import tqdm
import random

_proxies = []
_proxies.append({"http": "http://60.186.42.215:9000"})
_proxies.append({"http": "http://47.107.160.99:8118"})
_proxies.append({"http": "http://182.92.113.148:8118"})
_proxies.append({"http": "http://123.163.121.119:9999"})
_proxies.append({"http": "http://119.119.117.236:9000"})
_proxies.append({"http": "http://123.163.115.143:9999"})
_proxies.append({"http": "http://47.107.160.99:8118"})
_proxies.append({"http": "http://47.106.113.221:8118"})
_proxies.append({"http": "http://60.168.206.27:1133"})
_proxies.append({"http": "http://117.64.234.139:1133"})
_proxies.append({"http": "http://47.106.162.218:80"})
_proxies.append({"http": "http://221.2.155.35:8060"})
_proxies.append({"http": "http://122.226.57.70:8888"})
_proxies.append({"http": "http://115.29.170.58:8118"})
_proxies.append({"http": "http://112.245.17.202:8080"})
_proxies.append({"http": "http://123.57.84.116:8118"})
_proxies.append({"http": "http://175.44.108.153:9999"})
_proxies.append({"http": "http://221.1.205.74:8060"})
_proxies.append({"http": "http://123.57.84.116:8118"})
_proxies.append({"http": "http://112.111.217.66:9999"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://47.106.162.218:80"})
_proxies.append({"http": "http://123.149.141.104:9999"})
_proxies.append({"http": "http://47.106.162.218:80"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://123.57.61.38:8118"})
_proxies.append({"http": "http://161.35.4.201:80"})
_proxies.append({"http": "http://47.106.162.218:80"})
_proxies.append({"http": "http://112.111.217.69:9999"})
_proxies.append({"http": "http://122.226.57.70:8888"})
_proxies.append({"http": "http://182.92.113.148:8118"})
_proxies.append({"http": "http://39.106.223.134:80"})
_proxies.append({"http": "http://183.166.71.170:9999"})
_proxies.append({"http": "http://47.107.160.99:8118"})
_proxies.append({"http": "http://121.8.146.99:8060"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://39.106.223.134:80"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://218.75.102.198:8000"})
_proxies.append({"http": "http://111.229.224.145:8118"})
_proxies.append({"http": "http://180.118.128.124:9000"})
_proxies.append({"http": "http://123.57.61.38:8118"})
_proxies.append({"http": "http://115.29.108.117:8118"})
_proxies.append({"http": "http://47.104.255.144:8118"})
_proxies.append({"http": "http://47.104.255.144:8118"})
_proxies.append({"http": "http://218.75.102.198:8000"})
_proxies.append({"http": "http://182.92.113.148:8118"})
_proxies.append({"http": "http://1.85.5.66:8060"})
_proxies.append({"http": "http://221.236.16.197:8118"})
_proxies.append({"http": "http://111.229.224.145:8118"})
_proxies.append({"http": "http://112.245.17.202:8080"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://110.243.8.110:9999"})
_proxies.append({"http": "http://115.221.244.127:9999"})
_proxies.append({"http": "http://111.160.169.54:41820"})
_proxies.append({"http": "http://59.110.227.129:8081"})
_proxies.append({"http": "http://36.248.129.135:9999"})
_proxies.append({"http": "http://118.126.107.41:8118"})
_proxies.append({"http": "http://218.58.193.98:8060"})
_proxies.append({"http": "http://101.200.36.219:80"})
_proxies.append({"http": "http://118.126.107.41:8118"})
_proxies.append({"http": "http://182.92.113.148:8118"})
_proxies.append({"http": "http://110.243.23.61:9999"})
_proxies.append({"http": "http://60.205.132.71:80"})
_proxies.append({"http": "http://175.42.68.89:9999"})
_proxies.append({"http": "http://115.29.199.16:8118"})
_proxies.append({"http": "http://118.126.107.41:8118"})
_proxies.append({"http": "http://103.39.214.69:8118"})
_proxies.append({"http": "http://47.94.136.5:8118"})
'''
获取随机User-Agent的请求头
'''

# 用户代理User-Agent列表
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

# 随机获取一个用户代理User-Agent的请求头


def get_request_headers():
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        # 'Accept':
        # 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-language': 'zh-CN,zh;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate,br',
        # 'Connection': 'keep-alive',
    }
    return headers


def get_request_proxy():
    proxy = random.choice(_proxies)
    return proxy


url = 'https://www.bilibili.com/video/av'

data = []

timesOnes = 0

links = []
view = []
dm = []
like = []
coin = []
collect = []
share = []
passtime = [0, 0, 0, 0, 0, 0]
ipBlockTime = 0
deleteTime = 0

# strint = 2800000
strint = 3200000
for i in range(2000):
    strint = strint + random.randint(1, 10) * 10
    links.append(url + str(strint))

pbar = tqdm(total=len(links))
for i in range(len(links)):
    pbar.update(1)
    if (i % 10 == 0):
        print("deleteTime: ", deleteTime)
        print("ipBlockTime: ", ipBlockTime)
    try:
        r = requests.get(links[i], headers=get_request_headers()).text
    except:
        continue

    # r = requests.get(links[i], headers=get_request_headers()).text
    # r = requests.get('https://www.bilibili.com/video/av1000200',
    # headers=get_request_headers()).text

    # r = requests.get(
    # links[i],
    # headers=get_request_headers(),
    # proxies=get_proxy_headers()
    # ).text
    soup = BeautifulSoup(r, 'lxml')

    if len(soup.find_all('div', class_='check-input')) != 0:
        ipBlockTime += 1
        continue

    elif len(soup.find_all('div', class_='error-body')) != 0:
        deleteTime += 1
        continue

    if (len(soup.find_all('span', class_='view')) != 0):
        try:
            view.append(soup.find('span', class_='view')["title"][4:])
        except:
            passtime[0] += 1
            pass
        try:
            dm.append(soup.find('span', class_='dm')["title"][7:])
        except:
            passtime[1] += 1
            pass
        try:
            like.append(soup.find('span', class_='like')["title"][3:])
        except:
            passtime[2] += 1
            pass
        count = [0, 0, 0]
        try:
            for i in soup.find('span', class_='coin'):
                count[0] = count[0] + 1
                if (count[0] == 4):
                    coin.append(i.strip())
        except:
            passtime[3] += 1
            pass
        try:
            if (soup.find('span', class_='collect') != None):
                for i in soup.find('span', class_='collect'):
                    count[1] = count[1] + 1
                    if (count[1] == 4):
                        collect.append(i.strip())
            else:
                for i in soup.find('span', class_='collect on'):
                    count[1] = count[1] + 1
                    if (count[1] == 4):
                        collect.append(i.strip())
        except:
            passtime[4] += 1
            pass
        try:
            for i in soup.find('span', class_='share'):
                count[2] = count[2] + 1
                if (count[2] == 2):
                    share.append(i.strip())
        except:
            passtime[5] += 1
            pass
        sleep(1)
pbar.close()
df0 = pandas.DataFrame(view)
df1 = pandas.DataFrame(dm)
df2 = pandas.DataFrame(like)
df3 = pandas.DataFrame(coin)
df4 = pandas.DataFrame(collect)
df5 = pandas.DataFrame(share)
df6 = pandas.DataFrame(passtime)
df0.to_csv('view.csv', mode='a', header=False)
df1.to_csv('dm.csv', mode='a', header=False)
df2.to_csv('like.csv', mode='a', header=False)
df3.to_csv('coin.csv', mode='a', header=False)
df4.to_csv('collect.csv', mode='a', header=False)
df5.to_csv('share.csv', mode='a', header=False)
df6.to_csv('passtime.csv', mode='a', header=False)
