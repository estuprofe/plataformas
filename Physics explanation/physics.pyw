#!/usr/bin/python3
# módulos necesarios #
import pygame
import sys
from pygame.locals import *
# variables
colorFondo= pygame.Color("white")
colorFrente= pygame.Color("green")
colorTeselas = pygame.Color("gray")

# setup pygame/window
reloj=pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Experimento de física y colisiones')
pantalla = pygame.display.set_mode((500,500),0,32)
jugador = pygame.Rect(100,100,40,80)
teselas= [pygame.Rect(200,350,50,50),pygame.Rect(260,350,50,50)]

# funciones #
def comprueba_colisiones(rectangulo,teselas):
    colisiones = []
    for tesela in teselas:
        if rectangulo.colliderect(tesela):
            colisiones.append(tesela)
    return colisiones

def mover(rectangulo, movimiento, teselas):
    print(movimiento)
    

    rectangulo.x += movimiento[0]
    colisiones = comprueba_colisiones(rectangulo,teselas)
    for tesela in colisiones:
        if movimiento[0] > 0:
            rectangulo.right = tesela.left
        if movimiento[0] < 0:
            rectangulo.left = tesela.right
    rectangulo.y += movimiento[1]
    for tesela in colisiones:
        if movimiento[1] > 0:
            rectangulo.bottom = tesela.top
        if movimiento[1] < 0:
            rectangulo.top = tesela.bottom

derecha= False
izquierda = False
arriba = False
abajo = False

# Ciclo de juego #
while True:
        # Limpiar pantalla #

        pantalla.fill(colorFondo)
        movimiento = [0,0]
        if derecha == True:
            movimiento[0] +=5
        if izquierda == True:
            movimiento[0] -=5
        if arriba == True:
            movimiento[1] -=5
        if abajo == True:
            movimiento[1] +=5

        mover(jugador,movimiento,teselas)

        pygame.draw.rect(pantalla,colorFrente,jugador)

        for tesela in teselas:
            pygame.draw.rect(pantalla,colorTeselas,tesela)

        # Manejo de eventos

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    derecha = True
                if evento.key == K_LEFT:
                    izquierda = True
                if evento.key == K_UP:
                    arriba = True
                if evento.key == K_DOWN:
                    abajo = True
            if evento.type == KEYUP:
                if evento.key == K_RIGHT:
                    derecha = False
                if evento.key == K_LEFT:
                    izquierda = False
                if evento.key == K_UP:
                    arriba = False
                if evento.key == K_DOWN:
                    abajo = False
        
        # actualizar pantalla #
        pygame.display.update()
        reloj.tick(40)