from cviceni4_jaccard import jaccardova_vzdalenost_mnozin
from cviceni4_levenstein import levensteinova_vzdalenost


def deduplikace_dotazu2(dotazy):
    """
    tato funkce spocita jaccardovu vzdalenost a levensteinovu vzadelnost a vyradi z seznamu dotazy, polozky, ktere budou mit
    jaccardovu vzdalenost mensi nez 0.5 a levensteinovu vzdalenost <= 1
    """
    results = [dotazy.pop(0)]
    for dotaz1 in dotazy:
        remove = False
        for dotaz2 in results:
            jaccard = jaccardova_vzdalenost_mnozin(dotaz1["serp"], dotaz2["serp"])
            levenstein = levensteinova_vzdalenost(dotaz1["dotaz"], dotaz2["dotaz"])
            if jaccard < 0.5 or levenstein <= 1:
                remove = True
        if not remove:
            results.append(dotaz1)
    return results


def deduplikace_dotazu(dotazy):
    i = 0
    while i < len(dotazy):
        j = i + 1
        while j < len(dotazy):
            jaccard = jaccardova_vzdalenost_mnozin(dotazy[i]["serp"], dotazy[j]["serp"])
            levenstein = levensteinova_vzdalenost(dotazy[i]["dotaz"], dotazy[j]["dotaz"])
            if jaccard < 0.5 or levenstein <= 1:
                dotazy.pop(j)
            else:
                j += 1
        i += 1
    return dotazy


if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))

