# input_helpers.py

def get_non_empty_string(prompt):
    """Demande un texte non vide."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Try again.")


def get_positive_int(prompt):
    """Demande un entier positif."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_float(prompt):
    """Demande un nombre décimal positif."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")