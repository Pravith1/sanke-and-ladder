import pygame
import random
class Player:
    def __init__(self, board, color):
        self.val = 100
        self.color = color
        self.size = random.randint(15, 25)
        self.board = board
        self._update_position()

    def _update_position(self):
        for row in self.board.boardarr:
            for cell in row:
                if self.val == cell[2]:
                    self.xpos, self.ypos = cell[0], cell[1]

    def move(self, steps):
        if self.val - steps > 0:
            self.val -= steps
        if self.val == 1:
            print("+=+" * 10 + " YOU WIN " + "+=+" * 10)
            global game_over
            game_over = True
        self._update_position()

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.xpos + 30, self.ypos + 30), self.size)
