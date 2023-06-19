#Request  module is used when you want send some url to  and also used for web scrapping
import requests
from bs4 import BeautifulSoup 
req=requests.get("https://www.google.com/")  #get request is used to get the data
soup=BeautifulSoup(req.text,'html.parser')
print(soup.prettify())

#similarly you can use a post request 
#when you do scrapping scrapping is necessary 




