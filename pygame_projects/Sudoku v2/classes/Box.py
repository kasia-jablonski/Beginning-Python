import pygame
from constants.colors import BLACK_COLOR, FILL_COLOR, BACKGROUND_COLOR

class Box(object):
    def __init__(self, screen, font, x, y, value):
        self.x = x
        self.y = y
        self.width = 39
        self.height = 39
        self.value = value
        self.clickable = True
        self.set_initial_value(screen, font, value)
        self.draw_box(screen)

    def get_x_y(self):
        return self.x / 40, ' - ', self.y / 40

    def set_initial_value(self, screen, font, value):
        self.value = value
        if value != 0:
            self.clickable = False

            self.highlight_box(screen, font, FILL_COLOR)

            self.set_number(screen, font)

    def set_number(self, screen, font):
        if self.value != 0:
            number = font.render(str(int(self.value)), True, (0, 0, 0))
            screen.blit(
                number,
                (
                    self.x + 10,
                    self.y + 5 
                )
            )
    def erase_number(self, screen, font):
        self.value = 0
        self.highlight_box(screen, font, BACKGROUND_COLOR)

    def draw_box(self, screen):
        pygame.draw.rect(
            screen, BLACK_COLOR, pygame.Rect(self.x, self.y, 40, 40), 1
        )

    def clicked_box(self, screen, clicked_x, clicked_y):
        if self.clickable:
            return (clicked_x >= self.x and (clicked_x <= self.x + self.width)) and (clicked_y >= self.y and (clicked_y <= self.y + self.height))
        return False

    def highlight_box(self, screen, font, color):
        if self.clickable:
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(
                screen,
                FILL_COLOR,
                pygame.Rect(self.x, self.y, self.width, self.height))
        number = font.render(str(int(self.value)), True, (0, 0, 0))
        self.set_number(screen, font)

    def on_click(self, screen, font, value):
        if isinstance(value, int):
            number = font.render(str(value), True, (0, 0, 0))
            self.value = value
            self.set_number(screen, font)
