"""Exercise 02: slicing, mutability, alias and copy."""

def slices(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Tạo lát cắt 3 phần tử đầu và 3 phần tử cuối."""
    return numbers[:3], numbers[-3:]


def alias_and_copy(numbers: list[int]) -> tuple[list[int], list[int], list[int]]:
    """Minh họa alias và shallow copy."""
    original = numbers.copy()
    alias = original
    copied = original.copy()
    alias.append(3)
    return original, alias, copied


numbers = [1, 2, 3, 4, 5, 6]

# TODO: create first_three and last_three using slices.
first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

# TODO: make alias refer to numbers and copied be a shallow copy.
alias: list[int] = numbers
copied: list[int] = numbers.copy()

# TODO: append through alias and explain which lists change.
alias.append(7)
# Khi append qua alias, cả 'numbers' và 'alias' đều thay đổi vì cùng trỏ tới 1 list; 'copied' không đổi.

if __name__ == "__main__":
    print(first_three, last_three, alias, copied)
