import src.game as game

import src.pages.confrontcamel as confront_camel
import src.pages.inventory as inventory

from random import randint
from time import sleep

def display():
    game.print_seperator()
    game.print_rand_location("What happened?")
    game.print_rand_location("Where am I?")
    game.print_rand_location("Where is this?")
    game.print_rand_location("Where is everyone?")
    game.print_rand_location("What's going on?")
    game.print_rand_location("wake up.")
    game.print_rand_location("...")
    game.print_rand_location("WAKE UP")
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

options_played = False
def display3():
    global options_played
    options_printer = print if options_played else game.print_dialogue
    game.print_seperator()
    print(game.art.get("wake"))
    game.print_seperator()
    options_printer("What do you want to do?")
    print()
    options_printer("[1] Attempt to confront the camel")
    options_printer("[2] Pretend to stay unconscious")
    options_printer("[3] Stand up and run as far as you can")
    options_printer("\n[4] Open Inventory")
    game.print_seperator()
    game.set_page(display3, receive)
    options_played = True

def receive(inp: str):
    if inp == "1":
        game.set_page(confront_camel.display, confront_camel.receive)
    elif inp == "4":
        game.set_return_page(display3, receive)
        game.set_page(inventory.display, inventory.receive)
