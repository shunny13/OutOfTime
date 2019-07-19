import pygame


class Ennemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imgs = []
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

    def draw(self, win):
        """
        Draws ennemy with given images
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Return if position has hit the Ennemy
        :param x:  init
        :par
        """
        if (X <= self.x + self.width and self.X >= self.x):
            if(Y <= self.y + self.height and Y >= self.y):
                return True

    def move(self):
        pass

    def ok(self):
        pass

    def hit(self):
        """
        Returns if ennemy died and return true if it's the case
        """
        self.health -= 1
        if self.health <= 0:
            return True
