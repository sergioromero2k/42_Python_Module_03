#!/usr/bin/env python3


def ft_achievement_tracker() -> None:
    """
    This function creates sets of achievements for three players
    (alice, bob, charlie), then performs analysis using set
    operations
    """
    # Sets containing each player's achievements (no duplicates)
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

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

    # Difference: achievements exclusive to each player
    only_alice = alice.difference(bob, charlie)
    only_bob = bob.difference(alice, charlie)
    only_charlie = charlie.difference(alice, bob)

    # Union of exclusive achievements = rare achievements (only 1 player)
    rare_achievements = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}")
    print("")

    # Player comparisons
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
