from random import randint

fegyver = ['kő', 'papír', 'olló']

while True:
    computer = fegyver[randint(0,2)]
    játékos = input('kő, papír vagy olló (vagy vége) ').lower()
    if játékos == 'vége':
        print('Vége a játéknak.')
        break
    elif játékos == computer:
        print('Döntetlen!')
    elif játékos == 'kő':
        if computer == 'papír':
            print('Vesztettél! A(z)', computer, 'üti a(z)', játékos, '-t')
        else:
            print('Nyertél! A(z)', játékos, 'üti a(z)', computer, '-t')
    elif játékos == 'papír':
        if computer == 'olló':
            print('Vesztettél! A(z)', computer, 'üti a(z)', játékos, '-t')
        else:
            print('Nyertél! A(z)', játékos, 'üti a(z)', computer, '-t')
    elif játékos == 'olló':
        if computer == 'kó':
            print('Vesztettél! A(z)', computer, 'üti a(z)', játékos, '-t')
        else:
            print('Nyertél! A(z)', játékos, 'üti a(z)', computer, '-t')
    else:
        print('Ellenőrizd, amit írtál...')