from .. import game

import src.pages.about as about
import src.pages.wake as wake

@game.wrap_seperators
def display():
	print(game.art.get("camel_banner"))
	game.print_seperator()
	game.print_centered("CAMELGAME: The great text adventure")
	game.print_seperator()
	print("[1] Play\n[2] About\n[3] Exit")

def receive(inp: str):
	if inp == "1":
		game.set_page(wake.display, wake.receive)
	elif inp == "2":
		game.set_page(about.display, about.receive)
	elif inp == "3":
		game.clear()
		game.print_dialogue("Now exiting Camelgame...")
		exit()