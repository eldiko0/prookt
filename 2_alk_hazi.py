"""1. Magánhangzó számláló"""

def vowel_counter():

    text = input("Adj meg egy szöveget: ")

    vowels = "aáeéiíoóöőuúüű"
    count = 0

    for text_vowels in text.lower():
        if text_vowels in vowels:
            count += 1

    print(f"{count} magánhangzó található.")

vowel_counter()




"""2. Számjegyek összege"""

def add_number_parts():
    number = input("Adj meg egy számot: ")
    total = 0

    for digit in number:
        total += int(digit)

    print(f"A számjegyek összege: {total}")

add_number_parts()




"""3. Szavak visszafelé"""

def words_backward ():
    sentence = input("Írj be egy mondatot: ")
    words = sentence.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)
    print(result)
words_backward()




"""4. Leggyakoribb szám"""

def most_common_number():

    numbers = []

    while True:
        added_numbers = input("Írj be egy számot: ")
        if added_numbers == "":
            break

        numbers.append(int(added_numbers))

    most_common = max(numbers, key=numbers.count)
    print(f"A leggyakoribb szám: {most_common}")

most_common_number()




"""5. Egyszerű jelszó-ellenőrző"""

def password_checker ():

    while True:

        password = input("Adj meg egy jelszót! (Tartalmazzon legalább egy nagy-, egy kis betűt és egy számot!")
        has_lowercase = any(p.islower() for p in password)
        has_uppercase = any (p.isupper() for p in password)
        has_number = any (p.isdigit() for p in password)

        if has_lowercase and has_uppercase and has_number:
            print("A jelszó megfelelő!")
            break

        else:
            print("A jelszó nem megfelelő, próbáld újra!")

password_checker()