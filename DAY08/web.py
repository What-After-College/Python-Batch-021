import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Constitution_of_India"
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())


# print(soup.title)

# print(soup.title.text)

# print(soup.title.parent.name)

# print(soup.p)

# print(soup.a)

# print(soup.find_all('a'))

# for i in soup.find_all('a'):
#     print(i.text)



print(soup.get_text())
