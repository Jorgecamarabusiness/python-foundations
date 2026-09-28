
BICHO = 'x'
VACIO = ' ' 
DERECHA = '→'
IZQUIERDA = '←'
ARRIBA = '↑'
ABAJO = '↓'

tablero = []

#ABRIMOS EL FICHERO CON EL LABERINTO Y LO CARGAMOS EN TABLERO
fichero = open("laberinto1.txt", 'r')

for linea in fichero:

    tablero += [list(linea)]

fichero.close()


pos_i = 0
pos_j = 0

tablero[pos_i][pos_j] = BICHO

avance_i = 0
avance_j = 1

pasos = 1

while ((pos_i < len(tablero)-1) and (pos_j < len(tablero[0]))):

    print(pasos)
    pasos += 1
    
    #ESCRIBIMOS EL LABERINTO
    for i in range(len(tablero)):

       print(''.join(tablero[i]), end='')

    print()
    #input()
    
#AVANZAMOS EL BICHO
    #Si vamos hacia abajo y la casilla a su derecha está vacía, gira...
    if ((avance_i == 1) and (avance_j == 0) and (tablero[pos_i][pos_j-1] == VACIO)):
        avance_i = 0
        avance_j = -1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = IZQUIERDA
        pos_i += avance_i
        pos_j += avance_j

    #Si vamos hacia arriba y la casilla a su derecha está vacía, gira...
    elif ((avance_i == -1) and (avance_j == 0) and (tablero[pos_i][pos_j+1] == VACIO)):
        avance_i = 0
        avance_j = 1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = DERECHA
        pos_i += avance_i
        pos_j += avance_j

    #Si vamos hacia la izquierda y la casilla a su derecha está vacía, gira...
    elif ((avance_i == 0) and (avance_j == -1) and (tablero[pos_i-1][pos_j] == VACIO)):
        avance_i = -1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ARRIBA
        pos_i += avance_i
        pos_j += avance_j

    #Si vamos hacia la derecha y la casilla su derecha está vacía, gira...
    elif ((avance_i == 0) and (avance_j == 1) and (tablero[pos_i+1][pos_j] == VACIO)):
        avance_i = 1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ABAJO
        pos_i += avance_i
        pos_j += avance_j

#Si no puede girar y la casilla siguiente está vacía...
    elif (tablero[pos_i+avance_i][pos_j+avance_j] == VACIO):
        if ((avance_i == 1) and (avance_j == 0) and (tablero[pos_i+1][pos_j] == VACIO)):
            avance_i = 1
            avance_j = 0
            tablero[pos_i][pos_j] = VACIO
            tablero[pos_i+avance_i][pos_j+avance_j] = ABAJO
            pos_i += avance_i
            pos_j += avance_j
            
        if ((avance_i == -1) and (avance_j == 0) and (tablero[pos_i-1][pos_j] == VACIO)):
            avance_i = -1
            avance_j = 0
            tablero[pos_i][pos_j] = VACIO
            tablero[pos_i+avance_i][pos_j+avance_j] = ARRIBA
            pos_i += avance_i
            pos_j += avance_j

        if ((avance_i == 0) and (avance_j == 1) and (tablero[pos_i][pos_j+1] == VACIO)):
            avance_i = 0
            avance_j = 1
            tablero[pos_i][pos_j] = VACIO
            tablero[pos_i+avance_i][pos_j+avance_j] = DERECHA
            pos_i += avance_i
            pos_j += avance_j

        if ((avance_i == 0) and (avance_j == -1) and (tablero[pos_i][pos_j-1] == VACIO)):
            avance_i = 0
            avance_j = -1
            tablero[pos_i][pos_j] = VACIO
            tablero[pos_i+avance_i][pos_j+avance_j] = IZQUIERDA
            pos_i += avance_i
            pos_j += avance_j

#Si no puede girar y la siguiente casilla no está vacía...

        #Si venía hacia abajo, gira a su derecha si puede(línea de código eliminada)

    #Si venía hacia abajo y no puede girar a su derecha, que gire a la izquierda si puede
    elif ((avance_i == 1) and (avance_j == 0) and (tablero[pos_i][pos_j+1] == VACIO)):
        avance_i = 0
        avance_j = 1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = DERECHA
        pos_i += avance_i
        pos_j += avance_j

    #Si venía hacia abajo y no puede girar ni a su derecha ni a su izquierda, que dé la vuelta
    elif ((avance_i == 1) and (avance_j == 0)):
        avance_i = -1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ARRIBA
        pos_i += avance_i
        pos_j += avance_j

        #Si venía hacia la izquierda, gira a su derecha si puede (línea de código eliminada)

    #Si venía hacia la izquierda, gira a su izquierda si no puede girar a la derecha
    elif ((avance_i == 0) and (avance_j == -1) and (tablero[pos_i+1][pos_j] == VACIO)):
        avance_i = 1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ABAJO
        pos_i += avance_i
        pos_j += avance_j

    #Si venía hacia la izquierda, da la vuelta si no puede girar ni a izquierda ni a derecha
    elif ((avance_i == 0) and (avance_j == -1)):
        avance_i = 0
        avance_j = 1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = DERECHA
        pos_i += avance_i
        pos_j += avance_j

        #Si venía hacia arriba, que gire a su derecha si puede (línea de código eliminada)

    #Si venía hacia arriba, que gire a su izquierda si no puede girar a la derecha
    elif ((avance_i == -1) and (avance_j == 0) and (tablero[pos_i][pos_j-1] == VACIO)):
        avance_i = 0
        avance_j = -1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = IZQUIERDA
        pos_i += avance_i
        pos_j += avance_j


    #Si venía hacia arriba y no puede girar ni a derecha ni a izquierda, que dé la vuelta
    elif ((avance_i == -1) and (avance_j == 0)):
        avance_i = 1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ABAJO
        pos_i += avance_i
        pos_j += avance_j

            #Si venía hacia la derecha, que gire a su derecha si puede (línea de código eliminada)

    #Si venía hacia la derecha, que gire a su izquierda si no puede girar a la derecha
    elif ((avance_i == 0) and (avance_j == 1) and (tablero[pos_i-1][pos_j] == VACIO)):
        avance_i = -1
        avance_j = 0
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = ARRIBA
        pos_i += avance_i
        pos_j += avance_j

    #Si venía hacia la derecha, que dé la vuelta si no puede girar ni a su izquierda ni a su derecha
    elif ((avance_i == 0) and (avance_j == 1)):
        avance_i = 0
        avance_j = -1
        tablero[pos_i][pos_j] = VACIO
        tablero[pos_i+avance_i][pos_j+avance_j] = IZQUIERDA
        pos_i += avance_i
        pos_j += avance_j