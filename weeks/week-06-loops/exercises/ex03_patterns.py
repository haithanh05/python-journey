"""Exercise 03: readable list comprehensions."""

def squares(numbers: list[int]) -> list[int]:
    """Tính bình phương cho danh sách số."""
    return [number**2 for number in numbers]


def even_numbers(numbers: list[int]) -> list[int]:
    """Lọc các số chẵn trong danh sách."""
    return [number for number in numbers if number % 2 == 0]


def main() -> None:
    numbers = range(1, 11)

    # TODO: build squares for all numbers.
    squares_result: list[int] = [n**2 for n in numbers]

    # TODO: build even_numbers with one filter.
    even_result: list[int] = [n for n in numbers if n % 2 == 0]

    # TODO: rewrite one comprehension as a normal loop and compare readability.
    even_loop: list[int] = []
    for n in numbers:
        if n % 2 == 0:
            even_loop.append(n)

    print(squares_result, even_result)


if __name__ == "__main__":
    main()
