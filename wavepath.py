# WAVEPATH v 1
# Javier del Álamo -=- 10/19/2013


import random
import time
import os

def displayIntro():
    print()
    print()
    print('= WAVEPATH =')
    time.sleep(1)
    print('Wavepath es un programa para generar ')
    time.sleep(1)
    print('trayectorias sobre mapas de celdas. ')
    time.sleep(1)
    print('En esta versión se trabaja sobre mapas de ')
    time.sleep(1)
    print('celdas cuadradas y conectividad de 4 u 8 puntos. ')
    time.sleep(1)
    print('Se debe indicar la celda de partida así como la celda objetivo. ')
    time.sleep(1)
    print('Se pueden seleccionar celdas obstaculo, así como la resolución.')
    print()


displayIntro()

continuar='y'
while continuar=='y':

    time.sleep(1)
    print('Por favor, introduzca la resolución deseada.')
    time.sleep(1)
    print('(Número de filas, enter,número de columnas,enter.)')
    Resolution=[None]*2
    Resolution[0]=input()
    Resolution[1]=input()
    dim_filas=int(Resolution[0])
    dim_columnas=int(Resolution[1])
    dim_max=max(dim_filas,dim_columnas)

    Grid=[None]*dim_filas
    Numbergrid=[None]*dim_filas

    for i in range(dim_filas):
         Grid[i]=[None]*dim_columnas
         Numbergrid[i]=[None]*dim_columnas

    for i in range(dim_filas):
        for j in range(dim_columnas):
            Grid[i][j]=' '
            Numbergrid[i][j]='None'

    print('Por favor, introduzca la casilla "Inicio"')
    time.sleep(1)
    print('(Número de fila, enter,número de columna,enter.)')
    Start=[None]*2
    Start[0]=input()
    Start[1]=input()
    Grid[int(Start[0])-1][int(Start[1])-1]='O'

    print('Por favor, introduzca la casilla "objetivo"')
    time.sleep(1)
    print('(Número de fila, enter,número de columna,enter.)')
    Goal=[None]*2
    Goal[0]=input()
    Goal[1]=input()
    Grid[int(Goal[0])-1][int(Goal[1])-1]='X'
    Numbergrid[int(Goal[0])-1][int(Goal[1])-1]=0

    print('Ahora, introduzca las casillas "obstáculo"')
    time.sleep(1)
    masobstaculos='y'
    while masobstaculos=='y':
        print('(Número de fila, enter,número de columna,enter.)')
        Obstacle=[None]*2
        Obstacle[0]=input()
        Obstacle[1]=input()
        Grid[int(Obstacle[0])-1][int(Obstacle[1])-1]='Z'
        Numbergrid[int(Obstacle[0])-1][int(Obstacle[1])-1]=100

        print('¿Desea continuar? (y/n)')
        masobstaculos=input()



    for n in range(2*dim_max):
        for i in range(dim_filas):
            for j in range(dim_columnas):
                if Numbergrid[i][j]==n:
                    if (i+1) <= (dim_filas-1) and Numbergrid[i+1][j]=='None':
                        Numbergrid[i+1][j]=n+1

                    if (i-1) >= 0 and Numbergrid[i-1][j]=='None':
                        Numbergrid[i-1][j]=n+1

                    if (j+1) <= (dim_columnas-1) and Numbergrid[i][j+1]=='None':
                        Numbergrid[i][j+1]=n+1

                    if (j-1) >= 0 and Numbergrid[i][j-1]=='None':
                        Numbergrid[i][j-1]=n+1

    cf=int(Start[0])-1
    cc=int(Start[1])-1
    vact=Numbergrid[cf][cc]
    os.system("clear all")
    time.sleep(1)
    for i in range(dim_filas):
        print (Grid[i])
    time.sleep(1)
    os.system("clear all")

    while vact != 1:
        if (cf+1) <= (dim_filas-1) and vact > Numbergrid[cf+1][cc]:
            vact = Numbergrid[cf+1][cc]
            Grid[cf+1][cc]='*'
            cf=cf+1
        elif (cc-1) >= 0 and vact > Numbergrid[cf][cc-1]:
            vact = Numbergrid[cf][cc-1]
            Grid[cf][cc-1]='*'
            cc=cc-1
        elif (cf-1) >= 0 and vact > Numbergrid[cf-1][cc]:
            vact = Numbergrid[cf-1][cc]
            Grid[cf-1][cc]='*'
            cf=cf-1
        elif (cc+1) <= (dim_columnas-1) and vact > Numbergrid[cf][cc+1]:
            vact = Numbergrid[cf][cc+1]
            Grid[cf][cc+1]='*'
            cc=cc+1
        else:
           print ('No hay solución')
           vact=0
        for i in range(dim_filas):
            print (Grid[i])
        time.sleep(0.35)
        os.system("clear all")


    for i in range(dim_filas):
        print (Grid[i])


    #for i in range(int(dim_filas)):
        #print (Numbergrid[i])

    print('¿Desea continuar? (y/n)')
    continuar=input()
