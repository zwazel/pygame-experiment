import sys

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

# Set up fonts
font = pygame.font.Font(None, 36)

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define game states
MENU = 0
GAME = 1
current_state = MENU

# Set up the red square
red_square_size = 50
red_square_color = red
red_square_x = width // 2 - red_square_size // 2
red_square_y = 10  # Start position near the top
red_square_speed = 5

# Set up the black square
black_square_size = 50
black_square_color = black
black_square_x = width // 2 - black_square_size // 2
black_square_y = height - black_square_size - 10  # Start position near the bottom
black_square_speed = 5

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
        screen.fill(white)
        pygame.draw.rect(screen, black, button_rect)
        text = font.render("Start", True, white)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    # Game state
    elif current_state == GAME:
        # Move the red square down
        red_square_y += red_square_speed

        # Wrap around to the top when the red square goes off the bottom of the screen
        if red_square_y > height:
            red_square_y = -red_square_size

        # Move the black square based on keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and black_square_x > 0:
            black_square_x -= black_square_speed
        if keys[pygame.K_d] and black_square_x < width - black_square_size:
            black_square_x += black_square_speed

        # Collision detection
        red_rect = pygame.Rect(red_square_x, red_square_y, red_square_size, red_square_size)
        black_rect = pygame.Rect(black_square_x, black_square_y, black_square_size, black_square_size)

        if red_rect.colliderect(black_rect):
            # Reset the positions of both squares
            red_square_y = 10
            black_square_x = width // 2 - black_square_size // 2
            black_square_y = height - black_square_size - 10

            # Switch back to the menu state
            current_state = MENU

        # Clear the screen
        screen.fill(white)

        # Draw the red square
        pygame.draw.rect(screen, red_square_color, (red_square_x, red_square_y, red_square_size, red_square_size))

        # Draw the black square
        pygame.draw.rect(screen, black_square_color, (black_square_x, black_square_y, black_square_size,
                                                      black_square_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
