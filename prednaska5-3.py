import csv


data = [
    ["jmeno", "prijmeni", "vek"],
    ["Tomas", "Novak", 20],
    ["Jan", "Dvorak", 25]
]


if __name__ == "__main__":

    with open("excel.csv", "w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)