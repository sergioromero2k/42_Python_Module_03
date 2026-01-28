#!/usr/bin/env python3
import math


def pythagoras_3d(p1: tuple, p2: tuple) -> float:
    """
    Calculate the Euclidean distance between two points in 3D space.
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def coordinate_system() -> None:
    """
    Demostrate a simple 3D coordinate system.
    """
    print("=== Game Coordinate System ===")
    print("")
    # 1. Creation and initial distance
    pos = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {pos}")
    print(
        f"Distance between {origin} and {pos}: "
        f"{pythagoras_3d(origin, pos):.2f}\n"
    )

    # 2. Parsing valid coordinates
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    x_s, y_s, z_s = coord_str.split(",")
    parsed = (int(x_s), int(y_s), int(z_s))
    print(f"Parsed position: {parsed}")
    print(
        f"Distance between {origin} and {parsed}: "
        f"{pythagoras_3d(origin, parsed):.1f}\n"
    )

    # 3. Parsing invalid coordinates
    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    try:
        # Aquí es donde el error salta y se va directo al except
        parts = invalid_str.split(",")
        _ = (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")

    # 4. Unpacking demostration (using the valid parsed coordinates)
    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
