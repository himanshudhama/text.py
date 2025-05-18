import requests
from unidecode import unidecode
from scrapy.selector import Selector

url='https://www.airbnb.co.in/s/Dehradun--Uttarakhand/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2025-05-01&monthly_length=3&monthly_end_date=2025-08-01&price_filter_input_type=2&channel=EXPLORE&place_id=ChIJr4jIVsMpCTkRmYdRMsBiNUw&location_bb=QfM7ykKcN8ZB8fkrQpvZxg%3D%3D&acp_id=fb62a1ea-3805-48e3-859c-043b4e15aa50&date_picker_type=calendar&checkin=2025-04-23&checkout=2025-04-25&source=structured_search_input_header&search_type=autocomplete_click'
response=requests.get(url)
print(response.status_code)
# with open("airbnb.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
list1=[]
hxs=Selector(text=response.text)
hrefs = hxs.xpath("//a[@class][@href]/@href").getall()
list1.append(hrefs)
print(list1)



# list1=[]
# href=hxs.xpath('.//a[@href]').extract()
# list1.append(href)
# print(len(list1))