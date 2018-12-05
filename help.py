import requests
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_capitals_of_states_of_Nigeria'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'TD'})
print table.prettify()