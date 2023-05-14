from mcpi.minecraft import Minecraft
import mcpi.block as block
import pygame
import BrushColors as BC
import UI
import pyquark

pix = 10
WH = 120 * pix
HT = 60 * pix
FPS = 60

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

menuWidth = 150
xBG = 120
yBG = 160

pygame.init()
screen = pygame.display.set_mode((WH, HT))
clock = pygame.time.Clock()
pygame.display.update()


def Reset():
    screen.fill(White)


def ResetMinecraft(mc):
    Reset()
    x1 = xBG - (WH // pix) + (menuWidth // pix)
    y1 = yBG - (HT // pix)
    playerX = xBG - ((WH // pix) // 2)
    playerY = yBG - ((HT // pix) // 2)
    playerZ = -70
    mc.setBlocks(xBG, yBG, 0, x1, y1, 0, block.Block(251))
    mc.player.setPos(playerX, playerY, playerZ)
    mc.setBlock(playerX, playerY - 1, playerZ, block.GRASS)


def ColorIcon(x, y, color, colorDark, action, argument, display):
    buttonColor = UI.Button(x=x, y=y, color=color, colorDark=colorDark, width=20, height=20, display=display)
    buttonColor.Render(size=5, text="", colorFront=(0, 0, 0), action=action, argument=argument)


def Back():
    return False


def PaintMinecraft():
    running = True
    mc = Minecraft.create()
    mc.setBlocks(200, 255, 0, -100, 100, 0, block.AIR)
    mc.postToChat("/weather clear")
    screen.fill(White)
    pygame.display.update()
    button = UI.Button(x=40, y=40, color=Green, colorDark=(0, 200, 0), width=80, height=40, display=screen)
    brush = BC.Brush(10, BC.colorDict, screen)
    BackButton = UI.Button(x=40, y=HT - 80, color=Green, colorDark=(0, 200, 0), width=80, height=40, display=screen)
    ResetMinecraft(mc)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.draw.rect(screen, Red, (0, 0, menuWidth, HT))
        pygame.draw.rect(screen, Black, (0, 0, menuWidth, HT), 2)
        ColorIcon(20, 100, Black, (25, 25, 25), brush.Color, "Black", screen)
        ColorIcon(60, 100, White, (240, 240, 240), brush.Color, "White", screen)
        ColorIcon(100, 100, Red, (240, 0, 0), brush.Color, "Red", screen)
        ColorIcon(20, 140, Blue, (0, 0, 240), brush.Color, "Blue", screen)
        ColorIcon(60, 140, Green, (0, 240, 0), brush.Color, "Green", screen)

        button.Render(15, "Reset", Blue, ResetMinecraft, mc)
        if BackButton.Render(15, "Back", Blue, Back) is False:
            return False
        brush.Render(menuWidth, xBG, yBG, mc, True)

        pygame.display.update()
        clock.tick(FPS)


#
def Paint():
    running = True
    screen.fill(White)
    pygame.display.update()
    button = UI.Button(x=40, y=40, color=Green, colorDark=(0, 200, 0), width=80, height=40, display=screen)
    brush = BC.Brush(10, BC.colorDict, screen)
    BackButton = UI.Button(x=40, y=HT - 80, color=Green, colorDark=(0, 200, 0), width=80, height=40, display=screen)
    Reset()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.draw.rect(screen, Red, (0, 0, menuWidth, HT))
        pygame.draw.rect(screen, Black, (0, 0, menuWidth, HT), 2)
        ColorIcon(20, 100, Black, (25, 25, 25), brush.Color, "Black", screen)
        ColorIcon(60, 100, White, (240, 240, 240), brush.Color, "White", screen)
        ColorIcon(100, 100, Red, (240, 0, 0), brush.Color, "Red", screen)
        ColorIcon(20, 140, Blue, (0, 0, 240), brush.Color, "Blue", screen)
        ColorIcon(60, 140, Green, (0, 240, 0), brush.Color, "Green", screen)

        button.Render(15, "Reset", Blue, Reset)
        if BackButton.Render(15, "Back", Blue, Back) is False:
            return False
        brush.Render(menuWidth, xBG, yBG)

        pygame.display.update()
        clock.tick(FPS)


def Expectations():
    running = True
    screen.fill(Red)
    BackButton = UI.Button(x=40, y=HT - 80, color=Green, colorDark=(0, 200, 0), width=80, height=40, display=screen)
    pyquark.filestart('../Minecraft/MinecraftTools/server/start.command')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        UI.CreateText(20, "Подождите пока загружается сервер", (WH // 2, HT // 2), Black, screen)
        try:
            Minecraft.create()
            running = False
            return True
        except:
            if BackButton.Render(15, "Back", Blue, Back) is False:
                return False
        pygame.display.update()
        clock.tick(FPS)


def Menu():
    running = True
    screen.fill(White)
    ButtonPaintMinecraft = UI.Button(x=WH // 2 - 100, y=HT // 2 - 150, color=Green, colorDark=(0, 200, 0), width=200,
                                     height=100, display=screen)
    ButtonPaint = UI.Button(x=WH // 2 - 100, y=HT // 2, color=Green, colorDark=(0, 200, 0), width=200,
                            height=100, display=screen)
    Quit = UI.Button(x=WH // 2 - 100, y=HT // 2 + 150, color=Green, colorDark=(0, 200, 0), width=200,
                     height=100, display=screen)
    while running:
        screen.fill(White)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        ButtonPaintMinecraft.Render(20, "Paint Minecraft", Black, StartPaintMinecraft)
        ButtonPaint.Render(20, "Paint", Black, Paint)
        Quit.Render(20, "Quit", Black, quit)
        pygame.display.update()
        clock.tick(FPS)


def StartPaintMinecraft():
    stop = True
    while stop:
        try:
            Minecraft.create()
        except:
            stop = Expectations()
        else:
            stop = PaintMinecraft()


Menu()
pygame.quit()
