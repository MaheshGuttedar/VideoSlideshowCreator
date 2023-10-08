import requests
from bs4 import BeautifulSoup
url = "https://www.w3schools.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title').text
links = soup.find_all('a')
print(title)
for link in links:
    print(link['href'])
