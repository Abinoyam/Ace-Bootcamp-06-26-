def get_non_empty_input(message):

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_integer_input(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid integer.")


def get_float_input(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Please enter a valid number.")


def get_yes_no_input(message):

    while True:

        value = input(message).strip().lower()

        if value in ("y", "yes"):
            return True

        elif value in ("n", "no"):
            return False

        print("Please enter Y or N.")


def print_divider():

    print("=" * 55)