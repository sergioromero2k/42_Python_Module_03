#!/usr/bin/env python3
import time

"""
Demonstrates the power of Python
generators for memory-efficient data processing.
"""


def events(count: int):
    # Generator that yields game events one by one to save memory
    players = ["alice", "bob", "charlie"]
    event_types = ["killed monster", "found treasure", "leveled up"]
    zones = ["pixel_zone_2", "pixel_zone_4", "pixel_zone_5"]
    for i in range(1, count+1):
        yield {
                    "id": i,
                    "player": players[i % len(players)],
                    "event_type": event_types[i % len(event_types)],
                    "timestamp": "2024-01-01T12:00",
                    "data": {
                        "level": (i * 7) % 50 + 1,       # Dynamic levels
                        "score_delta": (i * 100) % 500,  # Calculated score
                        "zone": zones[i % len(zones)]    # Cycled zones
                    }
                }


def fibonacci(count: int):
    # Generator for the Fibonacci sequence
    a, b = 0, 1
    for _ in range(1, count+1):
        yield a
        a, b = b, a+b


def is_prime(num: int):
    # Helper to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_number(count: int):
    # Generator that yields the first N prime numbers
    found = 0
    num = 2
    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print("")
    print("Processing 1000 game events...")
    print("")

    # Matrix tracked in real-time without storing events
    total_events = 0
    high_level_players = 0
    treasure_events = 0
    levelup_events = 0

    stream = events(1000)
    start_time = time.time()

    for event in stream:
        total_events += 1
        if (event['data'])['level'] >= 10:
            high_level_players += 1
        if "treasure" in event['event_type']:
            treasure_events += 1
        if "leveled" in event['event_type']:
            levelup_events += 1

        # Display only the first 3 events for brevity
        if event['id'] <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {(event['data'])['level']}) {event['event_type']}"
                )
        elif event['id'] == 4:
            print("...")

    end_time = time.time()

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("")

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("")
    print("=== Generator Demonstration ===")
    fibo_gen = fibonacci(10)
    print("Fibonacci sequence (first 10): ", end="")
    first = True
    # Fibonacci Demo
    for num in fibo_gen:
        if first:
            print(num, end="")
            first = False
        else:
            print(f", {num}", end="")

    print("")
    # Prime NUmbers Demo
    prime_gen = prime_number(5)
    print("Prime numbers (first 5): ", end="")
    first = True
    for num in prime_gen:
        if first:
            print(num, end="")
            first = False
        else:
            print(f", {num}", end="")
    print("")


if __name__ == "__main__":
    main()
