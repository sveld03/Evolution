from config import *

# this import may be temporary, while I am testing this as a main file
# from Field import *

import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BLOCKSIZE = WIDTH // FIELDWIDTH

class Grid:
    def __init__(self):
        # self.player_name = playerName
        # self.player_one_field = playerOneField
        # self.player_two_field = playerTwoField
        # self.player_number = playerNumber

        pygame.font.init()

        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Evolution")

        self.PLANT1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'plant.png')).convert(), (BLOCKSIZE, BLOCKSIZE))
        self.PLANT2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'plant2.png')).convert(), (BLOCKSIZE, BLOCKSIZE))

        self.plant_list = []
        for row in range(FIELDWIDTH):
            self.plant_list.append([])
            for column in range(FIELDHEIGHT): 
                self.plant_list[row].append(0)
        self.draw_grid()

    def draw_grid(self):

        self.WIN.fill(BLACK)

        grid = []
        for x in range(0, WIDTH, BLOCKSIZE):
            grid.append([])
            for y in range(0, HEIGHT, BLOCKSIZE):
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                grid[x//BLOCKSIZE].append(rect)
                pygame.draw.rect(self.WIN, WHITE, rect, 1)
        pygame.display.update()

def inpt(prompt):
    print(prompt)
    input=""

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    pygame.quit()
                else:
                    input += chr(event.key)
    return input

# grid = Grid()
# result = inpt("test input: ")
# print(result)

# def main():
#     # pygame.init()

#     field = Field.initializeField()
#     player = Player(1, field)

#     Player.draw_window_init

#     WIN.fill(BLACK)
#     run = True
#     clock = pygame.time.Clock()
#     while run:
#         clock.tick()
#         player.draw_plants()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#         pygame.display.update()

# if __name__ == "__main__":
#     main()