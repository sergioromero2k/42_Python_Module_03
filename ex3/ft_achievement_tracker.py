#!/usr/bin/env python3


def ft_achievement_tracker() -> None:
    """
    This function creates sets of achievements for three players
    (alice, bob, charlie), then performs analysis using set
    operations
    """
    # 1. Raw Data: Dictionary containing player names and lists of achievements
    # Included intentional duplicates to demonstrate set deduplication power
    raw_data = {
        "alice": [
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
            "level_10",
        ],
        "bob": ["first_kill", "level_10", "boss_slayer", "collector",
                "first_kill"],
        "charlie": [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
            "level_10",
        ],
    }

    # 2. Set Conversion: Automatically removes duplicates from raw lists
    alice = set(raw_data["alice"])
    bob = set(raw_data["bob"])
    charlie = set(raw_data["charlie"])

    print("=== Achievement Tracker System ===")
    print("")
    # Print each player's achievements
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("")

    print("=== Achievement Analytics ===")

    # Union: all unique achievements among the three players
    all_unique = alice.union(bob, charlie)
    print(f"All unique achievements: {all_unique}")

    # Length of the resulting set (number of unique achievements)
    print(f"Total unique achievements: {len(all_unique)}")

    print("")
    # Intersection: achievements common to all three players
    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")

    # Rare achievements (only 1 player has them)
    rare = set()
    for ach in all_unique:
        count = 0
        if ach in alice:
            count += 1
        if ach in bob:
            count += 1
        if ach in charlie:
            count += 1
        if count == 1:
            rare.add(ach)
    print(f"Rare achievements (1 player): {rare}")
    print("")

    # Player comparisons
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
