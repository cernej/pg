import sys
import csv

def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data.append(row)
    return data


def spoj_data(*data):
    {
        "Novak": {
            "jmeno": "Jan",
            "prijmeni": "Novak",
            "vek": "20",
            "rocnik": 1
        }
    }

    vysledek = {}

    keys = set()
    for d in data:
        for k in d[0]:
            keys.add(k)
        for v in d[1:]:

    


    print(keys)

    tmp = {}
    for d in data:
        for v in zip(*d):
            tmp[v[0]] = v[1:]
    vysledek = []
    vysledek.append(list(tmp.keys()))
    for v in zip(*tmp.values()):
        vysledek.append(v)
    
    return vysledek


# def spoj_data(*data):
#     return [['jmeno', 'prijmeni', 'vek', 'rocnik'], ['Tomas', 'Novak', '20', '1'], ['Jan', 'Dvorak', '25', '2'],  ['Alice', 'Novotna', '', '1']]


def zapis_csv(soubor, data):
    with open(soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Zadej 2 vstupni soubory typu csv")
    except FileNotFoundError:
        print("Soubor neexistuje")
