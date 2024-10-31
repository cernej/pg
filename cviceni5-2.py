import sys

def read_data(file_name):
    data = []
    fp = open(file_name, "r")
    for line in fp:
        data.append(line.strip().split(','))
    return data


def write_data(file_name, data):
    with open(file_name, "w") as fp:
        for row in data:
            line = ','.join(row) + '\n'
            fp.write(line)


if __name__ == "__main__":

    try:
        file = sys.argv[1]
        data = read_data(file)
        write_data("excel3.csv", data)
    except Exception as e:
        print(f"Nastala chyba: {e}")
