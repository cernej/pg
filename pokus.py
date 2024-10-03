# funkce, ktera vypise Hello World
def hello_world():
    print("Hello World")


# funkce, ktera vypise pozadovany pocet hvezd
def five_stars(limit):
    i = 0
    while i < limit:
        print('*')
        i += 1


# funkce overi zda je number v rozmezi minimum - maximum a vypise textovy vystup
def in_range(number, minimum, maximum):
    if number > minimum and number < maximum:
        print("Number", number, "is in range", minimum, "-", maximum)
    else:
        print("Number", number, "is out of range", minimum, "-", maximum)
    

# funkce vrati nejvetsi cislo z a, b, c
def max_number(a, b, c):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    return c


m = max_number(1, 2, 3)
print(m)
3
m = max_number(100, 10, 1)
print(m)
100
m = max_number(1.1, 1.3, 1.2)
print(m)
1.3