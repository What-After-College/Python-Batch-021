import requests

url = "https://sv443.net/jokeapi/v2/joke/Miscellaneous,Dark"


response = requests.request("GET", url)


# print(response)

data = response.json()

# print(response.text.encode('utf8'))
print(data)
# print(data['category'])