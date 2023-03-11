from .. import game

import src.pages.menu as menu

@game.wrap_seperators
def display():
	for line in game.art.get("about_camel_banner").split("\n"):
		game.print_centered(line)
	print()
	game.print_seperator()
	game.print_centered("ABOUT CAMELGAME")
	game.print_seperator()
	print("Camelgame is a text-based RPG / adventure game")
	print("about a camel and a journey!\n")
	print("Credits:")
	print("Programmer - Wilson Krabs")
	print("Narrative Designer - Mikolaj Jankowski")
	print("ASCII Art - asciiart.eu")
	print("Solitary Ship Repairman - Mikolaj Jankowski")

def receive(inp: str):
	game.set_page(menu.display, menu.receive)