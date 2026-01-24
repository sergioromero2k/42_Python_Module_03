#!/usr/bin/env python3

def ft_inventory_system() -> None:
    """
    Inventory system using nested dictionaries.
    """

    # Initialize Alice's nested inventory
    alice_inventory = {
        "sword":
        {
            "type": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion":
        {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield":
        {
            "type": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        }
    }
    # Bob starts with an empty inventory
    bob_inventory = {}

    print("=== Player Inventory System ===")
    print("")
    # --- Alice's Inventory ---
    print("=== Alice's Inventory ===")
    total_val_alice = 0
    total_items_alice = 0
    categories = {}

    # Itering through items using authorized items() method
    for name, details in alice_inventory.items():
        # Calculate subtotals for the report
        quantity = details.get("quantity")
        price = details.get("value")
        subtotal = quantity * price

        # Accumulate total values
        total_val_alice = total_val_alice + subtotal
        total_items_alice = total_items_alice + quantity

        # Cateogry tracking using get() and update()
        item_type = details.get("type")
        current_cat_qty = categories.get(item_type, 0)
        categories.update({item_type: current_cat_qty + quantity})

        print(
                f"{name} ({details.get('type')}, {details.get('rarity')}):"
                f"{quantity}x @ {price} gold each = {subtotal} gold"
            )

    # Manual formatting for categories output
    print("")
    print(f"Inventory value: {total_val_alice}")
    print(f"Item count: {total_items_alice}")

    print("Categories: ", end="")
    first = True
    for c, v in categories.items():
        if first:
            print(f"{c}({v})", end="")
            first = False
        else:
            print(f", {c}({v})", end="")

    print("")
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!")

    alice_inventory.get("potion").update({"quantity": 3})

    # Define potion data for Bob
    bob_potion = {
        "type": "consumable",
        "rarity": "common",
        "quantity": 2,
        "value": 50
    }
    bob_inventory.update({"potion": bob_potion})

    print("")
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory.get('potion').get('quantity')}")
    print(f"Bob potions: {bob_inventory.get('potion').get('quantity')}")
    print("")

# --- Inventory Analytics ---
    print("\n=== Inventory Analytics ===")

    # Calculate Bob's totals manually
    total_val_bob = 0
    total_items_bob = 0
    for item in bob_inventory.values():
        total_val_bob = total_val_bob + \
            (item.get("quantity") * item.get("value"))
        total_items_bob = total_items_bob + item.get("quantity")

    # Recalculate Alice's value after transaction
    # (Initial 950 - 100 from the 2 potions given away)
    current_val_alice = total_val_alice - 100

    # Determine most valuable player
    if current_val_alice > total_val_bob:
        print(f"Most valuable player: Alice ({current_val_alice} gold)")
    else:
        print(f"Most valuable player: Bob ({total_val_bob} gold)")

    # Determine player with most items
    current_items_alice = total_items_alice - 2
    if current_items_alice > total_items_bob:
        print(f"Most items: Alice ({current_items_alice} items)")
    else:
        print(f"Most items: Bob ({total_items_bob} items)")

    # Identify rare items

    print("Rarest items: ", end="")
    first = True
    for c, v in alice_inventory.items():
        rare = v.get('rarity')
        if first:
            if rare == "rare":
                print(f"{rare}", end="")
                first = False
        else:
            if rare == "rare":
                print(f", {rare}", end="")
    print("\n")


def main():
    ft_inventory_system()


if __name__ == "__main__":
    main()
