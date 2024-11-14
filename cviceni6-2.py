import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(prefix):
    # stahneme url + prefix

    result = []
    return result


if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

    # pro prefix "ni" mi to vypise Nissan a Nio
