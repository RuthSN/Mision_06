import math
import pygame

ANCHO = 800
ALTO = 800

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

ANCHO = 1600
ALTO = 800

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)


def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        for theta in range(0, 360*(r//math.gcd(r, R)), 1):
            a = math.radians(theta)
            k = r/R
            x = int(R*(((l - k) * math.cos(a) + l * k * math.cos(((l - k) / k) * a))))
            y = int(R*(((l - k) * math.sin(a) - l * k * math.sin(((l - k) / k) * a))))
            pygame.draw.circle(ventana, ROJO, (x+ANCHO//2,ALTO//2-y), 1)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()



def main():
    r = 54
    R = 220
    l = 1
    dibujar(r, R, l)

main()
