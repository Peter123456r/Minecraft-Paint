import pygame


def CreateText(size, text, rect=(0, 0), color_font=(0, 0, 0), display=None):
    f = pygame.font.SysFont('arial', size)
    text_f = f.render(str(text), True, color_font)
    poz = text_f.get_rect(center=rect)
    return display.blit(text_f, poz)


class Button:
    def __init__(self, x=0, y=0, color=(255, 255, 255), colorDark=(240, 240, 240), width=50, height=30, display=None):
        self.x = x
        self.y = y
        self.color = color
        self.colorDark = colorDark
        self.width = width
        self.height = height
        self.display = display

    def Render(self, size, text, colorFront, action=None, argument=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(self.display, self.colorDark, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and action is not None:
                if argument is not None:
                    return action(argument)
                else:
                    return action()
        else:
            pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))
        CreateText(size, text, self.Center(), color_font=colorFront, display=self.display)
        pygame.draw.rect(self.display, (0, 0, 0), (self.x, self.y, self.width + 1, self.height + 1), 1)

    def Center(self):
        xCenter = (self.width / 2) + self.x
        yCenter = (self.height / 2) + self.y
        center = (xCenter, yCenter)
        return center
