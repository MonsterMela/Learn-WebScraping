from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re


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
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
#print(list_rows)
    #type(clean2)
df = pd.DataFrame(list_rows)
#print(df.head(10))
df1 = df[0].str.split(',', expand=True)
df1[0] = df1[0].str.strip('[')
print(df1.head(10))
#print(df1.head(10))
#type(row_td)