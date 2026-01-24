import math


def pythagoras_3d(origin: tuple, tupla: tuple) -> float:
    x1, y1, z1 = origin
    x2, y2, z2 = tupla
    distance = float(
        math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2))
    return distance


def coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print("")
    tupla = (10, 20, 5)
    origin = (0, 0, 0)
    pythagoras_3d_tupla = pythagoras_3d(origin, tupla)
    print(f"Position created: {tupla}")
    print(f"Distance between {origin} and {tupla}: {pythagoras_3d_tupla:.2f}")
    print("")

    parsing_coords("3,4,0", origin)
    parsing_coords("abc,def,ghi", origin)


def parsing_coords(coord: str, origin: tuple) -> None:
    try:
        print(f"Parsing coordinates: \"{coord}\"")
        x_str, y_str, z_str = coord.split(",")
        x = int(x_str)
        y = int(y_str)
        z = int(z_str)
        parsed = (x, y, z)
        pythagoras_3d_par = pythagoras_3d(origin, parsed)
        print(f"Parsed position: {parsed}")
        print(
            f"Distance between {origin} and {parsed}: {pythagoras_3d_par:.1f}")
        print("")

        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

        print("")
    except ValueError as e:
        print(f"Parsing invalid coordinates: {coord}")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")


def main():
    coordinate_system()


if __name__ == "__main__":
    main()
