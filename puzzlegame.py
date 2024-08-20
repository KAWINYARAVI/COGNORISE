import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 300, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3x3 Puzzle Game")

# Load and resize image
image = pygame.image.load('your_image_path.jpg')
image = pygame.transform.scale(image, (screen_width, screen_height))

# Define the grid
rows, cols = 3, 3
piece_width = screen_width // cols
piece_height = screen_height // rows

# Create a list of pieces
pieces = []
for row in range(rows):
    for col in range(cols):
        piece = image.subsurface(col * piece_width, row * piece_height, piece_width, piece_height)
        pieces.append(piece)

# Shuffle the pieces
random.shuffle(pieces)

# Define empty piece (last piece in the list)
empty_piece_index = pieces.index(pieces[-1])

def swap_pieces(index1, index2):
    """Swap two pieces in the list."""
    pieces[index1], pieces[index2] = pieces[index2], pieces[index1]

def draw_grid():
    """Draw the current state of the grid."""
    for i, piece in enumerate(pieces):
        row = i // cols
        col = i % cols
        screen.blit(piece, (col * piece_width, row * piece_height))
    pygame.display.flip()

def is_adjacent(index1, index2):
    """Check if two pieces are adjacent in the grid."""
    if index1 == index2:
        return False
    row1, col1 = index1 // cols, index1 % cols
    row2, col2 = index2 // cols, index2 % cols
    return abs(row1 - row2) + abs(col1 - col2) == 1

def check_win():
    """Check if the pieces are in the correct order."""
    for i, piece in enumerate(pieces[:-1]):
        correct_piece = image.subsurface((i % cols) * piece_width, (i // cols) * piece_height, piece_width, piece_height)
        if piece != correct_piece:
            return False
    return True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            clicked_index = (y // piece_height) * cols + (x // piece_width)

            if is_adjacent(clicked_index, empty_piece_index):
                swap_pieces(clicked_index, empty_piece_index)
                empty_piece_index = clicked_index

                if check_win():
                    print("You Win!")
                    running = False

    draw_grid()

pygame.quit()
