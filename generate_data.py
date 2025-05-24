import random

def create_sorted_data(size):
    """Generates a sorted dataset."""
    return list(range(size))

def create_reverse_sorted_data(size):
    """Generates a reverse sorted dataset."""
    return list(range(size, 0, -1))

def create_random_data(size):
    """Generates a random dataset."""
    return [random.randint(0, size) for _ in range(size)]