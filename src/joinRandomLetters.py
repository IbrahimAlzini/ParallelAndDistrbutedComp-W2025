import random
import string
# Function to join a thousand random letters
def join_random_letters(start = 0, end = 1000):
    letters = [random.choice(string.ascii_letters) for _ in range(start, end)]
    joined_letters = ''.join(letters)
    return joined_letters
