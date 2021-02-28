import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/TSLA/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find_all('div',{'class:','My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
print(price)

def priceTracker():
  url = "https://finance.yahoo.com/quote/TSLA/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  price = soup.find_all('div',{'class:','My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
  return price
  
while True:
  print("The Current Tesla Price is: " + priceTracker() + "!")
  