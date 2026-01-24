#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    """
    Print info about command line arguments using sys.argv
    """
    print("=== Command Quest ===")
    # If only the script name is present, no user arguments were given
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        # Number of user arguments (exclude the script name)
        print(f"Arguments received: {len(sys.argv) - 1}")
        # Always show the program name
        print(f"Program name: {sys.argv[0]}")

        # Print each user argument one by one
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    # Total elements in sys.argv includes the program name too
    print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    # Main entry point of the program
    main()
