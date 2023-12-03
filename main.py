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
player_y = height - player_size - 10  # Start position near the bottom
player_lane_positions = [width // 4, width // 2, 3 * width // 4]  # Set positions for three lanes
current_lane = 1  # Start in the middle lane

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

        # Collision detection
        red_rect = pygame.Rect(red_square_x, red_square_y, red_square_size, red_square_size)

        if red_rect.colliderect(player_lane_positions[current_lane], player_y, player_size, player_size):
            print("Collision!")

            # Reset the position of the red square
            red_square_y = 10

            # Switch back to the menu state
            current_state = MENU

        # Clear the screen
        screen.fill(white)

        # Draw the red square
        pygame.draw.rect(screen, red_square_color, (red_square_x, red_square_y, red_square_size, red_square_size))

        # Draw the player square in the current lane
        pygame.draw.rect(screen, player_color,
                         (player_lane_positions[current_lane], height - player_size - 10, player_size, player_size))

        # Update the display
        pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
