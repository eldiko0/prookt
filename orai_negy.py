"""1. Feladat: Megszámlálás tétele"""
def score_counter():

    counter = [0] * 10

    while True:
        user_score = input("Add meg a pontod: ")
        if user_score == "":
            break
        try:
            score = int(user_score)
            if 1 <= score <= 10:
                counter[score-1] +=1
            else:
                print("Nem 1 és 10 közötti számot adtál meg!")
        except ValueError:
            print("Ez nem egy szám, írj be egy valós számot!")

    for i in range(10):
        print(f"{i + 1} pontos: {counter[i]} db")



"""2. Feladat: Szökőév"""


def leap_year():

    while True:
        user_year = input("Adj meg egy évet: ")

        try:
            year = int(user_year)
            if year % 4 == 0 and year % 100 != 0:
                print(f"{year} egy szökőév!")
            elif year % 400 == 0:
                print(f"{year} egy szökőév!")
            else:
                print(f"{year} nem szökőév!")

        except ValueError:
            print("Ez nem egy szám, írj be egy valós számot!")



"""3. Feladat: megértés, függvények"""

"""szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]
szum = 0
db = 0

for x in szamok:
    szum += x
    db += 1

atlag = szum / db
szurt = []

for x in szamok:
    if x < atlag:
        szurt.append(x)

print(szurt)"""

def get_sum(szamok):
    return int(sum(szamok))

def get_pcs (szamok):
    return len(szamok)

def get_avg(szamok):
    return get_sum(szamok) / get_pcs(szamok)

def smaller_than_avg (szamok):
    average = get_avg(szamok)
    return [x for x in szamok if x < average]

def list_analysis():
    szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65, 69, 83, 39]

    print("A lista összege:", get_sum(szamok))
    print("A lista ennyi darabból áll:", get_pcs(szamok))
    print("A lista átlaga:", get_avg(szamok))
    print("Átlagnál kisebbek számok a listában:", smaller_than_avg(szamok))



"""4. Feladat: betücsere"""

def letter_change(user_text, which_letter, to_letter):
    try:
        if int(which_letter) < 1 or int(which_letter) > len(user_text):
            raise ValueError("Helytelenül adtad meg a betű számát!")
        user_text_list = list(user_text)
        user_text_list[int(which_letter) - 1] = to_letter
        return "".join(user_text_list)
    except ValueError:
        return "Hibás adatokat adtál meg!"

def user_rqst_change():
    user_text = input("Adj meg egy szöveget: ")
    which_letter = input("Hanyadik karaktert szeretnéd cserélni? ")
    to_letter = input("Milyen betűre szeretnéd cserélni? ")

    print("Eredmény:", letter_change(user_text, which_letter, to_letter))

def main():
    score_counter()
    leap_year()
    list_analysis()
    user_rqst_change()
    pass

if __name__ == "__main__":
    main()