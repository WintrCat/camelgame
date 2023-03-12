import src.game as game

import src.pages.about as about
import src.pages.wake as wake

@game.wrap_seperators
def display():
	print(game.art.get("camel_banner"))
	game.print_seperator()
	game.print_centered("CAMELGAME: The great text adventure")
	game.print_seperator()
	print("[1] Play\n[2] About\n[3] Exit")

@game.wrap_seperators
def dev_mode_display():
	print("💻 DEVELOPER MODE")
	print("You are currently in developer mode. If this should not")
	print("be the case, please go into the game files and open the")
	print("src/game.py file. At the top, change DEV_MODE = True to")
	print("DEV_MODE = False. Alternatively, just enter \"wake\"")
	print("below to start from the normal beginning scene.")
	game.print_seperator()

	page = input("Select starting page: ")
	try:
		exec(f"import src.pages.{page} as {page}")
	except:
		print("That is not the name of a valid page...")
		game.adjusted_sleep(2)
		return
	
	section = input("Select page section: ")
	try:
		section = int(section)
		if section < 1: raise RuntimeError()
	except:
		print("That is an invalid page section number...")
		game.adjusted_sleep(2)
		return

	exec(f"game.set_page({page}.display{section if section > 1 else ''}, {page}.receive)")

def receive(inp: str):
	if inp == "1":
		if game.DEV_MODE:
			game.clear()
			dev_mode_display()
		else:
			game.set_page(wake.display, wake.receive)
	elif inp == "2":
		game.set_page(about.display, about.receive)
	elif inp == "3":
		game.clear()
		game.print_dialogue("Now exiting Camelgame...")
		exit()