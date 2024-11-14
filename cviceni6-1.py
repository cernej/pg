import sys
import requests
from lxml import html

"""
program stahne url a z nej vrati vsechny nadpisy:
<h1>Hlavni nadpis</h1>
<h2>Podnadpis</h2>
<h3>Podpodnadpis</h3>
<h4>Maly nadpis</h4>
<h5>Nejmensi nadpis</h5>
"""
def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []

    response = requests.get(url)
    if response.status_code != 200:
        print('chyba')
        return []
    
    root = html.fromstring(response.content)
    for h in ("h1", "h2", "h3", "h4", "h5"):
        elements = root.xpath(f"//{h}")
        for el in elements:
            nadpis = el.text_content()
            nadpisy.append(nadpis)

    return nadpisy


if __name__ == "__main__":
    url = sys.argv[1]
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print(nadpisy)