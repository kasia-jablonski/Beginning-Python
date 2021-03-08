import pygame
from constants.colors import BLACK_COLOR
eraser = pygame.image.load('eraser.png')

class Button(object):
    def __init__(self, x, y, button_number):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 55
        self.selected = False
        self.button_number = button_number
        self.type = 'button'

    def clicked_button(self, clicked_x, clicked_y):
        return (clicked_x >= self.x and clicked_x <= self.x + self.width) and (clicked_y >= self.y and clicked_y <= self.y + self.height)

    def print_button_number(self):
        print(self.button_number)

    def select_button(self, screen):
        self.selected = True
        pygame.draw.rect(
            screen, BLACK_COLOR, pygame.Rect(self.x + 1, self.y + 1, self.width - 3, self.height - 3), 3
        )

class Numeric_Button(Button):
    def __init__(self, screen, font, x, y, button_number):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 55
        self.selected = False
        self.button_number = button_number
        self.draw_button(screen, font)
        self.type = 'numeric'

    def draw_button(self, screen, font):
        self.selected = False
        pygame.draw.rect(
            screen, (183, 166, 173), pygame.Rect(self.x, self.y, self.width, self.height)
        )
        number = font.render(str(self.button_number), True, (0, 0, 0))
        screen.blit(number, (self.x + 13, self.y + 7))

class Erase_Button(Button):
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 55
        self.selected = False
        self.button_number = ''
        self.draw_button(screen)
        self.type = 'eraser'

    def draw_button(self, screen):
        self.selected = False
        pygame.draw.rect(
            screen, (183, 166, 173), pygame.Rect(self.x, self.y, self.width, self.height)
        )
        screen.blit(eraser, (self.x - 8, self.y - 3))
        