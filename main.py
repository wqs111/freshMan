'''
爬虫开发主体完成

*筛选文章种类
*保存文件
'''


add

import requests
from bs4 import BeautifulSoup

num = 3  #在此处填写需要爬取的文章数量

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"

}
baseUrl = "https://www.aisixiang.com/data/"
for i in range(num):
    print("开始访问第{}篇文章，请稍后...".format(i+1))
    webNum = "133792"
    a = int(webNum)
    a = a+i

    FinalURL = "https://www.aisixiang.com/data/{}.html".format(a)
    response = requests.get(FinalURL, headers=headers)
    print(FinalURL)
    if response.ok:
        print("OK")
    else:
        print("FAIL")

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    all_p = soup.find_all("p")
    for p in all_p:
        print(p.string)

    print("-" * 8, "*" * 8, "-" * 8)



