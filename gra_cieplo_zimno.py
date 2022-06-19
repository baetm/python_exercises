import random

guest_num = random.randint(1, 51)
counter = 0

print('Zgadnij liczbę z zakresu 1-50: ')

while True:
    counter += 1
    try:

        while True:
            print(f"Ruch: {counter}")
            number = int(input('Podaj liczbę\n'))
            if number >= 1 and number <= 50:
                break
            else:
                print("Proszę podać liczbę z zakresu 1-50")
                continue

    except ValueError as e:
        print('Podano zły argument. Proszę podać liczbę całkowitą')
        continue

    if number == guest_num:
        print("Zgadłeś")
        counter = 0

        while True:
            question = str(input('Czy chcesz kontynuuować grę? (Y/N)'))

            if question == 'Y':
                print('Losowanie nowej liczby do zgadnięcia')
                guest_num = random.randint(1, 51)
                break
            elif question == 'N':
                exit()
            else:
                print('Podałeś złą literkę')
                continue

    elif number > guest_num:
        print('Za dużo')
        continue
    else:
        print('Za mało')
        continue

print('Koniec programu')
