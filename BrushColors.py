import pygame
import mcpi.block as block

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
colorDict = {"Black": [Black, block.Block(251, 15)], "Red": [Red, block.Block(251, 14)],
             "White": [White, block.Block(251)],
             "Green": [Green, block.Block(251, 13)], "Blue": [Blue, block.Block(251, 10)]}


class Brush:
    color = (255, 255, 255)
    block = block.Block(251)

    def __init__(self, size=0, color_dict=None, display=None):
        self.colorDict = color_dict
        self.size = size
        self.display = display

    def Render(self, menuWidth, StartPointX=0, StartPointY=0,mc= None,PaintMinecraftBool = False):
        posMouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pos_X = int((posMouse[0] // self.size) * self.size)
        pos_Y = int((posMouse[1] // self.size) * self.size)
        if click[0] == 1 and pos_X >= menuWidth:
            pygame.draw.rect(self.display, self.color, (pos_X, pos_Y, self.size, self.size))
            if PaintMinecraftBool:
                mc.setBlock((-pos_X // self.size) + StartPointX + (menuWidth // self.size),
                            (-pos_Y // self.size) + StartPointY, 0, self.block)

    def Color(self, textColor: str):
        self.color = self.colorDict[textColor][0]
        self.block = self.colorDict[textColor][1]
