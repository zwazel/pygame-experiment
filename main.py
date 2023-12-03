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

# Set up the player square
player_size = 50
player_color = black
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10  # Start position near the bottom
player_speed = 65  # Discrete movement between three vertical lines

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

        # Move the player square based on keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_d] and player_x < width - player_size:
            player_x += player_speed

        # Collision detection
        red_rect = pygame.Rect(red_square_x, red_square_y, red_square_size, red_square_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        if red_rect.colliderect(player_rect):
            print("Collision!")

            # Reset the positions of both squares
            red_square_y = 10
            player_x = width // 2 - player_size // 2

            # Switch back to the menu state
            current_state = MENU

        # Clear the screen
        screen.fill(white)

        # Draw the red square
        pygame.draw.rect(screen, red_square_color, (red_square_x, red_square_y, red_square_size, red_square_size))

        # Draw the player square
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

        # Draw the three vertical lines
        pygame.draw.line(screen, black, (width // 4, 0), (width // 4, height), 2)
        pygame.draw.line(screen, black, (width // 2, 0), (width // 2, height), 2)
        pygame.draw.line(screen, black, (3 * width // 4, 0), (3 * width // 4, height), 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
