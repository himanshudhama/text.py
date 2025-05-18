import requests
import csv
from unidecode import unidecode
#from parsel import Selector
from scrapy.selector import Selector
response = requests.get('https://books.toscrape.com/')
# print(response.status_code)
# with open('himanshu.html','w') as file:
#     file.write(response.text)
html_content=open("himanshu.html","r").read()
hxs=Selector(text=html_content)
data=[]

all_a_tags=hxs.xpath("//a[@href][@title]")
for a_tag in all_a_tags:
    href=''.join(a_tag.xpath('.//@href').extract())
    href="https://books.toscrape.com/"+href
    
   
    title=''.join(a_tag.xpath('.//@title').extract())
    
    text=''.join(a_tag.xpath('.//@text()').extract())
    tuple=(href,title,text)
    data.append(tuple)
# print(data)
# import pdb;pdb.set_trace()
all_data=[]
writer=csv.writer(open("csv_file.csv","w"))
zz=0
for z in data:
    href=z[0]
    zyv=requests.get(href)
    dst=Selector(text=zyv.text)
    product_information=dst.xpath(".//table//tr")
    info={}
    for product in product_information:
        key=product.xpath('.//th//text()').extract()[0]
        value=product.xpath('.//td//text()').extract()[0]
        info[key]=value
    print(info)

    productinformation=''.join(dst.xpath('.//div[@id="product_description"]//following-sibling::p//text()').extract())
    info['productinformation']=productinformation
    print(info)
    if zz==0:
        headers=list(info.keys())
        writer.writerow(headers)
        zz+=1
    
    writer.writerow([unidecode(info[h]) for h in headers])



"""
    csv_filename="booktoscrape.csv"
    field_name=info[key]
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_name)
        writer.writeheader()  # Write header row
        writer.writerows(info)
    
    # price=
    # produc_des=
    # tale_info={}
    # all_tr=hxs1.xpath('.//table//tr')
    # for tr in all_tr:
    #     key=tr.xpath('.//th//text()').e
    #     value=key
    #     table_info[key]=value

"""