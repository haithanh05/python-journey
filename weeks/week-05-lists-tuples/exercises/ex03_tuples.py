"""Exercise 03: tuple, packing and unpacking."""

def unpack_point(point: tuple[int, int]) -> str:
    """Unpack tọa độ điểm thành chuỗi 'x=..., y=...'."""
    x, y = point
    return f"x={x}, y={y}"


def unpack_profile(profile: tuple[str, int, str]) -> str:
    """Unpack thông tin profile thành chuỗi định dạng."""
    name, age, topic = profile
    return f"{name} · {age} · {topic}"


def swap(left: str, right: str) -> tuple[str, str]:
    """Hoán đổi hai giá trị sử dụng unpacking."""
    left, right = right, left
    return left, right


coordinate = (3, 7)

# TODO: unpack coordinate into x and y.
x, y = coordinate

# TODO: pack name, age and topic into one profile tuple, then unpack it.
profile: tuple[str, int, str] = ("An", 20, "Python")
p_name, p_age, p_topic = profile

# TODO: swap left and right using unpacking.
left = "A"
right = "B"
left, right = right, left

if __name__ == "__main__":
    print(x, y, profile, left, right)
