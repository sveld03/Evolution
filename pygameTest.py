# pygame test

import pygame
import os
pygame.font.init()

from config import *
from Field import *

WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BLOCKSIZE = 100
PLANT1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'plant.png')).convert(), (BLOCKSIZE, BLOCKSIZE))

TINY_FONT = pygame.font.SysFont('comicsans', 15)
SMALL_FONT = pygame.font.SysFont('comicsans', 20)
MEDIUM_FONT = pygame.font.SysFont('comicsans', 40)
BIG_FONT = pygame.font.SysFont('comicsans', 100)

# Most games run at 60 fps
FPS = 30

class Draw:

    def __init__(self):
        self.player1_name = ""
        self.name1_width = 20

        self.player2_name = ""
        self.name2_width = 20

        self.dont_draw_grid = False

        self.plant_grid = []
        for row in range(FIELDWIDTH):
            self.plant_grid.append([])
            for column in range(FIELDHEIGHT): 
                self.plant_grid[row].append(0)

        self.field1 = Field(self.plant_grid, 1)
        self.field2 = Field(self.plant_grid, 2)

        self.plant_counter1 = 0
        self.plant_counter2 = 0

    def draw_grid(self):
        WIN.fill(BLACK)

        grid = []
        for x in range(0, WIDTH, BLOCKSIZE):
            grid.append([])
            for y in range(200, HEIGHT, BLOCKSIZE):
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                grid[x//BLOCKSIZE].append(rect)
                pygame.draw.rect(WIN, WHITE, rect, 1)

    def draw_intro(self):
        intro_text1 = MEDIUM_FONT.render("Welcome to Evolution!", 1, WHITE)
        WIN.blit(intro_text1, (WIDTH//2 - intro_text1.get_width()//2, 10))
        intro_text2 = TINY_FONT.render("In this game, you will be designing a field of plants", 1, WHITE)
        WIN.blit(intro_text2, (WIDTH//2 - intro_text2.get_width()//2, 80))
        intro_text3 = TINY_FONT.render("and watching them evolve in response to changing environments.", 1, WHITE)
        WIN.blit(intro_text3, (WIDTH//2 - intro_text3.get_width()//2, 110))
        intro_text4 = SMALL_FONT.render("Are you ready to play? Press enter to start.", 1, WHITE)
        WIN.blit(intro_text4, (WIDTH//2 - intro_text4.get_width()//2, 150))

    def draw_name(self, player, stored_events):
        self.dont_draw_grid = True
        prompt = SMALL_FONT.render("Player " + str(player) + ", enter your name (no caps): ", 1, WHITE)
        WIN.blit(prompt, (20, 90))
        for event in stored_events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                else:
                    if player == 1:
                        self.player1_name += chr(event.key)
                    elif player == 2:
                        self.player2_name += chr(event.key)
        if player == 1:
            name = SMALL_FONT.render(self.player1_name, 1, WHITE)
            WIN.blit(name, (prompt.get_width() + 20, 90))
        elif player == 2:
            name = SMALL_FONT.render(self.player2_name, 1, WHITE)
            WIN.blit(name, (prompt.get_width() + 20, 90))

    def draw_field_init_a(self, player):
        if player == 1:
            player_name = self.player1_name
        elif player == 2:
            player_name = self.player2_name
        field_text1 = SMALL_FONT.render(player_name + ", let's start by designing your field of plants.", 1, WHITE)
        WIN.blit(field_text1, (WIDTH//2 - field_text1.get_width()//2, 20))
        field_text2 = SMALL_FONT.render("You will have to customize " + str(Parameters.fieldSize) + " plants.", 1, WHITE)
        WIN.blit(field_text2, (WIDTH//2 - field_text2.get_width()//2, 70))
        field_text3 = SMALL_FONT.render("Press enter to continue.", 1, WHITE)
        WIN.blit(field_text3, (WIDTH//2 - field_text3.get_width()//2, 120))

    def draw_field_init_b(self, player):
        field_text1 = TINY_FONT.render("Each plant has four attributes:", 1, WHITE)
        WIN.blit(field_text1, (WIDTH//2 - field_text1.get_width()//2, 20))
        field_text2 = TINY_FONT.render("heat resistance, cold resistance, disease resistance, and strength.", 1, WHITE)
        WIN.blit(field_text2, (WIDTH//2 - field_text2.get_width()//2, 60))
        field_text3 = TINY_FONT.render("Before selecting your values, remember, they must all add up to 10.", 1, WHITE)
        WIN.blit(field_text3, (WIDTH//2 - field_text3.get_width()//2, 100))
        field_text4 = SMALL_FONT.render("Press enter to continue.", 1, WHITE)
        WIN.blit(field_text4, (WIDTH//2 - field_text4.get_width()//2, 140))

    def draw_field_init_c(self, player, stored_events):

        if player == 1:
            for event in stored_events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.draw_grid()
                        self.plant_counter1 += 1
                    # else:

            plant_init_text = SMALL_FONT.render("Initializing plant #" + str(self.plant_counter1) + ": ", 1, WHITE)
            WIN.blit(plant_init_text, (WIDTH//2 - plant_init_text.get_width()//2, 20))
            plant_init_text2 = SMALL_FONT.render("Press space to continue.", 1, WHITE)
            WIN.blit(plant_init_text2, (WIDTH//2 - plant_init_text2.get_width()//2, 70))

            

    def draw_window(self, event_marker, stored_events):
        if self.dont_draw_grid == False:
            self.draw_grid()
        if event_marker == "intro":
            self.draw_intro()
        elif event_marker == "name1":
            self.draw_name(1, stored_events)
        elif event_marker == "name2":
            self.draw_name(2, stored_events)
        elif event_marker == "field_init1a":
            self.draw_field_init_a(1)
        elif event_marker == "field_init1b":
            self.draw_field_init_b(1)
        elif event_marker == "field_init1c":
            self.draw_field_init_c(1, stored_events)
        elif event_marker == "field_init2a":
            self.draw_field_init_a(2)
        elif event_marker == "field_init2b":
            self.draw_field_init_b(2)
        elif event_marker == "field_init2c":
            self.draw_field_init_c(2, stored_events)

        pygame.display.update()

def main():
    event_marker = "intro"

    draw = Draw()
    
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)

        stored_events = []
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    if event_marker == "intro":
                        draw.draw_grid()
                        event_marker = "name1"
                    elif event_marker == "name1":
                        draw.draw_grid()
                        event_marker = "name2"
                    elif event_marker == "name2":
                       draw.draw_grid()
                       event_marker = "field_init1a"
                    elif event_marker == "field_init1a":
                        draw.draw_grid()
                        event_marker = "field_init1b"
                    elif event_marker == "field_init1b":
                        draw.draw_grid()
                        event_marker = "field_init1c"

                else:
                    stored_events.append(event)

        # print(event_marker)
        draw.draw_window(event_marker, stored_events)


main()