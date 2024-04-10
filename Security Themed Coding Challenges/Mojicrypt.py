#! /usr/bin/python3

task = input("Enter 1 for Red Pill 🔴 OR 2 for Blue Pill 🔵\n")

mojidict = {
	'a': '😀', 'b': '😃', 'c': '😄', 'd': '😁', 'e': '😆', 'f': '😅', 'g': '🤣', 'h': '😂', 'i': '🙂', 'j': '🙃',
	'k': '😉', 'l': '😊', 'm': '😇', 'n': '🥰', 'o': '😍', 'p': '🥵', 'q': '🥶', 'r': '🥴', 's': '😘', 't': '😗',
	'u': '😚', 'v': '😙', 'w': '🥲', 'x': '😋', 'y': '😛', 'z': '😜', 'A': '🤪', 'B': '🤨', 'C': '🧐', 'D': '🤫',
	'E': '🤭', 'F': '🤗', 'G': '🤔', 'H': '🤐', 'I': '🤒', 'J': '🤕', 'K': '🤑', 'L': '🤠', 'M': '🤡', 'N': '🤳',
	'O': '🤴', 'P': '🤵', 'Q': '🤷', 'R': '🤦', 'S': '🤷‍', 'T': '🤷‍', 'U': '🤴‍', 'V': '🤴‍', 'W': '🤵‍', 'X': '🤵‍', 'Y': '🤰',
	'Z': '🤱', '0': '🥳', '1': '🥺', '2': '🥹', '3': '🥻', '4': '🥰', '5': '🤎', '6': '🖤', '7': '🤍', '8': '💘',
	'9': '💝', '!': '😽', '"': '🙀', '#': '😻', '$': '😼', '%': '😽', '&': '🙀', "'": '😿', '(': '😹', ')': '😸',
	'*': '😺', '+': '🤲', ',': '🙌', '-': '🤲‍🧑', '.': '🤌', '/': '🙏', ':': '🖖', ';': '🤟', '<': '✌️', '=': '🤞',
	'>': '🖕', '?': '🚶', '@': '✊', '[': '👊', '\\': '🙅', ']': '🙆', '^': '🙋', '_': '🙇', '`': '🤙', '{': '💪',
	'|': '🦾', '}': '🦿', '~': '🦻', ' ': '👍'
}

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
