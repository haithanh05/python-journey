"""Exercise 01: list create, read, update and delete."""

def add_subject(subjects: list[str], subject: str) -> list[str]:
    """Thêm một môn học vào danh sách (trả về bản copy)."""
    updated = subjects.copy()
    updated.append(subject)
    return updated


def remove_subject(subjects: list[str], subject: str) -> list[str]:
    """Xóa một môn học khỏi danh sách nếu có (trả về bản copy)."""
    updated = subjects.copy()
    if subject in updated:
        updated.remove(subject)
    return updated


subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects.append("Lý")
subjects.insert(1, "Hóa")

# TODO: update the first subject.
subjects[0] = "Toán nâng cao"

# TODO: remove one known subject and pop the last subject.
if "Văn" in subjects:
    subjects.remove("Văn")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
if __name__ == "__main__":
    print(f"First: {subjects[0]}")
    print(f"Last: {subjects[-1]}")
    print(f"Middle slice: {subjects[1:-1]}")
    print(subjects)
