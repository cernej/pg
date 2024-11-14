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
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'nastala chyba, nepodarilo se pripojit na {url}')
        return []
    if response.status_code != 200:
        print(f'nastala chyba, http code: {response.status_code}')
        return []
    
    root = html.fromstring(response.content)
    for h in ("h1", "h2", "h3", "h4", "h5"):
        for h1 in root.xpath(f"//{h}"):
            h1_text = h1.text_content().strip()
            if h1_text:
                nadpisy.append(h1_text)

    return nadpisy


if __name__ == "__main__":
    url = sys.argv[1]
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print(nadpisy)