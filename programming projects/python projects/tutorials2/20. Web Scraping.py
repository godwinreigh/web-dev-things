import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.weather-forecast.com/locations/Daet/forecasts/latest')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('a'))
week = soup.find(id=)



