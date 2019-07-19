import pygame
import sys
# import player


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.ennemies = []
        # self.player = Player()
        self.bg1 = pygame.image.load(os.path.join("assets", "lvl/b1.png"))
        self.bg2 = pygame.image.load(os.path.join("assets", "lvl/b2.png"))
        self.bg3 = pygame.image.load(os.path.join("assets", "lvl/b3.png"))
        self.bg4 = pygame.image.load(os.path.join("assets", "lvl/b4.png"))

   def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg1(0, 0))
        self.win.blit(self.bg2(0, 0))
        self.win.blit(self.bg3(0, 0))
        self.win.blit(self.bg4(0, 0))
        pygame.display.update()
