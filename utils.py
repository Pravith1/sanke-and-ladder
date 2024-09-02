import pygame

def text_objects(text, font, color, background_color=None):
    if background_color:
        text_surface = font.render(text, True, color, background_color)
    else:
        text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()
