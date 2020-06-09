import requests

url = "https://currencyapi.net/api/v1/rates?key=NXtUyotjncqJie5GKVEjlBi6FYfjgQuQyjjL&base=USD"


response = requests.request("GET", url)

response_data = response.json()

# print(response.text.encode('utf8'))

rates = response_data['rates']

print("1 USD is equals to ",rates['INR'],"INR")