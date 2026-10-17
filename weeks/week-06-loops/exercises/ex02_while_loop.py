"""Exercise 02: while, break and continue."""

def countdown(start: int) -> list[int]:
    """Đếm ngược từ start về 1."""
    values = []
    remaining = start
    while remaining > 0:
        values.append(remaining)
        remaining -= 1
    return values


def selected_numbers() -> list[int]:
    """Lọc các số từ 1..10: bỏ qua bội số của 3, dừng sau 8."""
    values = []
    for number in range(1, 11):
        if number % 3 == 0:
            continue
        if number > 8:
            break
        values.append(number)
    return values


remaining = 5

# TODO: count down to 1 and update remaining on every pass.
while remaining > 0:
    print(f"Countdown: {remaining}")
    remaining -= 1

# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
for number in range(1, 11):
    if number % 3 == 0:
        continue
    if number > 8:
        break
    print(number, end=" ")
print()

if __name__ == "__main__":
    print(remaining)
