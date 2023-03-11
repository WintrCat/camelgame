import src.game as game

import src.pages.menu as menu

inp: str = None

def main():
    game.set_page(menu.display, menu.receive)
    while True:
        game.clear()
        game.get_page().get("display")()
        inp = input("> ")
        game.get_page().get("receiver")(inp)