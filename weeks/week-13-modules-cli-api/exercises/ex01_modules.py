"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Call the reusable decision function from the package."""
    action = choose_action(1, 4)
    print(f"Action: {action}")


if __name__ == "__main__":
    main()
