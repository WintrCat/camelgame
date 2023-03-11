from os import system
from time import sleep

DEV_MODE = True

def adjusted_sleep(secs: float):
	if DEV_MODE: secs = secs / 30
	sleep(secs)

page: dict = None
def get_page() -> dict:
	return page
def set_page(display_fn, receiver_fn):
	global page
	page = {
		"display": display_fn,
		"receiver": receiver_fn
	}

return_page: dict = None
def get_return_page() -> dict:
	return return_page
def set_return_page(display_fn, receiver_fn):
	global return_page
	return_page = {
		"display": display_fn,
		"receiver": receiver_fn
	}

def clear():
	system("cls")

def print_seperator():
	print("(==========================+==========================)")
def wrap_seperators(display_fn):
	def wrapper():
		print_seperator()
		display_fn()
		print_seperator()
	return wrapper

def print_centered(text: str):
	print(" " * (screen_length // 2 - len(text) // 2), end="")
	print(text)

def print_dialogue(text: str, period: float = 0.03):
	for char in list(text):
		print(char, end="", flush=True)
		adjusted_sleep(period)
	print()

screen_length = 55

art = {
	"camel_banner": open("assets/camel.txt", "r", encoding="utf-8").read(),
	"about_camel_banner": open("assets/about.txt", "r").read(),
	"wake": open("assets/wake.txt", "r").read()
}