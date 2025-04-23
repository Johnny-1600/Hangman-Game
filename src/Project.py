import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 1000, 800
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font settings
font = pygame.font.SysFont('arial', 48)
small_font = pygame.font.SysFont('arial', 30)

# Function to get a random word
def get_word():
    words = ['python', 'hangman', 'computer', 'programming', 'developer', 'algorithm',
        'function', 'variable', 'internet', 'keyboard', 'monitor', 'software',
        'hardware', 'debugging', 'database', 'network', 'compiler', 'syntax',
        'penguin', 'elephant', 'giraffe', 'kangaroo', 'dolphin', 'tiger',
        'octopus', 'crocodile', 'rhinoceros', 'flamingo', 'cheetah', 'armadillo',
        'koala', 'hedgehog', 'squirrel', 'ostrich', 'panther',
        'mountain', 'river', 'ocean', 'forest', 'volcano', 'desert',
        'island', 'glacier', 'savanna', 'canyon', 'valley', 'rainforest',
        'tundra', 'meadow', 'waterfall', 'trees', 'water', 'smoke', 'air',
        'umbrella', 'backpack', 'notebook', 'puzzle', 'guitar', 'airplane',
        'rocket','helmet', 'sandwich', 'lantern', 'ladder', 'pillow',
        'microwave', 'bicycle', 'camera', 'car', 'game', 'keyboard', 'suitcase', 'wallet',
        'pirate', 'ninja', 'zombie', 'wizard', 'galaxy',
        'nebula', 'asteroid', 'spaceship', 'universe', 'planet', 'timewarp', 'blackhole',
        'portal', 'dragon', 'castle', 'magic', 'superhero', 'pumpkin'
    ]
    return random.choice(words)

# Function to draw the hangman figure
def draw_hangman(screen, tries):
    # Drawing the base
    pygame.draw.line(screen, BLACK, (100, 500), (200, 500), 5)  # Base line
    pygame.draw.line(screen, BLACK, (150, 500), (150, 200), 5)  # Vertical line (post)
    pygame.draw.line(screen, BLACK, (150, 200), (250, 200), 5)  # Horizontal line (top bar)
    pygame.draw.line(screen, BLACK, (250, 200), (250, 250), 5)  # Noose

    # Drawing the hangman based on the number of tries left
    if tries <= 5:
        pygame.draw.circle(screen, BLACK, (250, 270), 20, 5)  # Head
    if tries <= 4:
        pygame.draw.line(screen, BLACK, (250, 290), (250, 350), 5)  # Body
    if tries <= 3:
        pygame.draw.line(screen, BLACK, (250, 305), (220, 330), 5)  # Left arm
    if tries <= 2:
        pygame.draw.line(screen, BLACK, (250, 305), (280, 330), 5)  # Right arm
    if tries <= 1:
        pygame.draw.line(screen, BLACK, (250, 350), (220, 395), 5)  # Left leg
    if tries == 0:
        pygame.draw.line(screen, BLACK, (250, 350), (280, 395), 5)  # Right leg

# Main game loop
def hangman():
    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hangman Game')

    # Get a random word
    word = get_word()
    guessed_letters = []
    tries = 6
    word_display = ['_'] * len(word)

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                guess = pygame.key.name(event.key).lower()
                if len(guess) == 1 and guess.isalpha():
                    if guess not in guessed_letters:
                        guessed_letters.append(guess)
                        if guess in word:
                            for i in range(len(word)):
                                if word[i] == guess:
                                    word_display[i] = guess
                        else:
                            tries -= 1

        # Draw the hangman figure
        draw_hangman(screen, tries)

        # Draw the word display
        word_text = ' '.join(word_display)
        word_surface = font.render(word_text, True, BLACK)
        screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, 400))

        # Draw guessed letters
        guessed_text = 'Guessed Letters: ' + ', '.join(guessed_letters)
        guessed_surface = small_font.render(guessed_text, True, BLACK)
        screen.blit(guessed_surface, (50, 50))

        # Display remaining tries
        tries_text = f'Remaining Tries: {tries}'
        tries_surface = small_font.render(tries_text, True, RED)
        screen.blit(tries_surface, (WIDTH // 2 - tries_surface.get_width() // 2, 500))

        # Check if the player has won or lost
        if '_' not in word_display:
            win_text = "Congratulations! You Won!"
            win_surface = font.render(win_text, True, GREEN)
            screen.blit(win_surface, (WIDTH // 2 - win_surface.get_width() // 2, 550))
            pygame.display.update()
            pygame.time.wait(2000)  # Wait for 2 seconds before quitting
            running = False

        if tries == 0:
            lose_text = f"Game Over! The word was, '{word}'."
            lose_surface = font.render(lose_text, True, RED)
            screen.blit(lose_surface, (WIDTH // 2 - lose_surface.get_width() // 2, 550))
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 2 seconds before quitting
            running = False

        # Update the display
        pygame.display.update()

        # Set the frame rate
        pygame.time.Clock().tick(FPS)

    pygame.quit()

# Run the game
if __name__ == '__main__':
    hangman()