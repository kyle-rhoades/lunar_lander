# Lunar Lander game by Mr. Rhoades
# Created in January 2024 for the wonderful students of Rouse Hill High School
# Includes assets created by Dizzy Cow: https://opengameart.org/content/apollo-moon-landing-sprites

# Import libraries
import sys
import pygame
import os

# Initialise PyGame
pygame.init()

# Declare constants
WIDTH, HEIGHT = 1024, 768
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lunar Lander")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

THRUSTER_SOUND = pygame.mixer.Sound('Assets/Sound Effects/ThrustLow.wav')

HUD_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VELOCITY = 5
LANDER_WIDTH, LANDER_HEIGHT = 30, 30
LANDER_DISPLAY_WIDTH, LANDER_DISPLAY_HEIGHT = 30, 33

LANDER_NO_THRUST_IMAGE = pygame.image.load(os.path.join('Assets', 'Lunar Lander - No Thrust.png'))
LANDER_LOW_THRUST_IMAGE = pygame.image.load(os.path.join('Assets', 'Lunar Lander - Low Thrust.png'))
LANDER_HIGH_THRUST_IMAGE = pygame.image.load(os.path.join('Assets', 'Lunar Lander - High Thrust.png'))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


# Update the display to show the current state of the game
def draw_window(lander, thruster_level, rotation):
    # Draw window background
    WINDOW.blit(BACKGROUND, (0, 0))

    # Draw lander
    if thruster_level == 0:
        lander_image = LANDER_NO_THRUST_IMAGE
    elif thruster_level == 1:
        lander_image = LANDER_LOW_THRUST_IMAGE
    else:
        lander_image = LANDER_HIGH_THRUST_IMAGE

    # Rotate the lander image around the center
    # See: https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
    lander_surface = pygame.transform.rotate(pygame.transform.scale(
        lander_image, (LANDER_DISPLAY_WIDTH, LANDER_DISPLAY_HEIGHT)), rotation)
    new_rect = lander_surface.get_rect(center=lander.center)
    WINDOW.blit(lander_surface, new_rect)

    pygame.display.update()


def handle_lander_movement(keys_pressed, lander, rotation):
    thruster_level = 0
    if keys_pressed[pygame.K_a] and lander.x - VELOCITY > 0:  # LEFT
        #lander.x -= VELOCITY
        rotation -= VELOCITY
        thruster_level = 2
    if keys_pressed[pygame.K_d] and lander.x + VELOCITY + lander.width < WIDTH:  # RIGHT
        #lander.x += VELOCITY
        thruster_level = 2
        rotation += VELOCITY
    if keys_pressed[pygame.K_w] and lander.y - VELOCITY > 0:  # UP
        lander.y -= VELOCITY
        thruster_level = 2
    if keys_pressed[pygame.K_s] and lander.y + VELOCITY + lander.height < HEIGHT:  # DOWN
        lander.y += VELOCITY
        thruster_level = 2
    return thruster_level, rotation

# Main lunar lander game function
def lunar_lander():
    lander = pygame.Rect(WIDTH//2 - LANDER_WIDTH//2, LANDER_HEIGHT, LANDER_WIDTH, LANDER_HEIGHT)
    rotation = 0

    # Game loop
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit game
                run = False
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        thruster_level, rotation = handle_lander_movement(keys_pressed, lander, rotation)

        # Update the display to show the current state of the game
        draw_window(lander, thruster_level, rotation)

    # Play again
    lunar_lander()

if __name__ == '__main__':
    lunar_lander()
