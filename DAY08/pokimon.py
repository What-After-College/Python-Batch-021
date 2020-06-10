import requests
from matplotlib import pyplot as plt

def url_builder(name):
    return 'https://api.pokemontcg.io/v1/cards?name=' + name



def img_url(response_data):
    cards = response_data['cards']
    url_for_img = cards[0]["imageUrl"]
    return url_for_img


def save_img(response_2):
    with open('poke.png','wb') as f:
        for item in response_2.iter_content():
            f.write(item)


    # f = open('abc.txt','r+')
    # f.write('')
    # f.close()

def show_img():
    img_data = plt.imread('poke.png')
    plt.imshow(img_data)
    plt.show()



if __name__ == "__main__":
    name = input("Enter the name of pokemon : ")
    url = url_builder(name)

    response = requests.request('GET', url)
    response_data = response.json()

    url_for_img = img_url(response_data)
    response_2 = requests.request('GET', url_for_img)

    save_img(response_2)
    show_img()



