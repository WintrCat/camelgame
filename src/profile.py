username = "Player"
health = 100
hunger = 100
thirst = 100

def get_username() -> str:
    return username
def set_username(new_username: str):
    global username
    username = new_username

def get_health() -> int:
    return health
def set_health(new_health: int):
    global health
    health = new_health

def get_hunger() -> int:
    return hunger
def set_hunger(new_hunger: int):
    global hunger
    hunger = new_hunger

def get_thirst() -> int:
    return thirst
def set_thirst(new_thirst: int):
    global thirst
    thirst = new_thirst

inventory = {}
item_icons = {
    "Water Bottle": "🥤",
    "Knife": "🔪"
}

def get_inventory() -> dict:
    return inventory

def add_item(name: str, count: int):
    for item in inventory.keys():
        if item == name:
            inventory[item] += count
            break
    else:
        inventory[name] = count
    print(f"[INVENTORY] You picked up {count}x {item_icons[name]} {name}.")

def remove_item(name: str, count: int):
    for item in inventory.keys():
        if item == name:
            inventory[item] -= count
            if inventory[item] <= 0:
                inventory.pop(item)
            break
    print(f"[INVENTORY] You trashed {count}x {item_icons[name]} {name}.")

# implement soon
def use_item(name: str):
    pass