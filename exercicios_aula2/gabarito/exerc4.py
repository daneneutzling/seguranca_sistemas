import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
letters = []

for letter in SYMBOLS:
	letters.append(letter)

number_messages = int(input("How many messages?"))
size_messages = int(input("Which length?"))
messages = [''] * number_messages
for i in range(number_messages):
	for j in range(size_messages):
		messages[i] += letters[0]
		print(messages[i])
		random.shuffle(letters)
	print('')
print(messages)
