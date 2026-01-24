#!/usr/bin/env python3
import sys

"""
Processes command-line scores and prints basic statistics:
total, average, high, low, and range.
"""


def score_analytics():
    # List to store processed scores
    list_argvs = []
    argc = 0

    # Count command-line arguments
    argc = len(sys.argv)
    try:
        # If no scores are provided, raise an error to show usage
        if argc < 2:
            raise ValueError(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        # Create a fixed-size list based on number of scores
        list_argvs = [0] * (argc - 1)
        i = 1
        while i < argc:
            # Convert each argument to integer
            try:
                score = int(sys.argv[i])
            except ValueError:
                # Error if not a valid number
                raise ValueError(
                    "Error: All scores must be integers. Check your input!"
                    )
            # Validate score is not negative
            if score < 0:
                raise ValueError(f"Error: Negative score detected {score}")
            # Store score in the list
            list_argvs[i - 1] = score
            i += 1
        # Print statistics once all scores are ready
        info_score(list_argvs)
    except ValueError as e:
        # Print error message in required format
        print("=== Player Score Analytics ===")
        print(f"{e}")


def info_score(scores):
    # Calculate metrics from  the score list
    total_players = len(scores)
    total_sum = sum(scores)
    high_score = max(scores)
    low_score = min(scores)

    # Print formatted report
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_sum}")
    print(f"Average score: {total_sum / total_players}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    score_analytics()
