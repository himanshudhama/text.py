import requests
import csv
from scrapy.selector import Selector   
from unidecode import unidecode
list1=['sports','business']      
url = "https://timesofindia.indiatimes.com/"
list2=[]
for i in list1:
    list2.append(url+i)
print(list2)
list3=[]
list4=[]
for i in list2:
    response = requests.get(i)
    print(response.status_code)
    open("temp.html","w").write(unidecode(response.text))
    hxs=Selector(text=response.text)
    if 'business' in i:
         business_headline=hxs.xpath('.//figcaption[@class]//text()').extract()
         list3.append(business_headline)
    if 'sports' in i:
        Sports_headline=hxs.xpath('.//div[@class="WavNE  "]//text()').extract()
        list4.append(Sports_headline)
writer=csv.writer(open("News.csv","w"))
Headers=['Business','Sports']
writer.writerow(Headers)
writer.writerow([list3,list4])

print(list3)
print(list4)

