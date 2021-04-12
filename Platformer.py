# Game Template
import pygame as pg
import random
from PlatformerSettings import *
from Sprites import *



class Game():
    def __init__(self):
        # Initializes pygame and creates the window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.gameRunning = True

    def new(self):
        # Starting a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # Creating a new player sprite from the sprites file
        self.player = Player(self)
        self.all_sprites.add(self.player)
        plat1 = Platforms(0, HEIGHT - 60, WIDTH, 40)
        self.all_sprites.add(plat1)
        self.platforms.add(plat1)
        self.run()

    def run(self):
        # when the game is running/game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # For the game to update
        self.all_sprites.update()

        #Collision check between the player and platforms
        collision = pg.sprite.spritecollide(self.player, self.platforms, False)
        if collision:
            # the player's y position will be set to the top part of the platform
            self.player.pos.y = collision[0].rect.top
            self.player.vel.y = 0


    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False  # stops the game running loop and ends the game
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # drawing on the screen
        self.screen.fill(GREY)
        self.all_sprites.draw(self.screen)
        # This comes after drawing all the time
        pg.display.flip()

    def game_start_screen(self):
        pass

    def gameover_screen(self):
        pass


game = Game()
game.game_start_screen()
while game.gameRunning:
    game.new()
    game.game_start_screen()
pg.quit()
