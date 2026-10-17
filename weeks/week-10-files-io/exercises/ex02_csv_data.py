"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

def save_rows(path: Path, rows: list[dict[str, object]]) -> Path:
    """Tạo thư mục cha và ghi danh sách dòng vào file CSV với utf-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["bot", "wins"])
        writer.writeheader()
        writer.writerows(rows)
    return path


def load_rows(path: Path) -> list[dict[str, str]]:
    """Đọc dữ liệu từ file CSV bằng csv.DictReader."""
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows: list[dict[str, object]] = [
    {"bot": "student", "wins": 2},
    {"bot": "wait", "wins": 0},
]


def main() -> None:
    """Thực thi các bước ghi và đọc file CSV."""
    # TODO: tạo thư mục cha trước khi mở file.
    path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: ghi header và rows bằng csv.DictWriter.
    save_rows(path, rows)

    # TODO: tải rows bằng csv.DictReader rồi in kết quả.
    loaded_rows = load_rows(path)
    print("Kết quả đọc từ CSV:")
    for row in loaded_rows:
        print(f"  Bot: {row['bot']}, Wins: {row['wins']}")


if __name__ == "__main__":
    main()
