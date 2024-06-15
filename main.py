import pygame
import os
import time

# Creating the screen
colorSC = [255,255,255]
screen = pygame.display.set_mode((800,800))
screen.fill(colorSC)

# FPS
clock = pygame.time.Clock()
FPS = 120

# Initializing Color
color = (255,0,0)
color2 = (0,255,0)
color3 = (0,0,255)

# Posiciones de los cuadrados
sPos = 60
mPos = 45
bPos = 15
posY = 60
sqd = 30

# Square
square = pygame.Rect(sPos,posY,sqd,sqd)
square2 = pygame.Rect(mPos,posY-15,sqd*2,sqd*2)
square3 = pygame.Rect(bPos,posY-(15*3),sqd*4,sqd*4)

# Drawing Rectangle
# pygame.draw.rect(screen, color, square)
# pygame.display.flip()

# Events
# Scancodes
# Left = 80
# Up = 82
# Right = 79
# Down = 81

def posData(sqr):
    return f'square {sqr.height * sqr.width} pos is {sqr.x} {sqr.y}'

# Speed

speed = 8
sSquareSpeed = 4
mSquareSpeed = 2
bSquareSpeed = 1
lerp_factor = 0.05
minMSquareSpeed = 2
speedLow = speed/2
# Running the game
running = True
print(posData(square))
print(posData(square2))
print(posData(square3))
while running:
    for event in pygame.event.get():
        # # If the button X is clicked then the game stop
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         square.x -= speed1
        #         # square2.x -= speed
        #         print('LEFT KEY PRESSED')
        #     if event.key == pygame.K_d:
        #         square.x += speed1
        #         # square2.x += speed
        #         print('RIGHT KEY PRESSED')                    
            if event.key == pygame.K_p:
                print(posData(square))
                print(posData(square2))
                print(posData(square3))

        target_pos = square.x
        direction = target_pos - square2.x

        # Interpolación líneal del cuadrado m para seguir al s
        square2.x += direction * lerp_factor


        # Empezamos la prueba
        
        # Asegurar que el cuadrado m se mueva con una velocidad minima
        if abs(direction) > minMSquareSpeed:
            square2.x += minMSquareSpeed if direction > 0 else -minMSquareSpeed

        

        # if square.x < square2.x:
        #     square2.x 


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            square.x -= sSquareSpeed
            # square2.x -= speedLow
            print('LEFT KEY IS BEING PRESSED')
        if pressed[pygame.K_d]:
            square.x += sSquareSpeed
            # square2.x += speedLow
            print('RIGHT KEY IS BEING PRESSED')

        # The big square following the little one:



        # if square2.x + 15 < square.x:
        #     square2.x += mSquareSpeed 
        # if square2.x + 15 > square.x:
        #     square2.x -= mSquareSpeed
        
        # if square3.x + 30 < square2.x:
        #     square3.x += bSquareSpeed 
        # if square3.x + 30 > square2.x:
        #     square3.x -= bSquareSpeed
        

    screen.fill(colorSC) # Fill the entire screen
    pygame.draw.rect(screen,color3,square3)
    pygame.draw.rect(screen,color2,square2)
    pygame.draw.rect(screen,color,square) # Draw again over the screen
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()