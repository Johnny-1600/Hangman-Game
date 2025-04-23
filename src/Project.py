import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 1000, 800
FPS = 30

# Font settings
font = pygame.font.SysFont('arial', 48)
small_font = pygame.font.SysFont('arial', 30)

# Themes
LIGHT_THEME = {
    'bg': (255, 255, 255),
    'text': (0, 0, 0),
    'hangman': (0, 0, 0),
    'win': (0, 255, 0),
    'lose': (255, 0, 0)
}

DARK_THEME = {
    'bg': (30, 30, 30),
    'text': (255, 255, 255),
    'hangman': (255, 255, 255),
    'win': (0, 255, 150),
    'lose': (255, 100, 100)
}

# Word list
def get_word():
    words = [
        'python', 'hangman', 'computer', 'programming', 'developer', 'algorithm',
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

# Function to draw hangman
def draw_hangman(screen, tries, color):
    pygame.draw.line(screen, color, (100, 500), (200, 500), 5)
    pygame.draw.line(screen, color, (150, 500), (150, 200), 5)
    pygame.draw.line(screen, color, (150, 200), (250, 200), 5)
    pygame.draw.line(screen, color, (250, 200), (250, 250), 5)

    if tries <= 5:
        pygame.draw.circle(screen, color, (250, 270), 20, 5)
    if tries <= 4:
        pygame.draw.line(screen, color, (250, 290), (250, 350), 5)
    if tries <= 3:
        pygame.draw.line(screen, color, (250, 305), (220, 330), 5)
    if tries <= 2:
        pygame.draw.line(screen, color, (250, 305), (280, 330), 5)
    if tries <= 1:
        pygame.draw.line(screen, color, (250, 350), (220, 395), 5)
    if tries == 0:
        pygame.draw.line(screen, color, (250, 350), (280, 395), 5)

# Main game function
def hangman():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hangman Game')

    word = get_word()
    guessed_letters = []
    tries = 6
    word_display = ['_'] * len(word)

    # Theme state
    current_theme = LIGHT_THEME
    button_width, button_height = 200, 90
    button_x = WIDTH - button_width - 20
    button_y = 20
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    button_color = (80, 80, 80)

    running = True
    while running:
        screen.fill(current_theme['bg'])

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME

        # Draw hangman
        draw_hangman(screen, tries, current_theme['hangman'])

        # Draw word
        word_text = ' '.join(word_display)
        word_surface = font.render(word_text, True, current_theme['text'])
        screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, 400))

        # Guessed letters
        guessed_text = 'Guessed Letters: ' + ', '.join(guessed_letters)
        guessed_surface = small_font.render(guessed_text, True, current_theme['text'])
        screen.blit(guessed_surface, (50, 50))

        # Tries
        tries_text = f'Remaining Tries: {tries}'
        tries_surface = small_font.render(tries_text, True, current_theme['lose'])
        screen.blit(tries_surface, (WIDTH // 2 - tries_surface.get_width() // 2, 500))

        # Win/Lose messages
        if '_' not in word_display:
            win_text = "Congratulations! You Won!"
            win_surface = font.render(win_text, True, current_theme['win'])
            screen.blit(win_surface, (WIDTH // 2 - win_surface.get_width() // 2, 550))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        if tries == 0:
            lose_text = f"Game Over! The word was '{word}'."
            lose_surface = font.render(lose_text, True, current_theme['lose'])
            screen.blit(lose_surface, (WIDTH // 2 - lose_surface.get_width() // 2, 550))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False

        # Draw toggle theme button
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        button_text = small_font.render('Toggle Theme', True, (255, 255, 255))
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

# Run game
if __name__ == '__main__':
    hangman()