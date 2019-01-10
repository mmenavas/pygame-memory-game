import time
import pygame
from pygame.locals import *
from Game import Cards


class Tile(pygame.sprite.Sprite):
    def __init__(self, text, size, color, bg_color, width, height, border, border_color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.surf = pygame.Surface((width, height))
        self.surf.fill(border_color)
        self.image = pygame.Surface((width - border * 2, height - border * 2))
        self.image.fill(bg_color)
        w = self.textSurf.get_width()
        h = self.textSurf.get_height()
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, width, height)
        self.image.blit(self.textSurf, [width/2 - w/2, height/2 - h/2])
        self.surf.blit(self.image, [border, border])

class Settings:
    def __init__(self):
        self.unique_tiles = 8
        self.grid_x = 4
        self.grid_y = 4
        self.tile_width = 200
        self.tile_height = 200
        self.bg_color = (128, 128, 128)
        self.tile_bg_color = (255, 255, 255)
        self.tile_font_color = (255, 87, 51)
        self.tile_font_size = 160
        self.tile_border = 5
        self.tile_border_color = (128, 128, 128)

    def get_dimensions(self):
        return self.tile_width * self.grid_x, self.tile_height * self.grid_y


# Get settings
settings = Settings()

# Initialize pygame
pygame.init()

# create the screen object
screen = pygame.display.set_mode(settings.get_dimensions())
screen.fill(settings.bg_color)

# Build tiles
# cards = Cards.Cards(settings.unique_tiles)
# tiles = pygame.sprite.Group()
# for index, card in cards.get_cards().items():
#     tiles.add(Tile(
#         str(card.get_value()),
#         settings.tile_font_size,
#         settings.tile_font_color,
#         settings.tile_bg_color,
#         settings.tile_width,
#         settings.tile_height,
#         settings.tile_border,
#         settings.tile_border_color
#     ))

tiles = pygame.sprite.LayeredUpdates()
x = 0
y = 0
index = 0
while y < settings.grid_y:
    while x < settings.grid_x:
        coordinates = (x * settings.tile_width, y * settings.tile_height)
        # screen.blit(tiles.get_sprite(index).surf, coordinates)
        tiles.add(Tile(
            "?",
            settings.tile_font_size,
            settings.tile_font_color,
            settings.tile_bg_color,
            settings.tile_width,
            settings.tile_height,
            settings.tile_border,
            settings.tile_border_color,
            settings.tile_width * x,
            settings.tile_height * y
        ))
        x += 1
        index += 1
    x = 0
    y += 1

# Variable to keep our main loop running
running = True

# Our main loop!
while running:

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False

    tiles.draw(screen)

    # Show a single tile
    # coordinates = ((15 % settings.grid_x) * settings.tile_width, (15 % settings.grid_y) * settings.tile_height)
    # screen.blit(tiles[15].surf, coordinates)

    # Get mouse data
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Handle mouse click
    # if item.image.get_rect().collidepoint(mouse):
    items = len(tiles.get_sprites_at(mouse))
    if items:
        if click[0] == 1:
            print("Tile {}".format(items))
    # else:
    #     pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    # # Update the display
    pygame.display.flip()

# TODO: Learn how to use rectangles and surface
# sprites_clicked = [sprite for sprite in all_my_sprites_list if sprite.rect.collidepoint(x, y)]

