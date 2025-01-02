# napiste funkci, ktera podle typu "+"", "-", "*", "/" provede operaci a vrati vysledek

def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
        matematicka_operace = a + b
    elif typ == "-":
        matematicka_operace = a - b
    elif typ == "*":
        matematicka_operace = a * b
    elif typ == "/":
        matematicka_operace = a / b
    return matematicka_operace

if __name__ == "__main__":
    operace("+", 1, 2)  # 3
    operace("-", 2, 1)  # 1
    operace("*", 0, 5)  # 0
    operace("/", 4, 2)  # 2