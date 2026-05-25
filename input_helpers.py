# input_helpers.py  —  Secure input functions
# Dev 4 : DAYAMBA Abigaël Palingwendé


def get_int(message: str, min_val: int = 0, max_val: int = 9999) -> int:
    while True:
        try:
            value = int(input(message))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  ► Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ► That is not a whole number. Try again.")


def get_float(message: str, min_val: float = 0.0) -> float:
    while True:
        try:
            value = float(input(message))
            if value >= min_val:
                return value
            else:
                print(f"  ► The value must be at least {min_val}.")
        except ValueError:
            print("  ► That is not a valid number. Try again.")


def get_yes_no(message: str) -> bool:
    while True:
        answer = input(message).strip().lower()
        if answer in ["yes", "y", "oui", "o"]:
            return True
        elif answer in ["no", "n", "non"]:
            return False
        else:
            print("  ► Please answer yes or no.")


def get_animal_type() -> str:
    valid_types = ["cow", "chicken"]
    while True:
        choice = input("Animal type (cow / chicken) : ").strip().lower()
        if choice in valid_types:
            return choice
        else:
            print(f"  ► Choose from : {valid_types}")


def get_string(message: str, min_len: int = 1) -> str:
    while True:
        value = input(message).strip()
        if len(value) >= min_len:
            return value
        else:
            print("  ► This field cannot be empty.")