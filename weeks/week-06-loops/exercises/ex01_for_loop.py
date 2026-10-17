"""Exercise 01: for, range, enumerate and zip."""

def numbered_pairs(topics: list[str], scores: list[int]) -> list[str]:
    """Ghép cặp topic và score có đánh số thứ tự từ 1."""
    lines = []
    pairs = zip(topics, scores, strict=True)
    for position, (topic, score) in enumerate(pairs, start=1):
        lines.append(f"{position}. {topic}: {score}")
    return lines


def multiplication_table(number: int) -> list[str]:
    """Tạo bảng nhân từ 1 đến 10."""
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, 11)]


topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
for num in range(1, 6):
    print(num, end=" ")
print()

# TODO: print each topic with a one-based position using enumerate.
for idx, topic in enumerate(topics, start=1):
    print(f"{idx}. {topic}")

# TODO: pair topics and scores with zip(..., strict=True).
for topic, score in zip(topics, scores, strict=True):
    print(f"{topic}: {score}")

if __name__ == "__main__":
    print(topics, scores)
