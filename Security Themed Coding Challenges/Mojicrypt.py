#! /usr/bin/python3

task = input("Enter 1 for Red Pill 🔴 OR 2 for Blue Pill 🔵\n")

mojidict = {
    'a': '🍕', 'A': '🌈','b': '🐱', 'B': '🍎','c': '⚽', 'C': '🌳','d': '🍫', 'D': '👓','e': '🔥', 'E': '⚡','f': '🧸', 'F': '💰','g': '🌵', 'G': '🍷','h': '🦄', 'H': '⛄','i': '🐻', 'I': '🍩','j': '🌍', 'J': '🐶','k': '🍇', 'K': '💍','l': '🎸', 'L': '🥜','m': '!', 'M': '🌙','n': '🍋', 'N': '🐝','o': '💎', 'O': '🌮','p': '🥐', 'P': '👸','q': '☘', 'Q': '⚔','r': '🦋', 'R': '🍊','s': '🎯', 'S': '❌','t': '🐳', 'T': '🌊','u': '🍄', 'U': '🔑','v': '🌗', 'V': '🥚','w': '🏡', 'W': '🌹','x': '🐼', 'X': '🦖','y': '🏆', 'Y': '🎩','z': '🌻', 'Z': '🎬'
}

if (task == "1"):
	name = input("Enter the phrase: ")
	splitted = [*name]
	for i in splitted:
		print(mojidict[i])

elif (task == "2"):
	passphrase = input("Enter the phrase: ")
	splitted = [*passphrase]
	print (splitted)

	for i in splitted:
		for key, value in mojidict.items():
			if value == i:
				print (key)
				break
		else:
			print(f"No key found for character {i}")

else:
	print("Try again.")
