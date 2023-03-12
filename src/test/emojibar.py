from sys import argv

health = int(argv[1])

print("❤️" * (health // 10), end="")
if health % 10 >= 0:
    print("💔", end="")
if health <= 90:
    print("🖤" * ((100 - health) // 10))