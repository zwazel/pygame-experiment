import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello, Pygame World!")

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white color

    # Draw "Hello, World!" on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, Pygame World!", True, (0, 0, 0))  # Render text in black color
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
