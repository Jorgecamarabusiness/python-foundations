

tablero = []
import random

#DIMENSIONES DEL TABLERO
ANCHO = 30
ALTO = 13

#NUMERO DE CADA CIVILIZACION
NUMERO_DICENPAIZON = 25
NUMERO_DICENPITON = 25
NUMERO_ASESINO_DORMIDO = 1

#DEFINO LOS CARACTERES DE CADA COSA
ASESINO_DORMIDO = '^'
ASESINO = 'º'
DICENPAIZON = '-'
DICENPITON = '+'
VACIO = ' '
TABLERO = '#'
DICENPAIZON_NOMOVER = 'x'
BOMBA='Q'
CERCA_DE_EXPLOTAR='O'
EXPLOSION='*'

#TABLERO Y RELLENO
for i in range (ALTO):
    tablero += [[]]    
    for j in range(ANCHO):
        tablero[i] += [VACIO]

#TAPAS ARRIBA Y ABAJO
for j in range(ANCHO):
    tablero[0][j]= TABLERO
    tablero[ALTO-1][j]= TABLERO
        
for i in range (ALTO):
    tablero[i][0]= TABLERO
    tablero[i][ANCHO-1]= TABLERO

#INDIVIDUOS
i = 0
while i < NUMERO_DICENPAIZON:
    i_nuevo = int(random.random()*ALTO)
    j_nuevo = int(random.random()*ANCHO/3)
    if tablero[i_nuevo][j_nuevo] == VACIO:
        tablero[i_nuevo][j_nuevo] = DICENPAIZON
        i += 1

j = 0
while j < NUMERO_DICENPITON:
    i_nuevo2 = int(random.random()*ALTO)
    j_nuevo2 = int(random.random()*ANCHO/3) + ((ANCHO//3)*2)
    if tablero[i_nuevo2][j_nuevo2] == VACIO:
        tablero[i_nuevo2][j_nuevo2] = DICENPITON
        j += 1     

#AÑADO UN ASESINO EN EL CENTRO QUE SE REPRODUCE AL MATAR A VARIOS A LA VEZ
k = 0
while k < NUMERO_ASESINO_DORMIDO:
    i_nuevo3 = int(random.random()*ALTO/10) + ((ALTO//10)*5)
    j_nuevo3 = int(random.random()*ANCHO/10) + ((ANCHO//10)*5)
    if tablero[i_nuevo3][j_nuevo3] == VACIO:
        tablero[i_nuevo3][j_nuevo3] = ASESINO_DORMIDO
        k += 1

#RECORREMOS LA MATRIZ IMPRIMIENDO LA POSICIÓN ij
for i in range(len(tablero)):
    for j in range(len(tablero[i])):
        print(tablero[i][j], end = '')
    print()

#IMPLEMENTO LAS REPETICIONES
repeticiones = 0
while repeticiones < 28:
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j],end='')  
        print()
    repeticiones += 1
    for i in range (1, len(tablero) - 1):
        for j in range(1, len(tablero[i]) - 1):     
            aleatorio=random.random()
            if repeticiones < 28:

#ENCONTRAMOS UN DICENPITON
                if tablero[i][j] == DICENPITON:

#PROBABILIDAD DE QUE DICENPITON SALTE A DICENPAZON
                    if tablero [i][j-1] == DICENPAIZON and aleatorio <= 0.5:
                        if tablero [i][j-2] == VACIO or tablero[i][j-2] == DICENPAIZON:
                            tablero[i][j-2] = DICENPITON
                            tablero[i][j] = VACIO

#PROBABILIDAD DE QUE LUEGO DISPARE HACIA ATRAS Y MATE AL DICENPAIZON
                            if aleatorio < 0.1 and tablero[i][j-1] == DICENPAIZON:
                                tablero[i][j-1] = VACIO
                                
#SI LA SIGUIENTE CASILLA ESTÁ VACÍA           
                    if tablero[i][j - 1] == VACIO:
                        tablero[i][j - 1] = DICENPITON
                        tablero[i][j] = VACIO

#AL ENCONTRAR UNA EXPLOSION SALTAN HACIA OTRO CARRIL (ARRIBA O ABAJO)
                    if tablero [i][j-1] == EXPLOSION:
                        if aleatorio<0.5:
                            if tablero [i-1][j-1] == VACIO:
                                tablero [i-1][j-1] = DICENPITON
                                tablero[i][j] = VACIO
                        else:
                            if tablero [i+1][j-1] == VACIO:
                                tablero[i+1][j-1] = DICENPITON
                                tablero[i][j] = VACIO


#ENCONTRAMOS UN DICENPAIZON
                if tablero[i][j] == DICENPAIZON:

#SI LA SIGUIENTE CASILLA ESTÁ VACÍA
                    if (tablero[i][j + 1] == VACIO) or (tablero[i][j + 1] == DICENPITON):
                        tablero[i][j + 1] = DICENPAIZON_NOMOVER
                        tablero[i][j] = VACIO

#AL ENCONTRAR UNA EXPLOSION SALTAN HACIA OTRO CARRIL (ARRIBA O ABAJO)
                    if tablero [i][j+1] == EXPLOSION:
                        if aleatorio<0.5:
                            if tablero [i-1][j+1] == VACIO:
                                tablero [i-1][j+1] = DICENPAIZON
                                tablero[i][j] = VACIO
                        else:
                            if tablero [i+1][j+1] == VACIO:
                                tablero[i+1][j+1] = DICENPAIZON
                                tablero[i][j] = VACIO

#ENCONTRAMOS UN DICENPAIZON_NOMOVER
                if tablero [i][j] == DICENPAIZON_NOMOVER:             
                    tablero[i][j] = DICENPAIZON

#ENCONTRAMOS UN ASESINO QUE DESPIERTA TRAS 17 REPETICIONES
                if repeticiones > 15:
                    if tablero [i][j] == ASESINO_DORMIDO:
                        tablero[i][j] = ASESINO

#EL ASESINO COMIENZA A MATAR
                if tablero [i][j] == ASESINO:
                    if (tablero[i][j + 1] == DICENPAIZON):
                        tablero[i][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i][j - 1] == DICENPAIZON):
                        tablero[i][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j] == DICENPAIZON):
                        tablero[i + 1][j] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j] == DICENPAIZON):
                        tablero[i - 1][j] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j + 1] == DICENPAIZON):
                        tablero[i + 1][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j + 1] == DICENPAIZON):
                        tablero[i - 1][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j - 1] == DICENPAIZON):
                        tablero[i + 1][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j - 1] == DICENPAIZON):
                        tablero[i - 1][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i][j + 1] == DICENPITON):
                        tablero[i][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i][j - 1] == DICENPITON):
                        tablero[i][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j] == DICENPITON):
                        tablero[i + 1][j] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j] == DICENPITON):
                        tablero[i - 1][j] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j + 1] == DICENPITON):
                        tablero[i + 1][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j + 1] == DICENPITON):
                        tablero[i - 1][j + 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i + 1][j - 1] == DICENPITON):
                        tablero[i + 1][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    if (tablero[i - 1][j - 1] == DICENPITON):
                        tablero[i - 1][j - 1] = ASESINO
                        tablero [i][j] = VACIO
                    
#PONGO BOMBAS QUE EXPLOTAN A LA TERCERA REPETICION DEL TABLERO 
#EXPLOSION
            if (tablero[i][j] == CERCA_DE_EXPLOTAR):
                    tablero[i][j] = EXPLOSION
                    if tablero[i][j+1] == TABLERO:
                        tablero[i][j+1] =TABLERO
                    else:
                        tablero[i][j+1] =VACIO

                    if tablero[i-1][j+1] == TABLERO:
                        tablero[i-1][j+1] =TABLERO
                    else:
                        tablero[i-1][j+1] =VACIO

                    if tablero[i+1][j] == TABLERO:
                        tablero[i+1][j] =TABLERO
                    else:
                        tablero[i+1][j] =VACIO

                    if tablero[i-1][j] == TABLERO:
                        tablero[i-1][j] =TABLERO
                    else:
                        tablero[i-1][j] = VACIO

                    if tablero[i][j-1] == TABLERO:
                        tablero[i][j-1] =TABLERO
                    else:
                        tablero[i][j-1] =VACIO

                    if tablero[i-1][j-1] == TABLERO:
                        tablero[i-1][j-1] =TABLERO
                    else:
                        tablero[i-1][j-1] =VACIO
                        
                    if tablero[i+1][j-1] == TABLERO:
                        tablero[i+1][j-1] = TABLERO
                    else:
                        tablero[i+1][j-1] =VACIO

#CAMBIO DE BOMBA A BOMBA A PUNTO DE EXPLOTAR
            if (tablero[i][j] == BOMBA):
                tablero[i][j] = CERCA_DE_EXPLOTAR

#COLOCACION DE BOMBA
            if repeticiones < 7 and aleatorio <= 0.003:
                if (tablero[i][j]== VACIO):
                    tablero[i][j] = BOMBA
    
print()

