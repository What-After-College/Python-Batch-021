import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_id(num=30, page=1):
    df = pd.read_csv("links.csv")
    movie_ids = list(df.imdbId)
    start_index = (page - 1)*num
    end_index = start_index + num
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
    return movie

def get_movie_details():
    ids = get_id(10)
    lis = []
    for id in ids:
        movie = scrap(id)
        lis.append(movie)
    return lis



if __name__ == "__main__":
    # ids = get_id(3)
    # # print(ids)
    # for id in ids:
    #     movie = scrap(id)
    lis = get_movie_details()
    print(lis)
