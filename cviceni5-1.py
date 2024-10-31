import sys
import csv

def nacti_csv(soubor):
    data = []
    # nacist data ze souboru
    return data


def spoj_data(data1, data2):
    if not data1 or not data2:
        return data1 if data1 else data2

    # Získání hlaviček a dat z obou souborů
    headers1, *rows1 = data1
    headers2, *rows2 = data2

    # Vytvoření slovníků pro snadné vyhledávání
    data_dict1 = {tuple(row[:2]): row[2:] for row in rows1}
    data_dict2 = {tuple(row[:2]): row[2:] for row in rows2}

    # Spojení hlaviček a inicializace výsledného seznamu
    all_headers = list(dict.fromkeys(headers1 + headers2))  # Eliminuje duplicity a udržuje pořadí
    result_data = [all_headers]

    # Spojení dat
    all_keys = set(data_dict1.keys()).union(set(data_dict2.keys()))

    for key in all_keys:
        new_row = list(key) + [data_dict1.get(key, [''])[0]] + [data_dict2.get(key, [''])[0]]
        result_data.append(new_row)

    return result_data


def zapis_csv(soubor, data):
    pass


if __name__ == "__main__":

    soubor1 = sys.argv[1]
    soubor2 = sys.argv[2]
    csv_data1 = nacti_csv(soubor1)
    csv_data2 = nacti_csv(soubor2)
    vysledna_data = spoj_data(csv_data1, csv_data2)
    zapis_csv("vysledny_excel.csv", vysledna_data)
