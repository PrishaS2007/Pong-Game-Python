import pygame
import sys
import random

pygame.init()

# Constants
screen_width, screen_height = 800, 600
paddle_width, paddle_height = 10, 100
ball_size = 20
white = (255, 255, 255)
black = (0, 0, 0)
paddle_speed = 7
ball_x_speed = 5 
ball_y_speed = 5   

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Paddle positions
player1_pos = pygame.Rect(50, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
player2_pos = pygame.Rect(screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Ball variables
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)
ball_dx = random.choice([-1, 1]) * ball_x_speed
ball_dy = random.choice([-1, 1]) * ball_y_speed

# Font
font = pygame.font.Font(None, 36)

# Function to display text on screen
def display_text(text, x, y):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to reset the game
def reset_game():
    global ball_dx, ball_dy
    ball.center = (screen_width // 2, screen_height // 2)
    ball_dx = random.choice([-1, 1]) * ball_x_speed
    ball_dy = random.choice([-1, 1]) * ball_y_speed
    player1_pos.center = (50, screen_height // 2)
    player2_pos.center = (screen_width - 50, screen_height // 2)

# Game loop
game_over = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_pos.top > 0:
            player1_pos.move_ip(0, -paddle_speed)  # Move player 1 paddle up
        if keys[pygame.K_s] and player1_pos.bottom < screen_height:
            player1_pos.move_ip(0, paddle_speed)   # Move player 1 paddle down
        if keys[pygame.K_UP] and player2_pos.top > 0:
            player2_pos.move_ip(0, -paddle_speed)  # Move player 2 paddle up
        if keys[pygame.K_DOWN] and player2_pos.bottom < screen_height:
            player2_pos.move_ip(0, paddle_speed)   # Move player 2 paddle down

        # Move the ball
        ball.move_ip(ball_dx, ball_dy)

        # Check collisions with walls
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_dy = -ball_dy

        # Check collisions with paddles
        if ball.colliderect(player1_pos) or ball.colliderect(player2_pos):
            ball_dx = -ball_dx

        # Check if ball goes out of bounds
        if ball.left <= 0:
            game_over = True
            winner_text = "Player 2 Wins!"
        elif ball.right >= screen_width:
            game_over = True
            winner_text = "Player 1 Wins!"

    else:
        keys = pygame.key.get_pressed()
        if any(keys):
            game_over = False
            reset_game()

    # Clear screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, player1_pos)
    pygame.draw.rect(screen, white, player2_pos)
    pygame.draw.ellipse(screen, white, ball)

    # Display game over text
    if game_over:
        display_text("GAME OVER", screen_width // 2, screen_height // 2 - 50)
        display_text("Press any key to continue", screen_width // 2, screen_height // 2 + 50)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()