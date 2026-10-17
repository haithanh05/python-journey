"""Exercise 01: pathlib and UTF-8 text."""

from pathlib import Path

def save_text(path: Path, lines: list[str]) -> Path:
    """Tạo thư mục cha và ghi các dòng text với encoding utf-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def load_lines(path: Path) -> list[str]:
    """Đọc file text UTF-8 và trả về danh sách các dòng."""
    return path.read_text(encoding="utf-8").splitlines()


WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "week10.txt"


def main() -> None:
    """Thực thi các bước ghi và đọc file text."""
    # TODO: tạo thư mục cha.
    path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: ghi hai dòng với encoding="utf-8".
    sample_lines = ["Dòng 1: Python Journey", "Dòng 2: Data persistence với pathlib"]
    save_text(path, sample_lines)

    # TODO: đọc text và in từng dòng với số thứ tự bắt đầu từ 1.
    lines = load_lines(path)
    for index, line in enumerate(lines, start=1):
        print(f"{index}: {line}")

    print(f"File path: {path}")


if __name__ == "__main__":
    main()
