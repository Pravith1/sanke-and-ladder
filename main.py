import pygame
import random
from board import Board
from player import Player
from dice import draw_dice
from utils import text_objects

# Initialize Pygame
pygame.init()

# Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
SIZE = 25

# Colors
BACKGROUND_COLOR = (70, 130, 180)
FOREGROUNDS = (255, 215, 0)
DARK_BACKGROUND = (25, 25, 112)
BOARD_COLOR1 = (255, 239, 191)
BOARD_COLOR2 = (255, 223, 186)
SNAKE_COLOR = (0, 255, 0)
LADDER_COLOR = (255, 0, 0)
PLAYER1_COLOR = (0, 191, 255)
PLAYER2_COLOR = (255, 105, 180)

# Setup display
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake and Ladder')
clock = pygame.time.Clock()

def winner(turn):
    pygame.draw.rect(game_display, BACKGROUND_COLOR, (95, 95, 610, 410))
    pygame.draw.rect(game_display, DARK_BACKGROUND, (100, 100, 600, 400))
    pygame.draw.rect(game_display, BACKGROUND_COLOR, (105, 105, 590, 390))

    small_text = pygame.font.SysFont("comicsansms", 90)
    text_surf, text_rect = text_objects("GAME OVER", small_text, DARK_BACKGROUND)
    text_rect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 100)
    game_display.blit(text_surf, text_rect)

    small_text = pygame.font.SysFont("comicsansms", 50)
    text_surf, text_rect = text_objects("WINNER:", small_text, DARK_BACKGROUND)
    text_rect.center = (DISPLAY_WIDTH // 4 + 100, DISPLAY_HEIGHT // 2 + 100)
    game_display.blit(text_surf, text_rect)

    small_text1 = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects("Hit Space to Play", small_text1, DARK_BACKGROUND)
    text_rect.center = (700, 580)
    game_display.blit(text_surf, text_rect)

    color = PLAYER2_COLOR if turn == 1 else PLAYER1_COLOR
    pygame.draw.circle(game_display, color, (DISPLAY_WIDTH * 3 // 4, DISPLAY_HEIGHT // 2 + 100), 60)

    pygame.display.update()
    wait_for_space()

def wait_for_space():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def main():
    game_display.fill(BACKGROUND_COLOR)
    board = Board()
    player1 = Player(board, PLAYER1_COLOR)
    player2 = Player(board, PLAYER2_COLOR)
    turn = 1
    roll = False
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll = not roll

        if not game_over:
            board.draw(game_display, BOARD_COLOR1, BOARD_COLOR2, SNAKE_COLOR, LADDER_COLOR)
            player1.draw(game_display)
            player2.draw(game_display)
            small_text = pygame.font.SysFont("comicsansms", 40)
            text_surf, text_rect = text_objects("Turn", small_text, DARK_BACKGROUND, BACKGROUND_COLOR)
            text_rect.center = (700, 300)
            game_display.blit(text_surf, text_rect)
            small_text1 = pygame.font.SysFont("comicsansms", 20)
            text_surf, text_rect = text_objects("Hit Space to Play", small_text1, DARK_BACKGROUND, BACKGROUND_COLOR)
            text_rect.center = (700, 500)
            game_display.blit(text_surf, text_rect)

            if roll:
                dice_number = random.randint(1, 6)
                draw_dice(game_display, dice_number, DARK_BACKGROUND, FOREGROUNDS, SIZE)
                pygame.display.update()
                pygame.time.wait(1000)

                if turn == 1:
                    player1.move(dice_number)
                    turn = 2
                else:
                    player2.move(dice_number)
                    turn = 1

                if player1.val == 1 or player2.val == 1:
                    game_over = True
                    winner(turn)
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
