import time, random

def dibTablero(tab):
    print('\nRealizando jugada..\n')
    time.sleep(0.5)
    print('\nJugada Realizada\n')
    print('\n ',tab[2][0],'|',tab[2][1],'|',tab[2][2],' \n',
    '-----------\n',
    '',tab[1][0],'|',tab[1][1],'|',tab[1][2],' \n',
    '-----------\n',
    '',tab[0][0],'|',tab[0][1],'|',tab[0][2],' \n')

def hacerJugada(tab, pos, jugador):
    if jugador:
        simbolo = 'X'
    else:
        simbolo = 'O'
    if pos >= 1 and pos <= 3 and tab[0][pos-1] == ' ':
        tab[0][pos-1] = simbolo
        return 0
    elif pos >= 4 and pos <= 6 and tab[1][pos-4] == ' ':
        tab[1][pos-4] = simbolo
        return 0
    elif pos >= 7 and pos <= 9 and tab[2][pos-7] == ' ':
        tab[2][pos-7] = simbolo
        return 0
    else:
        return '\nMovimiento inválido, porfavor vuelve a jugar.\n'

def ganador(tab):
    for simbolo in ['X','O']:
        fila_0 = tab[0][0] == simbolo and tab[0][1] == simbolo and tab[0][2] == simbolo
        fila_1 = tab[1][0] == simbolo and tab[1][1] == simbolo and tab[1][2] == simbolo
        fila_2 = tab[2][0] == simbolo and tab[2][1] == simbolo and tab[2][2] == simbolo
        col_0 = tab[0][0] == simbolo and tab[0][1] == simbolo and tab[0][2] == simbolo
        col_1 = tab[1][0] == simbolo and tab[1][1] == simbolo and tab[1][2] == simbolo
        col_2 = tab[2][0] == simbolo and tab[2][1] == simbolo and tab[2][2] == simbolo
        diag_0 = tab[0][0] == simbolo and tab[1][1] == simbolo and tab[2][2] == simbolo
        diag_1 = tab[0][2] == simbolo and tab[1][1] == simbolo and tab[2][0] == simbolo
        if fila_0 or fila_1 or fila_2 or col_0 or col_1 or col_2 or diag_0 or diag_1:
            if simbolo == 'X':
                return 1
            elif simbolo == 'O':
                return 2
            break

def nuevoT(tab):
    tabJ = tab.copy()
    return tabJ

tab = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
tabJ = nuevoT(tab)

jugador1 = ''
jugador2 = ''
turno = 0
turnoJ = True

while turno < 9:
    if jugador1 == '':
        jugador1 = input('\nDime un nombre para el jugador nº 1:\n')
    elif jugador2 == '':
        jugador2 = input('\nDime un nombre para el jugador nº 2:\n')
    else:
        if turnoJ:
            pos=int(input('\nDime una posicion para hacer tu jugada '+jugador1+':\n'))
        else:
            pos=int(input('\nDime una posicion para hacer tu jugada '+jugador2+':\n'))
        valor = hacerJugada(tabJ, pos, turnoJ)
        if valor == 0:
            turnoJ = not turnoJ
            turno += 1
            dibTablero(tabJ)
            if ganador(tabJ) == 1:
                print('\n'+ jugador1 +' ganó el juego\n')
                break
            elif ganador(tabJ) == 2:
                print('\n' + jugador2 + ' ganó el juego\n')
                break
        else:
            print(valor)
        if turno == 9:
            print('\nHubo un empate.\n')
            break
