import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(abrakadabra):
    # stahneme url + prefix

    response = requests.get(url + abrakadabra)
    if response.status_code != 200:
        print('chyba')
        return []
    
    data = json.loads(response.content)

    result = []

    brands = data['brands']
    for brand in brands:
        result.append(brand['name'])
    
    return result


if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

    # pro prefix "ni" mi to vypise Nissan a Nio
