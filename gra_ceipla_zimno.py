import random

guest_num = random.randint(1, 51)
counter = 0

print('Zgadnij liczbę z zakresu 1-50: ')

while True:
    counter += 1
    try:
        temp = int(input('Podaj liczbę\n'))
    except:
        print('Proszę podać liczbę całkowitą')
        continue

    if temp == guest_num:
        print("Zgadełeś")
        break
    if temp > guest_num:
        print('Za dużo')
        continue
    else:
        print('Za mało')
        continue

print('Koniec programu')
