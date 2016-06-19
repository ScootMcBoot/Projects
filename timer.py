#Testing Time stuff

import time
import sys

foo = ["Hello", "World"]
snoo = [" "]
bar = ['World', 'Hello']
x = foo + snoo + bar

for string in x:
	print string
	time.sleep(.5)
snoo = ' '
text = "Hack the planet."
for char in text:
	print char + snoo
	time.sleep(.5)

text = "Hack the planet."
for character in text:
	sys.stdout.write(character)
	time.sleep(.2)