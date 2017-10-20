import requests
import sys
from bs4 import BeautifulSoup
placename = ['泉州港','江洋港','天涯盐场','钱塘港','望海岬','灵鹿岛','沧浪岛',
            '幽灵岛','宝矿山','琅嬛福地','大沧海','东海玉涡']
## print(sys.argv[1])
tempurl = "http://wuxia.duowan.com/1707/363805694444_"
for x in range(2,14):
    url = tempurl + str(x)+".html"
    re = requests.get(url)
    re.encoding='utf-8'
    soup = BeautifulSoup(re.text,"html.parser")
## print(soup.prettify())
    for link in soup.find_all("img"):
        src = link.get('src')

        ## 3-13 alt = 天刀最新版本航海图鉴坐标 及收藏攻略
        ## 2 alt = 泉州港图鉴坐标
        if((src.endswith('.jpg') or src.endswith('.JPG'))
        and (link.get('alt').startswith('泉州港图鉴坐标')
        or link.get('alt').startswith('天刀最新版本航海图鉴坐标 及收藏攻略'))):

            print(link.get('src'))
            imgre = requests.get(src)
            with open(placename[x-2]+'.jpg','wb') as file:
                file.write(imgre.content)
            file.close()

## print(re.text)
