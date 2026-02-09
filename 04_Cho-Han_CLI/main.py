import random

print(f"CHO-HAN")

print(f"Ile razy chcesz rozegrać grę?")
liczba_gier = int(input())

for x in range(liczba_gier):
    print(f"Co obstawiasz, liczby parzyste czy nieparzyste? Wciśnij 'p' dla parzystych lub 'n' dla nieparzystych")

    obstawienie_gracza = str(input())
    kostka_pierwsza = random.randint(1, 6)
    kostka_druga = random.randint(1, 6)
    suma_kostek = kostka_pierwsza + kostka_druga

    print(f"Kostka pierwsza: {kostka_pierwsza}")
    print(f"Kostka druga: {kostka_druga}")
    print(f"Suma kostek: {suma_kostek}")

    if (suma_kostek % 2 == 0) and (obstawienie_gracza == "p") or (suma_kostek % 2 !=0) and (obstawienie_gracza == "n"):
        print("Wygrałeś!")
    elif (suma_kostek % 2 == 0) and (obstawienie_gracza == "n") or (suma_kostek % 2 !=0) and (obstawienie_gracza == "p"):
        print("Przegrałeś!")
