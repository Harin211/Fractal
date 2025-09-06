
import pygame
import math
import sys

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fractals")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_tree(surface, x, y, angle, depth):

    # base case
    if depth == 0:
        return 

    #recursive case
    length = depth * 10

    x2 = x + math.cos(angle) * length
    y2 = y + math.sin(angle) * length

    pygame.draw.line(surface, WHITE, (x,y), (x2, y2), 2)

    draw_tree(surface, x2, y2, angle - math.pi / 6, depth - 1)
    draw_tree(surface, x2, y2, angle + math.pi / 6, depth - 1)


def main():

    depth= int(input("Enter depth:"))

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        draw_tree(screen, 400, 200, math.pi / 2, depth)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    
    pygame.quit()


if __name__ == "__main__":
    main()
