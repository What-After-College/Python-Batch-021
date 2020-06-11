import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_id(num):
    df = pd.read_csv("links.csv")
    movie_ids = list(df.imdbId)
    start_index = 0
    end_index = num
    return movie_ids[start_index:end_index]


def scrap(id):
    url = "https://www.imdb.com/title/tt{}/".format(str(id).zfill(7))
    request = requests.request('GET',url)
    soup = BeautifulSoup(request.text, 'html.parser')
    info = soup.find('script', attrs={"type": "application/ld+json"})
    info = str(info)[str(info).find('{'):-9]
    json_data = json.loads(info)
    movie = {
        "name" : json_data["name"],
        "genre" : json_data["genre"],
        "image" : json_data["image"],
        "description" : json_data["description"]
    }
    print(movie['name'],movie['description'])
    return movie


if __name__ == "__main__":
    ids = get_id(3)
    # print(ids)
    for id in ids:
        movie = scrap(id)
