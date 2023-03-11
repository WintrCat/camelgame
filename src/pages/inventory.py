import src.game as game

import src.inventory as Inventory

@game.wrap_seperators
def display():
    game.print_centered("INVENTORY")
    game.print_seperator()

    inv = Inventory.get()
    for item, count, i in zip(inv.keys(), inv.values(), range(length := len(inv))):
        print(f"[{i}] {count}x {item}")
    if length == 0: print("It's kind of empty in here...")

    game.print_seperator()
    if length > 0:
        print("[1] Use an item")
        print("[2] Trash an item\n")
    print("[3] Close")

def receive(inp: str):
    if inp == "3":
        return_page = game.get_return_page()
        game.set_page(return_page.get("display"), return_page.get("receiver"))