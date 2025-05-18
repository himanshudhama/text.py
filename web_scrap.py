import requests
import csv
from unidecode import unidecode
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import pdfkit
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmtopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
response = requests.get('https://quotes.toscrape.com/')
print(response)
if response.status_code == 200:
    page_link="https://quotes.toscrape.com/page"
    list1=[]
    for i in range(1,11):
        list1.append("https://quotes.toscrape.com/page"+"/"+str(i)+"/")

    all=[]
    for i in list1:
        soup = BeautifulSoup(response.text, 'html.parser')
        quote_blocks = soup.find_all('div', class_='quote')
        for blocks in quote_blocks:
            quotes = soup.find_all('span', class_='text')
            authors = soup.find_all('small', class_='author')
            tags = soup.find_all('a', class_='tag')
        
        for quote, author,tag in zip(quotes, authors,tags):
            all.append({
                "Quote": quote.text,
                "Author": author.text,
                "tags":tag.text
            })
    for items in all:
        print(all)
    
# Save each page as PDF
for i in range(1, 11):
    html_file = f"page_{i}.html"
    pdf_file = f"page_{i}.pdf"
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()
    pdfkit.from_string(html_content, pdf_file, configuration=config)
    print(f"Converted {html_file} to {pdf_file}")

        # html_file = f"page_{i}.html"
        # output_file = f"page_{i}.pdf"

       
    #     pdfkit.from_file(html_file,output_file, configuration=config)
    #     print(f"Saved: {output_file} from html:{html_file}")
    # else:
    #     print(f"Failed to fetch {url}")