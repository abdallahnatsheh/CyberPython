import requests
from bs4 import BeautifulSoup

url="https://www.pythonforbeginners.com/"

data = requests.get(url).text  # use it to print the html code
#print(data)

soup = BeautifulSoup(data)    #scrapping what i need from the html code
for link in soup.find_all('a'):
    print(link.get('href'))

