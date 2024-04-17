import requests , bs4
import time
for i in range(1 ,30):
 
 link="https://www.1point3acres.com/bbs/tag/meta-399-"+ str(i) +".html"
 res=requests.get(link) 
 res.raise_for_status()
 demo=bs4.BeautifulSoup(res.text , "html.parser")
 x = demo.select("b")
 
 print(x)
 time.sleep(5)
