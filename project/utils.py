def print_header(title):
    """Print a styled section header."""
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print(f"{'=' * 55}")


def print_separator():
    print("-" * 55)


def get_input(prompt, validator=None, error_msg="Invalid input. Please try again."):
    """
    Prompt user for input with optional validation.
    validator: a callable that returns True/False
    """
    while True:
        value = input(f"  {prompt}").strip()
        if validator is None or validator(value):
            return value
        print(f"  [ERROR] {error_msg}")


def get_int_input(prompt, min_val=None, max_val=None):
    """Prompt for an integer with optional range check."""
    while True:
        try:
            value = int(input(f"  {prompt}").strip())
            if min_val is not None and value < min_val:
                print(f"  [ERROR] Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  [ERROR] Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("  [ERROR] Please enter a valid integer.")


def get_float_input(prompt, min_val=0.1):
    """Prompt for a float."""
    while True:
        try:
            value = float(input(f"  {prompt}").strip())
            if value < min_val:
                print(f"  [ERROR] Value must be greater than {min_val}.")
                continue
            return value
        except ValueError:
            print("  [ERROR] Please enter a valid number.")


def yes_no_input(prompt):
    """Return True for 'y', False for 'n'."""
    while True:
        val = input(f"  {prompt} (y/n): ").strip().lower()
        if val in ("y", "yes"):
            return True
        if val in ("n", "no"):
            return False
        print("  [ERROR] Enter 'y' or 'n'.")
