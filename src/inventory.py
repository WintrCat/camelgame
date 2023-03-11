inventory = {}

def get() -> dict:
    return inventory

def add_item(name: str, count: int):
    for item in inventory.keys():
        if item == name:
            inventory[item] += count
            return
    inventory[item] = count

def remove_item(name: str, count: int):
    for item in inventory.keys():
        if item == name:
            inventory[item] -= count
            if inventory[item] <= 0:
                inventory.pop(item)
            return