import scrapy
import sys
import requests
from unidecode import unidecode
from scrapy.selector import Selector
from scrapy import Selector
import csv

url='https://quotes.toscrape.com/page/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
session = requests.Session()
list1=[]
for i in range(1,11):
    page_url=url+str(i)+"/"
    list1.append(page_url)
print(list1)
Quotes=[]
list3=[]
for i in list1:
    response=requests.get(i,headers=headers)
    response1=session.get(i,headers=headers)
    cookies = session.cookies.get_dict()
    list3.append(response1.status_code)

    # print(response.status_code)
    selectors=Selector(text=response.text)
    quotes = selectors.css('div.quote')
    for quote in quotes:
        text=quote.css('span.text::text').get()
        author=quote.css('small.author::text').get()
        tags = quote.css('div.tags a.tag::text').getall()
        Quotes.append({
            'author': author,
            'tags': ', '.join(tags),
            'text': text,
            })
        
    
print(Quotes)
print("cookies:",cookies)

with open('data.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'])
    writer.writeheader()
    writer.writerows(Quotes)
print("Data saved to data.csv")



# login 
# loginurl='https://quotes.toscrape.com/login'
# client = requests.session()
# client.get(loginurl)
# if 'csrftoken' in client.cookies:
#     csrftoken = client.cookies['csrftoken']
# else:
#     csrftoken = client.cookies['csrf']
# payload = {'csrf_token': csrftoken,
#         'username': 'admin',
#         'password': 'admin'
#     }
# with requests.Session() as s:
#     p = s.post('ttps://quotes.toscrape.com/login', data=payload)
#     print(p.text)

#     r = s.get('A protected web page URL')
#     print(r.text)




