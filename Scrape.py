from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://finance.yahoo.com/quote/%5EIXIC/components?p=%5EIXIC"

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.tbody.findAll('tr', {'class': 'BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s)'})

headersTag = page_soup.findAll('tr', {'class': 'Bdc($finLightGray) C($c-fuji-grey-j) Fz(xs) Ta(end)'})

headersArray = []

tempStockArray = []

filename = "NASDAQ1.csv"

f = open(filename, "w")

for i in headersTag:
    for j in i:
        headersArray.append(j.text)
headersArray = ",".join(headersArray)
f.write(headersArray + "\n")

for i in containers:
    for j in i:
        tempStockArray.append(j.text.replace(",", "."))
        if len(tempStockArray) == 6:
            tempStockArray = ",".join(tempStockArray)
            f.write(tempStockArray + "\n")
            tempStockArray = []
            break

f.close()
open(filename)