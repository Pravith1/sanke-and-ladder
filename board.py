import pygame
import random
from utils import text_objects

DARK_BACKGROUND = (53, 53, 53)
FOREGROUND_COLOR = (255, 138, 119) 
class Board:
    def __init__(self):
        self.boardarr = []
        count = 1
        for i in range(10):
            temp = []
            for j in range(10):
                x = j * 60
                y = i * 60
                temp.append((x, y, count))
                count += 1
            self.boardarr.append(temp)

        self.ladders = []
        self.countarr = [100, 1]
        nooflad = random.randint(4, 8)
        self._generate_random_ladders(nooflad)

        self.snakes = []
        noofsnk = random.randint(4, 8)
        self._generate_random_snakes(noofsnk)


    def _generate_random_ladders(self, nooflad):
        for _ in range(nooflad):
            while True:
                rand1, rand2 = random.randint(1, 100), random.randint(1, 100)
                if abs(rand1 - rand2) > 10 and rand1 not in self.countarr and rand2 not in self.countarr:
                    self.countarr.extend([rand1, rand2])
                    break
            a, b = self._find_coordinates(rand1), self._find_coordinates(rand2)
            self.ladders.append((a, b))

    def _generate_random_snakes(self, noofsnk):
        for _ in range(noofsnk):
            while True:
                rand1, rand2 = random.randint(1, 100), random.randint(1, 100)
                if abs(rand1 - rand2) > 10 and rand1 not in self.countarr and rand2 not in self.countarr:
                    self.countarr.extend([rand1, rand2])
                    break
            a, b = self._find_coordinates(rand1), self._find_coordinates(rand2)
            self.snakes.append([a, b])

    def _find_coordinates(self, value):
        for row in self.boardarr:
            for cell in row:
                if cell[2] == value:
                    return cell

    def draw(self, display, color1, color2, snake_color, ladder_color):
        for row in self.boardarr:
            for cell in row:
                color = color1 if cell[2] % 2 == 0 else color2
                pygame.draw.rect(display, color, (cell[0], cell[1], 59, 59))
                small_text = pygame.font.SysFont("comicsansms", 20)
                text_surf, text_rect = text_objects(str(cell[2]), small_text, FOREGROUND_COLOR)
                text_rect.center = (cell[0] + 30, cell[1] + 30)
                display.blit(text_surf, text_rect)

        for ladder in self.ladders:
            pygame.draw.line(display, ladder_color, (ladder[0][0] + 20, ladder[0][1] + 30), (ladder[1][0] + 20, ladder[1][1] + 30), 3)
            pygame.draw.line(display, ladder_color, (ladder[0][0] + 40, ladder[0][1] + 30), (ladder[1][0] + 40, ladder[1][1] + 30), 3)

        for snake in self.snakes:
            pygame.draw.line(display, snake_color, (snake[0][0] + 30, snake[0][1] + 30), (snake[1][0] + 30, snake[1][1] + 30), 8)
