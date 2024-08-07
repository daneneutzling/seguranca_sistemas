import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
letters = []

for letter in SYMBOLS:
	letters.append(letter)

messages = [''] * 5
for i in range(5):
	for j in range(10):
		messages[i] += letters[0]
		print(messages[i])
		random.shuffle(letters)
	print('')
print(messages)
