import src.game as game

import src.profile as Profile

item_count = 0

@game.wrap_seperators
def display():
    global item_count

    game.print_centered("STATS - " + Profile.get_username())
    game.print_seperator()

    health = Profile.get_health()
    print("HEALTH: ", end="")
    print("❤️" * (health // 10), end="")
    if health % 10 > 0:
        print("💔", end="")
    if health <= 90:
        print("🖤" * ((100 - health) // 10), end="")
    print()

    hunger = Profile.get_hunger()
    hunger_status = None
    if hunger <= 10:
        hunger_status = "Critically starving"
    elif hunger <= 20:
        hunger_status = "Starving"
    elif hunger <= 30:
        hunger_status = "Very hungry"
    elif hunger <= 50:
        hunger_status = "Hungry"
    elif hunger <= 70:
        hunger_status = "A bit hungry"
    else:
        hunger_status = "Fine"
    print(f"HUNGER: {hunger_status} ({hunger}%)")

    thirst = Profile.get_thirst()
    thirst_status = None
    if thirst <= 10:
        thirst_status = "Critically dehydrated"
    elif thirst <= 20:
        thirst_status = "Very dehydrated"
    elif thirst <= 50:
        thirst_status = "Dehydrated"
    elif thirst <= 70:
        thirst_status = "A little dehydrated"
    else:
        thirst_status = "Fine"
    print(f"THIRST: {thirst_status} ({thirst}%)")

    game.print_seperator()
    game.print_centered("INVENTORY")
    game.print_seperator()

    inv = Profile.get_inventory()
    for item, count, i in zip(inv.keys(), inv.values(), range(length := len(inv))):
        print(f"[{i}] {count}x {item}")
    item_count = length
    if is_empty := (length == 0): print("It's kind of empty in here...")

    game.print_seperator()
    if not is_empty:
        print("[1] Use an item")
        print("[2] Trash an item\n")
    print(f"[{1 if is_empty else 3}] Close")

def receive(inp: str):
    if inp == ("3" if item_count > 0 else "1"):
        return_page = game.get_return_page()
        game.set_page(return_page.get("display"), return_page.get("receiver"))
    if inp == "1":
        game.print_seperator()
        print("Enter the index of the item you want to use")
        item_index = input("> ")
        try:
            item_index = int(item_index)
            if item_index >= item_count or item_index < 0: raise RuntimeError()
        except:
            print("That is an invalid item index...")
            game.adjusted_sleep(1.5)
            return
        
        inv = Profile.get_inventory().keys()
        print(f"Using a {inv[item_index - 1]}...")
        game.adjusted_sleep(1.5)
    elif inp == "2":
        game.print_seperator()
        print("Enter the index of the item you want to trash")
        item_index = input("> ")
        try:
            item_index = int(item_index)
            if item_index >= item_count or item_index < 0: raise RuntimeError()
        except:
            print("That is an invalid item index...")
            game.adjusted_sleep(1.5)
            return
        
        game.print_seperator()
        print("Enter how many items you want to trash...")
        count = input("> ")
        try:
            count = int(count)
            inv = Profile.get_inventory().keys()
            if count < 0:
                print("You can't enter a negative amount...")
                raise RuntimeError()
            elif count > inv[item_index - 1]:
                print("You don't have enough of that item to trash...")
                raise RuntimeError()
        except:
            game.adjusted_sleep(1.5)
            return
        
        inv = Profile.get_inventory().keys()
        inv[item_index - 1]