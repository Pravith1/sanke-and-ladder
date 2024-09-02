import pygame

def draw_dice(display, number, background_color, foreground_color, size):
    x, y, w, h = 605, 50, 190, 190
    pygame.draw.rect(display, background_color, (x, y, w, h))
    draw_dot = {
        1: lambda: pygame.draw.circle(display, foreground_color, (x + w // 2, y + h // 2), size),
        2: lambda: [pygame.draw.circle(display, foreground_color, (x + w // 4, y + h // 2), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 2), size)],
        3: lambda: [pygame.draw.circle(display, foreground_color, (x + w // 4, y + 3 * h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 2, y + h // 2), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 4), size)],
        4: lambda: [pygame.draw.circle(display, foreground_color, (x + w // 4, y + h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 4, y + 3 * h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + 3 * h // 4), size)],
        5: lambda: [pygame.draw.circle(display, foreground_color, (x + w // 2, y + h // 2), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 4, y + h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 4, y + 3 * h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 4), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + 3 * h // 4), size)],
        6: lambda: [pygame.draw.circle(display, foreground_color, (x + w // 4, y + h // 2), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 2), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 4, y + h // 4 - 10), size),
                    pygame.draw.circle(display, foreground_color, (x + w // 4, y + 3 * h // 4 + 10), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + h // 4 - 10), size),
                    pygame.draw.circle(display, foreground_color, (x + 3 * w // 4, y + 3 * h // 4 + 10), size)]
    }
    draw_dot[number]()
