import sys

import pygame

global width, height
width, height = 800, 600


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, size, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            self.rect.y = -self.rect.height


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Experiment")
    background_image = pygame.image.load("res/bg.png")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Set up the clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Define game states
    MENU = 0
    GAME = 1
    current_state = MENU

    spaceship = Spaceship("res/SpaceShip.png", (75, 75), width // 2 - 37.5, height - 100, 5)
    asteroid = Asteroid("res/Asteroid1.png", (75, 75), width // 2 - 37.5, 10, 5)

    all_sprites = pygame.sprite.Group(spaceship, asteroid)

    # Set up the vertical lines
    line1_x = width // 5
    line2_x = 4 * width // 5
    line_width = 10

    # Define the start button
    button_rect = pygame.Rect(width // 2 - 100, height // 2 - 30, 200, 60)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if button_rect.collidepoint(x, y) and current_state == MENU:
                    # Switch to the game state when the user clicks the button in the main menu
                    current_state = GAME

        # Main menu
        if current_state == MENU:
            screen.blit(background_image, (0, 0))
            pygame.draw.rect(screen, black, button_rect)
            text = font.render("Start", True, white)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        # Game state
        elif current_state == GAME:
            # Move the Spaceship
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT] and spaceship.rect.x > 0:
                spaceship.rect.x -= spaceship.speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT] and spaceship.rect.x < width - spaceship.rect.width:
                spaceship.rect.x += spaceship.speed

            # Ensure the player stays centered between the two lines
            if spaceship.rect.x < line1_x:
                spaceship.rect.x = line1_x
            elif spaceship.rect.x + spaceship.rect.width > line2_x:
                spaceship.rect.x = line2_x - spaceship.rect.width
            # Collision detection
            if pygame.sprite.spritecollide(spaceship, [asteroid], False):
                asteroid.rect.y = 10
                spaceship.rect.x = width // 2 - spaceship.rect.width // 2
                spaceship.rect.y = height - spaceship.rect.height - 10
                # Switch back to the menu state
                current_state = MENU


            screen.blit(background_image, (0, 0))

            # Draw the vertical lines
            pygame.draw.rect(screen, black, (line1_x - line_width // 2, 0, line_width, height))
            pygame.draw.rect(screen, black, (line2_x - line_width // 2, 0, line_width, height))

            all_sprites.update()
            all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)


if __name__ == '__main__':
    main()
