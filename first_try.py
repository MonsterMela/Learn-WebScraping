from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as


url = "https://www.datacamp.com/community/tutorials/web-scraping-using-python"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
title = soup.title
#print(soup.prettify())
#print(title)
#text = soup.get_text()
#print(soup.text)


#print(soup.find_all("a"))

all_links = soup.find_all("a")
#for link in all_links:
 #   print(link.get("href"))
rows = soup.find_all("tr")

for row in rows:
    row_td = row.find_all('td')
   #print(row_td)
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    #print(cleantext)
    df = pd.DataFrame(cleantext)
    df.head(10)
#type(row_td)