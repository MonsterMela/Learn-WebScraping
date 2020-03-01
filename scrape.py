from bs4 import BeautifulSoup
#from url import urlopen
import requests
"""
url = "https://www.datacamp.com/community/tutorials/web-scraping-using-python"
html = urlopen(url)
print(html)
"""
soup = BeautifulSoup(requests.get("https://www.amazon.in/s?i=electronics&bbn=1389396031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389375031%2Cn%3A1389396031%2Cp_72%3A1318477031%2Cp_89%3ALG%7CSamsung%7CSony%2Cp_n_feature_six_browse-bin%3A11962317031&dc&fst=as%3Aoff&qid=1582542969&rnid=11962314031&ref=sr_nr_p_n_feature_six_browse-bin_3").text, 'lxml')
print(soup.prettify())

#info = soup.find('div', class_ = "sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28")
#print(soup.prettify())


