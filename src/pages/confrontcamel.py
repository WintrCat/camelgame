import src.game as game

import src.profile as Profile

def with_camel_image(fn):
    def wrapper():
        game.print_seperator()
        print(game.art.get("confront_camel"))
        game.print_seperator()
        fn()
    return wrapper

@with_camel_image
def display():
    game.print_dialogue("You decide to get up and confront the camel.")
    game.print_dialogue("You are not fully up yet,")
    game.print_dialogue("But the camel has already turned towards you.")
    game.print_dialogue("It smiles and speaks to you in many tongues,")
    game.print_dialogue("even those that do not exist.")
    game.print_seperator()
    input("> ")
    game.clear()
    display2()

@with_camel_image
def display2():
    game.print_rand_location("Mă înțelegi?")
    game.adjusted_sleep(0.5)
    game.print_rand_location("ተረድተሀኛል?")
    game.adjusted_sleep(0.5)
    game.print_rand_location("নেজানো?")
    game.adjusted_sleep(0.5)
    game.print_rand_location("के तिमी मलाई बुझ्छौं?")
    game.adjusted_sleep(0.5)
    game.print_rand_location("dromedary!")
    game.adjusted_sleep(0.5)
    game.print_seperator()
    input("> ")
    game.clear()
    display3()

@with_camel_image
def display3():
    game.print_dialogue("Camel: Do you understand me?")
    game.adjusted_sleep(1)
    game.print_dialogue("Camel: Traveller, are you okay?")
    game.print_seperator()
    input("> ")
    game.clear()
    display4()

def display4():
    game.print_seperator()
    print(game.art.get("desert"))
    game.print_seperator()
    game.print_dialogue("You look at the camel, then at your surroundings.")
    game.adjusted_sleep(3)
    game.print_dialogue("There is nothing around you for as far as you can see.")
    game.adjusted_sleep(3)
    game.print_dialogue("...Nothing.")
    game.adjusted_sleep(3)
    game.print_dialogue("A land void of life,")
    game.adjusted_sleep(3)
    game.print_dialogue("with only the remains thereof.")
    game.print_seperator()
    input("> ")
    game.clear()
    display5()

@with_camel_image
def display5():
    game.print_dialogue("Camel: Can you hear me traveller?")
    game.adjusted_sleep(3)
    game.print_dialogue("\nYou snap out of your despair and respond to the camel.")
    game.adjusted_sleep(1)
    game.print_dialogue("The camel should really not be able to talk,")
    game.print_dialogue("and you are yet to realise this in your confusion.")
    game.adjusted_sleep(3)
    game.print_dialogue("\nCamel: I saw you in the sand.")
    game.print_dialogue("\nCamel: What are you doing here?")
    game.print_seperator()
    input("> ")
    game.clear()
    display6()

@with_camel_image
def display6():
    game.print_dialogue("In your panic, you shout at the camel.")
    game.print_dialogue("You: Where am I!? Who are you!?")
    game.adjusted_sleep(3)
    game.print_dialogue("The camel stares at you blankly.")
    game.adjusted_sleep(3)
    game.print_dialogue("Camel: Traveller, you must calm down.")
    game.adjusted_sleep(3)
    game.print_dialogue("Camel: I am here only to assist you.")
    game.adjusted_sleep(2)
    game.print_dialogue("Camel: Please, take some water.")
    input("\nPress any key to take the water.")
    print()
    Profile.add_item("Water Bottle", 1)
    game.print_seperator()
    game.print_dialogue("What do you want to do?")
    game.print_dialogue("\n[1] Thank the camel")
    game.print_dialogue("\n[2] Open Inventory")

def receive(inp: str):
    pass