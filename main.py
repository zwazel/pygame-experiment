import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Squares")

# Set up the red square
red_square_size = 50
red_square_color = (255, 0, 0)  # Red
red_square_x = width // 2 - red_square_size // 2
red_square_y = 10  # Start position near the top
red_square_speed = 5

# Set up the black square
black_square_size = 50
black_square_color = (0, 0, 0)  # Black
black_square_x = width // 2 - black_square_size // 2
black_square_y = height - black_square_size - 10  # Start position near the bottom
black_square_speed = 5

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white color

    # Draw the red square
    pygame.draw.rect(screen, red_square_color, (red_square_x, red_square_y, red_square_size, red_square_size))

    # Draw the black square
    pygame.draw.rect(screen, black_square_color, (black_square_x, black_square_y, black_square_size, black_square_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)