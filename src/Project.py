import pygame
import random

# Game Layout
def initialize_game():
    pygame.init()

    # Game Settings
    WIDTH, HEIGHT = 1000, 800
    FPS = 30
    BORDER_WIDTH = 10

    # Font Settings
    font = pygame.font.SysFont('arial', 48)
    small_font = pygame.font.SysFont('arial', 30)

    # Themes
    LIGHT_THEME = {
        'bg': (255, 255, 255),
        'text': (0, 0, 0),
        'win': (0, 255, 0),
        'lose': (255, 0, 0)
    }

    DARK_THEME = {
        'bg': (30, 30, 30),
        'text': (255, 255, 255),
        'win': (0, 255, 150),
        'lose': (255, 100, 100)
    }

    # Color Themes
    COLOR_THEMES = [
        {'name': 'Default', 'light': {'hangman': (0, 0, 0), 'text': (0, 0, 0)}, 'dark': {'hangman': (255, 255, 255), 'text': (255, 255, 255)}},
        {'name': 'Blue', 'light': {'hangman': (0, 120, 255), 'text': (0, 120, 255)}, 'dark': {'hangman': (0, 120, 255), 'text': (0, 120, 255)}},
        {'name': 'Red', 'light': {'hangman': (200, 30, 30), 'text': (200, 30, 30)}, 'dark': {'hangman': (200, 30, 30), 'text': (200, 30, 30)}},
        {'name': 'Green', 'light': {'hangman': (30, 200, 100), 'text': (30, 200, 100)}, 'dark': {'hangman': (30, 200, 100), 'text': (30, 200, 100)}},
        {'name': 'Yellow', 'light': {'hangman': (255, 215, 0), 'text': (255, 215, 0)}, 'dark': {'hangman': (255, 215, 0), 'text': (255, 215, 0)}}
    ]

    return WIDTH, HEIGHT, FPS, BORDER_WIDTH, font, small_font, LIGHT_THEME, DARK_THEME, COLOR_THEMES

# Word List
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
    pygame.draw.rect(screen, color, pygame.Rect(120, 480, 160, 15))
    pygame.draw.rect(screen, color, pygame.Rect(140, 460, 40, 20))
    pygame.draw.rect(screen, color, pygame.Rect(180, 460, 40, 20))
    pygame.draw.line(screen, color, (150, 460), (150, 200), 8)
    pygame.draw.line(screen, color, (150, 200), (250, 200), 8)
    pygame.draw.circle(screen, color, (250, 200), 8)

    if tries <= 5:
        pygame.draw.line(screen, color, (250, 210), (250, 250), 5)
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
def hangman(current_theme, color_theme_index):
    # Set Screen
    WIDTH, HEIGHT, FPS, BORDER_WIDTH, font, small_font, LIGHT_THEME, DARK_THEME, COLOR_THEMES = initialize_game()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hangman Game')

    # Get a random word
    word = get_word()
    guessed_letters = []
    tries = 6
    word_display = ['_'] * len(word)
    hint_used = False

    # Theme and Color state
    hangman_color = COLOR_THEMES[color_theme_index]['light']['hangman'] if current_theme == LIGHT_THEME else COLOR_THEMES[color_theme_index]['dark']['hangman']
    text_color = COLOR_THEMES[color_theme_index]['light']['text'] if current_theme == LIGHT_THEME else COLOR_THEMES[color_theme_index]['dark']['text']

    # Button Settings
    button_width, button_height = 200, 90
    button_color = (80, 80, 80)

    # Theme toggle button
    theme_button_rect = pygame.Rect(WIDTH - button_width - 20, 20, button_width, button_height)

    # Color theme button and hint button
    color_button_rect = pygame.Rect(WIDTH - button_width - 20, 130, button_width, button_height)
    hint_button_rect = pygame.Rect(WIDTH // 2 + 200, 500, 100, 50)

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(current_theme['bg'])

        # Draw a border
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT), BORDER_WIDTH)

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
                if theme_button_rect.collidepoint(event.pos):
                    # Toggle between light and dark theme
                    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME
                    hangman_color = COLOR_THEMES[color_theme_index]['dark']['hangman'] if current_theme == DARK_THEME else COLOR_THEMES[color_theme_index]['light']['hangman']
                    text_color = COLOR_THEMES[color_theme_index]['dark']['text'] if current_theme == DARK_THEME else COLOR_THEMES[color_theme_index]['light']['text']

                if color_button_rect.collidepoint(event.pos):
                    color_theme_index = (color_theme_index + 1) % len(COLOR_THEMES)
                    hangman_color = COLOR_THEMES[color_theme_index]['dark']['hangman'] if current_theme == DARK_THEME else COLOR_THEMES[color_theme_index]['light']['hangman']
                    text_color = COLOR_THEMES[color_theme_index]['dark']['text'] if current_theme == DARK_THEME else COLOR_THEMES[color_theme_index]['light']['text']

                if hint_button_rect.collidepoint(event.pos) and not hint_used and '_' in word_display:
                    unrevealed = [i for i, l in enumerate(word) if word_display[i] == '_']
                    if unrevealed:
                        index = random.choice(unrevealed)
                        letter = word[index]
                        for i in range(len(word)):
                            if word[i] == letter:
                                word_display[i] = letter
                        guessed_letters.append(letter)
                        hint_used = True

        # Draw hangman
        draw_hangman(screen, tries, hangman_color)

        # Draw word
        word_text = ' '.join(word_display)
        word_surface = font.render(word_text, True, text_color)
        screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, 400))

        # Guessed letters
        guessed_text = 'Guessed Letters: ' + ', '.join(guessed_letters)
        guessed_surface = small_font.render(guessed_text, True, text_color)
        screen.blit(guessed_surface, (50, 50))

        # Tries
        tries_text = f'Remaining Tries: {tries}'
        tries_surface = small_font.render(tries_text, True, text_color)
        screen.blit(tries_surface, (WIDTH // 2 - tries_surface.get_width() // 2, 500))

        # Hint button
        pygame.draw.rect(screen, (100, 160, 100), hint_button_rect, border_radius=8)
        hint_label = "Hint" if not hint_used else "Used"
        hint_text = small_font.render(hint_label, True, (255, 255, 255))
        screen.blit(hint_text, hint_text.get_rect(center=hint_button_rect.center))

        # Win/Lose messages
        if '_' not in word_display or tries == 0:
            result_text = "Congratulations! You Won!" if '_' not in word_display else f"Game Over! The word was '{word}'."
            result_surface = font.render(result_text, True, text_color)
            screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, 550))

            # Draw buttons
            play_again_rect = pygame.Rect(WIDTH // 2 - 180, 620, 180, 60)
            quit_rect = pygame.Rect(WIDTH // 2 + 20, 620, 180, 60)

            pygame.draw.rect(screen, (70, 130, 180), play_again_rect, border_radius=10)
            pygame.draw.rect(screen, (180, 70, 70), quit_rect, border_radius=10)

            play_again_text = small_font.render("Play Again", True, (255, 255, 255))
            quit_text = small_font.render("Quit", True, (255, 255, 255))
            screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))
            screen.blit(quit_text, quit_text.get_rect(center=quit_rect.center))

            pygame.display.update()

            # Wait for click or timeout
            wait_time = 10000  # 10 seconds
            timer_start = pygame.time.get_ticks()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_again_rect.collidepoint(event.pos):
                            hangman(current_theme, color_theme_index)  # Restart the game with current settings
                            return
                        if quit_rect.collidepoint(event.pos):
                            pygame.quit()
                            return

                # Auto-quit after couple of seconds if no input
                if pygame.time.get_ticks() - timer_start > wait_time:
                    pygame.quit()
                    return

        # Draw theme toggle button
        pygame.draw.rect(screen, button_color, theme_button_rect, border_radius=10)
        theme_text = small_font.render('Toggle Theme', True, (255, 255, 255))
        screen.blit(theme_text, theme_text.get_rect(center=theme_button_rect.center))

        # Draw color theme button
        pygame.draw.rect(screen, button_color, color_button_rect, border_radius=10)
        color_label = f"Color: {COLOR_THEMES[color_theme_index]['name']}"
        color_text_render = small_font.render(color_label, True, (255, 255, 255))
        screen.blit(color_text_render, color_text_render.get_rect(center=color_button_rect.center))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

# Run game
if __name__ == '__main__':
    WIDTH, HEIGHT, FPS, BORDER_WIDTH, font, small_font, LIGHT_THEME, DARK_THEME, COLOR_THEMES = initialize_game()
    hangman(LIGHT_THEME, 0)
