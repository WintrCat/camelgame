import src.game as game

import src.pages.inventory as inventory

from random import randint
from time import sleep

def rand_loc_print(text: str):
    print(" " * randint(1, game.screen_length - len(text)), end="")
    game.print_dialogue(text)
    print("\n" * randint(0, 2), end="")
    game.adjusted_sleep(1.5)

def display():
    game.print_seperator()
    rand_loc_print("What happened?")
    rand_loc_print("Where am I?")
    rand_loc_print("Where is this?")
    rand_loc_print("Where is everyone?")
    rand_loc_print("What's going on?")
    rand_loc_print("wake up.")
    rand_loc_print("...")
    rand_loc_print("WAKE UP")
    game.print_seperator()
    input("> ")
    game.clear()
    display2()

def display2():
    game.print_seperator()
    print(game.art.get("wake"))
    game.print_seperator()
    game.adjusted_sleep(2)
    game.print_dialogue("You wake up in an infinite stretch of desert.")
    game.adjusted_sleep(3)
    game.print_dialogue("There is nothing here.")
    game.adjusted_sleep(3)
    game.print_dialogue("Nothing... but a camel that stands before you.")
    game.adjusted_sleep(3)
    game.print_dialogue("It bears a fine silk carpet,")
    game.adjusted_sleep(3)
    game.print_dialogue("although it is obscured by a mess of luggage.")
    game.print_seperator()
    input("> ")
    game.clear()
    display3()

def display3():
    game.print_seperator()
    print(game.art.get("wake"))
    game.print_seperator()
    game.print_dialogue("What do you want to do?")
    print()
    game.print_dialogue("[1] Attempt to confront the camel")
    game.print_dialogue("[2] Pretend to stay unconscious")
    game.print_dialogue("[3] Stand up and run as far as you can")
    game.print_dialogue("\n[4] Open Inventory")
    game.print_seperator()

def receive(inp: str):
    if inp == "1":
        game.set_page()
    if inp == "4":
        game.set_return_page(display3, receive)
        game.set_page(inventory.display, inventory.receive)