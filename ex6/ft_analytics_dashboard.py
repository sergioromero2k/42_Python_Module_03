#!/usr/bin/env python3


def main():
    raw_data = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 3,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
        },
        "sessions": [
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }

    players = raw_data["players"]

    print("=== Game Analytics Dashboard ===\n")

    # List Comprehension Examples
    high_score = [
        name for name, value in players.items() if value["total_score"] > 2000
    ]
    score_doubled = [value["total_score"] * 2 for value in players.values()]
    active_player = [
        name for name, value in players.items() if value["sessions_played"] > 7
    ]

    print("High scorers (>2000):", high_score)
    print("Scores doubled:", score_doubled)
    print("Active players:", active_player)
    print("")

    # Dict Comprehension Examples
    player_score = {name: value["total_score"] for name, value in players.items()}

    score_categories = {
        "high": len(
            [name for name, value in players.items() 
            if value["total_score"] > 5000]
        ),
        "medium": len(
            [
                name
                for name, value in players.items()
                if 3000 < value["total_score"] <= 5000
            ]
        ),
        "low": len(
            [name for name, value in players.items() if value["total_score"] <= 3000]
        ),
    }

    achieve_count = {
        name: value["achievements_count"] for name, value in players.items()
    }

    print("Player scores:", player_score)
    print("Score categories:", score_categories)
    print("Achievement counts:", achieve_count)
    print("")

    # Set Comprehension Examples
    # Aquí haces tú tu código


if __name__ == "__main__":
    main()
