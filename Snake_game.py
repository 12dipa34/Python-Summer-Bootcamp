import pygame  # Import the pygame library
import random  # Import the random library

pygame.init()  # Initialize all imported pygame modules

# Define colors using RGB tuples
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the dimensions of the display window
dis_width = 800
dis_height = 600

# Create the display window with the specified width and height
dis = pygame.display.set_mode((dis_width, dis_height))
# Set the title of the window
pygame.display.set_caption('Snake Game by Gajendra verma')

clock = pygame.time.Clock()  # Create a clock object to control the frame rate
snake_block = 20  # Define the size of each block of the snake and food
snake_speed = 10  # Set the speed of the snake

# Load fonts for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score on the screen
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Function to draw the snake on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Main game loop function
def gameLoop():
    game_over = False  # Flag to indicate if the game is over
    game_close = False  # Flag to indicate if the game is close to being over

    # Initial position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial movement direction of the snake
    x1_change = 0
    y1_change = 0

    snake_List = []  # List to store the coordinates of the snake's body
    Length_of_snake = 1  # Initial length of the snake

    # Randomly generate the position of the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

    while not game_over:  # Main game loop
        while game_close:  # Loop for when the game is close to being over
            dis.fill(blue)  # Fill the display with blue color
            your_score(Length_of_snake - 1)  # Display the score
            pygame.display.update()  # Update the display

            for event in pygame.event.get():  # Handle events
                if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                    if event.key == pygame.K_q:  # If 'Q' is pressed, quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # If 'C' is pressed, restart the game
                        gameLoop()

        for event in pygame.event.get():  # Handle events
            if event.type == pygame.QUIT:  # If the close button is pressed, quit the game
                game_over = True
            if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_LEFT:  # If the left arrow key is pressed
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # If the right arrow key is pressed
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # If the up arrow key is pressed
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # If the down arrow key is pressed
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries of the display
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change  # Update the x-coordinate of the snake
        y1 += y1_change  # Update the y-coordinate of the snake
        dis.fill(blue)  # Fill the display with blue color
        # Draw the food on the display
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []  # List to store the coordinates of the snake's head
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)  # Add the snake's head to the snake list

        if len(snake_List) > Length_of_snake:  # Remove the last segment of the snake
            del snake_List[0]

        for x in snake_List[:-1]:  # Check if the snake hits itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # Draw the snake on the display
        your_score(Length_of_snake - 1)  # Display the score
        pygame.display.update()  # Update the display

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1  # Increase the length of the snake

        clock.tick(snake_speed)  # Control the speed of the snake

    pygame.quit()  # Quit pygame
    quit()  # Quit the program

gameLoop()  # Start the game loop
