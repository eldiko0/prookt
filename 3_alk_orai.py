"""1. Feladat: Szorzat"""

def number_multiply():
    while True:
        try:
            first_number = float(input("Add meg az első számot: "))
            second_number = float(input("Add meg a második számot: "))

            break

        except ValueError:
            print("Nem számokat adtál meg!")

    return first_number * second_number

print(number_multiply())




"""2. Feladat: Kisebb duplája"""

def smallest_double():
    first_number = float(input("Add meg az első számot: "))
    second_number = float(input("Add meg a második számot: "))

    if first_number <= second_number:
        return float(second_number) * 2
    return float(first_number) * 2
print(f'A két szám közül a kissebb duplája: ', smallest_double())

def smallest_double2(a, b):
    return min(a, b) * 2

while True:
    try:
        a = float(input("Add meg az első számot: "))
        b = float(input("Add meg a második számot: "))
        break

    except ValueError:
        print("Nem számot adtál meg!")

print(f'A kissebb szám kétszerese: ', smallest_double2(a,b))




"""3. Feladat: Páros vagy páratlan?"""

def even_odd(x):
    if x % 2 == 0:
        return True

while True:
    try:
        x = int(input("Adj meg egy számot: "))
        if even_odd(x):
            print(f"({x}) egy páros szám")
        else:
            print(f"{x} egy páratlan szám")
        break
    except ValueError:
        print("Ez nem egy szám, adj meg egy valódi számot!")




"""4. Feladat: Nagyobb triplázva"""

def biggest_triple(x,y):
    bigger = max(x,y)
    return bigger, bigger * 3

while True:
    try:
        x = int(input("Add meg az első számot: "))
        y = int(input("Add meg a második számot: "))
        bigger, tripled = biggest_triple(x,y)
        print(f"A nagyobb szám a(z) {bigger}, melynek a háromszorosa: {tripled}")
        break
    except ValueError:
        print("Ez nem egy szám, adj meg egy valós számot!")




"""+ Feladat: Szóközök nélkül"""

def text_without_spaces(text):
    return text.replace(" ", "")

while True:
        user_text = input("Adj meg egy tetszőleges szövet (mindenképp tartalmaznia kell szóközt!): ")
        if " " in user_text:
            print(f"Így néz ki a szöveg szóközök nélkül: {text_without_spaces(user_text)}")
            break
        else:
            print("A szöveg nem tartalmaz szóközt, kérlek adj meg egy új szöveget!")