import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(prefix):
    # stahneme url + prefix
    response = requests.get( ... )
    # stahneme json
    json_data = response.json()
    # zkonvertujeme na data
    json.loads()

    brands = []

    # vytahneme nazvy brandu ["brans"]["name"]

    return brands


if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

