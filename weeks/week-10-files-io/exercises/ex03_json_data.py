"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

def save_json(path: Path, data: dict[str, object]) -> Path:
    """Tạo thư mục cha và lưu dữ liệu JSON với ensure_ascii=False và indent=2."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def load_json(path: Path) -> dict[str, object]:
    """Đọc dữ liệu từ file JSON và kiểm tra kiểu dict."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object")
    return data


WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay: dict[str, object] = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}


def main() -> None:
    """Thực thi các bước ghi và đọc file JSON replay."""
    # TODO: tạo thư mục cha trước khi ghi file.
    path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: lưu replay với ensure_ascii=False và indent=2.
    save_json(path, replay)

    # TODO: tải lại và kiểm tra cả hai nhãn trước khi đọc turns.
    loaded = load_json(path)
    is_valid_format = (
        loaded.get("format") == "COURSE LOCAL FORMAT"
        and loaded.get("production_compatibility") == "NOT VUACOC PRODUCTION FORMAT"
    )

    if is_valid_format:
        turns = loaded.get("turns", [])
        print(f"Replay hợp lệ. Định dạng: {loaded['format']}; Số turns: {len(turns)}")
    else:
        print("Cảnh báo: Replay không hợp lệ theo định dạng course-local.")


if __name__ == "__main__":
    main()
