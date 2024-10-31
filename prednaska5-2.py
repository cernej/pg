
if __name__ == "__main__":

    fp = open("soubor2.txt", "r")

    fp.seek(9)

    znak = fp.read(2)

    print(znak)

    print(fp.tell())

    fp.close()