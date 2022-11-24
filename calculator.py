import math


def adunare(x, y):
    return x + y


def scadere(x, y):
    return x - y


def inmultire(x, y):
    return x * y


def impartire(x, y):
    return x / y


def factorial(x):
    return math.factorial(x)


def logaritm(x, y):
    return math.log(x, y)


print('Alege ce vrei sa calculezi: ')
print('1. Adunare')
print('2. Scadere')
print('3. Inmultire')
print('4. Impartire')
print('5. Factorial')
print('6. Logaritm')

run = True

while run:
    alegere = input('Alege: ')
    if alegere in ('1', '2', '3', '4'):
        n1 = float(input('Alege primul numar: '))
        n2 = float(input('Alege al doilea numar: '))
    elif alegere in '5':
        n = int(input('Alege un numar: '))
    elif alegere in '6':
        n1 = float(input('Alege numarul: '))
        n2 = float(input('Alege baza: '))
    if alegere == '1':
        print(f'{n1} + {n2} =', adunare(n1, n2))
    elif alegere == '2':
        print(f'{n1} - {n2} =', scadere(n1, n2))
    elif alegere == '3':
        print(f'{n1} * {n2} =', inmultire(n1, n2))
    elif alegere == '4':
        print(f'{n1} / {n2} =', impartire(n1, n2))
    elif alegere == '5':
        print(factorial(n))
    elif alegere == '6':
        print(logaritm(n1, n2))
    else:
        break
