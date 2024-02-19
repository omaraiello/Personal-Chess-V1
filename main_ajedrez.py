import pygame
from clases import Ficha

#----------------- Dimensiones de la ventana y el tablero-------#
ANCHO, ALTO = 500, 500
DIMENSION = 8
TAMANO_CUADRO = ANCHO // DIMENSION
BORDE = 4
#------------------------- Colores------------------------------#
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100)
AZUL = (0, 0, 255)
NEGRO_TEXTO = (0, 0, 0)
#--------------------IMAGENES DE FICHAS ------------------------#

Peon_img_B = pygame.image.load('imagenes/Peon_B.png')
rey_img_B  = pygame.image.load('imagenes/Rey_B.png')
reina_img_B  = pygame.image.load('imagenes/Reina_B.png')
torre_img_B  = pygame.image.load('imagenes/Torre_B.png')
alfil_img_B  = pygame.image.load('imagenes/Alfil_B.png')
caballo_img_B  = pygame.image.load('imagenes/Caballo_B.png')


Peon_img_N  = pygame.image.load('imagenes/Peon_N.png')
rey_img_N   = pygame.image.load('imagenes/Rey_N.png')
reina_img_N  = pygame.image.load('imagenes/Reina_N.png')
torre_img_N  = pygame.image.load('imagenes/Torre_N.png')
alfil_img_N  = pygame.image.load('imagenes/Alfil_N.png')
caballo_img_N  = pygame.image.load('imagenes/Caballo_N.png')

selec_img = pygame.image.load('imagenes/Selector.png')
mov_img = pygame.image.load('imagenes/mov.png')
#----------------------FICHAS-----------------------------------#
FICHAS = []
FICHAS_MUERTAS = []
LISTA_MOV = []
 
selector = Ficha("select",selec_img,3,4,1,"",True,TAMANO_CUADRO)

FICHAS.append(Ficha("torre",torre_img_N,0,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("torre",torre_img_N,7,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("caballo",caballo_img_N,1,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("caballo",caballo_img_N,6,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("alfil",alfil_img_N,2,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("alfil",alfil_img_N,5,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("rey",rey_img_N,3,0,1,"negro",True,TAMANO_CUADRO))
FICHAS.append(Ficha("reina",reina_img_N,4,0,1,"negro",True,TAMANO_CUADRO))

FICHAS.append(Ficha("torre",torre_img_B,0,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("torre",torre_img_B,7,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("caballo",caballo_img_B,1,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("caballo",caballo_img_B,6,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("alfil",alfil_img_B,2,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("alfil",alfil_img_B,5,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("rey",rey_img_B,3,7,1,"blanco",True,TAMANO_CUADRO))
FICHAS.append(Ficha("reina",reina_img_B,4,7,1,"blanco",True,TAMANO_CUADRO))

for n in range(8):
    FICHAS.append(Ficha("peon",Peon_img_N,n,1,1,"negro",True,TAMANO_CUADRO))
for n in range(8):
    FICHAS.append(Ficha("peon",Peon_img_B,n,6,1,"blanco",True,TAMANO_CUADRO))    

display = pygame.display.set_mode((ANCHO,ALTO))

def posicion (event_pos):
    pixel_x = event_pos[0]
    pixel_y = event_pos[1]
    posicion_x = pixel_x // 62  
    posicion_y = pixel_y // 62
                       
    return posicion_x,posicion_y

def movimientos(ficha):
#------------------------------------PEON-----------------------------------------------------------------------------------------------------#
    if (ficha.tipo == "peon"):
        movimiento = True
        if(ficha.color == "blanco"):
            for eat in FICHAS:
                if (eat.posicion_X == ficha.posicion_X-1) and (eat.posicion_Y == ficha.posicion_Y-1) and (eat.color == "negro"):
                    LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X-1,ficha.posicion_Y-1,1,"",True,TAMANO_CUADRO))
                if (eat.posicion_X == ficha.posicion_X+1) and (eat.posicion_Y == ficha.posicion_Y-1) and (eat.color == "negro"):    
                    LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X+1,ficha.posicion_Y-1,1,"",True,TAMANO_CUADRO))
                if (eat.posicion_X == ficha.posicion_X) and (eat.posicion_Y == ficha.posicion_Y-1):
                    movimiento = False
            if ficha.posicion_Y == 6: 
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,ficha.posicion_Y-2,1,"",True,TAMANO_CUADRO))
            if (movimiento == True):
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,ficha.posicion_Y-1,1,"",True,TAMANO_CUADRO))
        if(ficha.color == "negro"):
            for eat in FICHAS:
                if (eat.posicion_X == ficha.posicion_X+1) and (eat.posicion_Y == ficha.posicion_Y+1) and (eat.color == "blanco"):
                    LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X+1,ficha.posicion_Y+1,1,"",True,TAMANO_CUADRO))
                if (eat.posicion_X == ficha.posicion_X-1) and (eat.posicion_Y == ficha.posicion_Y+1) and (eat.color == "blanco"):    
                    LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X-1,ficha.posicion_Y+1,1,"",True,TAMANO_CUADRO))
                if (eat.posicion_X == ficha.posicion_X) and (eat.posicion_Y == ficha.posicion_Y+1):
                    movimiento = False
            if (movimiento == True):    
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,ficha.posicion_Y+1,1,"",True,TAMANO_CUADRO))
            if ficha.posicion_Y == 1:
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,ficha.posicion_Y+2,1,"",True,TAMANO_CUADRO))
#------------------------------------TORRE-----------------------------------------------------------------------------------------------------#
    if ficha.tipo == "torre":
        if(ficha.color == "blanco"):
            for mov in range(10):
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,mov,1,"",True,TAMANO_CUADRO))
            for mov in range(10):
                LISTA_MOV.append(Ficha("mov",mov_img,mov,ficha.posicion_Y,1,"",True,TAMANO_CUADRO))
        if(ficha.color == "negro"):
            for mov in range(10):
                LISTA_MOV.append(Ficha("mov",mov_img,ficha.posicion_X,mov,1,"",True,TAMANO_CUADRO))
            for mov in range(10):
                LISTA_MOV.append(Ficha("mov",mov_img,mov,ficha.posicion_Y,1,"",True,TAMANO_CUADRO))
#------------------------------------ALFIL-----------------------------------------------------------------------------------------------------#

#------------------------------------REY-------------------------------------------------------------------------------------------------------#

#------------------------------------REINA-----------------------------------------------------------------------------------------------------#

#------------------------------------CABALLO---------------------------------------------------------------------------------------------------#

#------------------------------------FIN-------------------------------------------------------------------------------------------------------#


def dibujar_tablero(pantalla):
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (columna * TAMANO_CUADRO, fila * TAMANO_CUADRO, TAMANO_CUADRO, TAMANO_CUADRO))

    # Dibujar peón
    for ficha in FICHAS :
        if (ficha.vivo == True):
            display.blit(ficha.imagen,(ficha.pixel_X,ficha.pixel_Y))
    display.blit(selector.imagen,(selector.pixel_X,selector.pixel_Y))    
    for movi in LISTA_MOV:
        display.blit(movi.imagen,(movi.pixel_X,movi.pixel_Y))
    
    # Dibujar borde azul alrededor del tablero
    pygame.draw.rect(pantalla, AZUL, (0, 0, ANCHO, ALTO), BORDE)

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Tablero de Ajedrez')

    reloj = pygame.time.Clock()
    corriendo = True
    mouse_pos = 10, 10
    valor = 0
    Turno = "blanco"                     #TRUE BLANCAS / FALSE NEGROS
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.pos != mouse_pos):
                mouse_pos = posicion(event.pos)
                selector.posicion_X ,selector.posicion_Y = mouse_pos
                selector.pixel()
                contador = 0
                contador_2 = 0
                for mover in LISTA_MOV:
                    if (selector.posicion_X == mover.posicion_X) and (selector.posicion_Y == mover.posicion_Y):
                        if Turno == "blanco":
                            Turno = "negro"
                        else:
                            Turno = "blanco"
                        LISTA_MOV.clear()
                        FICHAS[valor-1].posicion_X = mover.posicion_X
                        FICHAS[valor-1].posicion_Y = mover.posicion_Y
                        FICHAS[valor-1].pixel()
                        contador = 0
                        for comer in FICHAS:
                            contador_2+=1
                            if (comer.posicion_X == FICHAS[valor-1].posicion_X) and (comer.posicion_Y == FICHAS[valor-1].posicion_Y) and (comer.color != FICHAS[valor-1].color) and (ficha_select.vivo == True):
                                FICHAS_MUERTAS.append(FICHAS.pop(contador_2-1))
                for ficha_select in FICHAS:
                    contador = contador + 1
                    if (selector.posicion_X == ficha_select.posicion_X) and (selector.posicion_Y == ficha_select.posicion_Y) and (ficha_select.vivo == True) and (ficha_select.color == Turno):
                        valor = contador
                        LISTA_MOV.clear()
                        movimientos(ficha_select)   
        pantalla.fill(GRIS_CLARO)
        dibujar_tablero(pantalla)
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()