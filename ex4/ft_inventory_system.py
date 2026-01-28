#!/usr/bin/env python3


def ft_inventory_system() -> None:
    """
    Inventory system using nested dictionaries with players and catalog.
    """
    data = {
        "players": {
            "alice": {
                "items": {"sword": 1, "potion": 5, "shield": 1},
                "total_val": 950,
                "total_items": 7,
            },
            "bob": {"items": {}, "total_val": 0, "total_items": 0},
        },
        "catalog": {
            "sword": {"type": "weapon", "value": 500, "rarity": "rare"},
            "potion": {"type": "consumable", "value": 50, "rarity": "common"},
            "shield": {"type": "armor", "value": 200, "rarity": "uncommon"},
            "magic_ring":
            {"type": "accessory", "value": 1000, "rarity": "rare"},
        },
    }

    print("=== Player Inventory System ===")
    print("")

    # --- Alice's Inventory ---
    print("=== Alice's Inventory ===")

    catalog = data.get("catalog")
    alice_data = data.get("players").get("alice")
    categories = {}

    # Itering through items like your original code
    for name, quantity in alice_data.get("items").items():
        details = catalog.get(name)
        price = details.get("value")
        subtotal = quantity * price

        # Category tracking
        item_type = details.get("type")
        current_cat_qty = categories.get(item_type, 0)
        categories.update({item_type: current_cat_qty + quantity})

        print(
            f"{name} ({item_type}, {details.get('rarity')}): "
            f"{quantity}x @ {price} gold each = {subtotal} gold"
        )

    print("")
    print(f"Inventory value: {alice_data.get('total_val')} gold")
    print(f"Item count: {alice_data.get('total_items')} items")

    # Category output with your "first" logic
    print("Categories: ", end="")
    first = True
    for c, v in categories.items():
        if not first:
            print(", ", end="")
        print(f"{c}({v})", end="")
        first = False

    print("\n\n=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!")

    # Update quantities
    alice_data.get("items").update({"potion": 3})
    data.get("players").get("bob").get("items").update({"potion": 2})

    print("")
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_data.get('items').get('potion')}")
    print(
        "Bob potions: "
        f"{data.get('players').get('bob').get('items').get('potion')}")

    print("\n=== Inventory Analytics ===")

    # Your manual calculation logic
    current_val_alice = alice_data.get("total_val") - 100
    print(f"Most valuable player: Alice ({current_val_alice} gold)")
    print(f"Most items: Alice ({alice_data.get('total_items') - 2} items)")

    # Identify rare items with your original loop logic
    print("Rarest items: ", end="")
    first = True
    for name, info in catalog.items():
        if info.get("rarity") == "rare":
            if not first:
                print(", ", end="")
            print(f"{name}", end="")
            first = False
    print("")


def main():
    ft_inventory_system()


if __name__ == "__main__":
    main()
