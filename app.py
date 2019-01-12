import pygame
from pygame.locals import *
from Game import Cards


class Tile(pygame.sprite.Sprite):
    def __init__(self, index, card, font_size, font_color, bg_color, width, height, border, border_color, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        # Set properties
        self.index = index
        self.card = card
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.border = border
        self.border_color = border_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        # Build tile
        self.font = pygame.font.SysFont("Arial", font_size)
        self.text = self.font.render(card.get_facedown(), 1, font_color)
        self.surf = pygame.Surface((width, height))
        self.surf.fill(border_color)
        self.image = pygame.Surface((width - border * 2, height - border * 2))
        self.image.fill(bg_color)
        self.rect = pygame.Rect(x_pos + border, y_pos + border, width, height)
        self.image.blit(self.text, [width/2 - self.text.get_width()/2, height/2 - self.text.get_height()/2])
        self.surf.blit(self.image, [border, border])

    def update(self, *args):
        self.text = self.font.render(self.card.get_value(), 1, self.font_color)
        self.image.fill(self.bg_color)
        self.image.blit(self.text, [self.width/2 - self.text.get_width()/2, self.height/2 - self.text.get_height()/2])


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
        self.padding = 20

    def get_dimensions(self):
        return self.tile_width * self.grid_x + self.padding * 2, self.tile_height * self.grid_y + self.padding * 2


def main():

    # Get settings
    settings = Settings()

    # Initialize pygame
    pygame.init()

    # create the screen object
    screen = pygame.display.set_mode(settings.get_dimensions())
    screen.fill(settings.bg_color)

    # Build tiles
    cards_game = Cards.Cards(settings.unique_tiles)
    cards = cards_game.get_cards()
    tiles = pygame.sprite.LayeredUpdates()
    x = 0
    y = 0
    index = 0
    while y < settings.grid_y:
        while x < settings.grid_x:
            tiles.add(Tile(
                index + 1,
                cards[index + 1],
                settings.tile_font_size,
                settings.tile_font_color,
                settings.tile_bg_color,
                settings.tile_width,
                settings.tile_height,
                settings.tile_border,
                settings.tile_border_color,
                settings.tile_width * x + settings.padding,
                settings.tile_height * y + settings.padding
            ))
            x += 1
            index += 1
        x = 0
        y += 1

    # Variable to keep our main loop running
    running = True

    # Variables to control tile animations
    wait = False
    flip_back = False

    # Our main loop!
    while running:

        # For loop through the event queue
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

        # Handle game state.
        if wait:
            wait = False
            pygame.time.wait(1000)
        elif flip_back:
            flip_back = False
            cards_game.hide_cards()
            tiles.update()
            wait = True
        else:
            # Handle click on card event
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                for tile in tiles.get_sprites_at(mouse):
                    status = cards_game.play(tile.index)
                    if not status == 'invalid_card':
                        tile.update()
                        if status == 'not_a_match':
                            flip_back = True

        pygame.display.flip()

    pygame.time.wait(1000)
    pygame.quit()


# Call the "main" function if running this script
if __name__ == '__main__':
    main()
