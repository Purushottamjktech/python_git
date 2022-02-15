inp = "A very very long string from user input"
new_input = ""
for i, letter in enumerate(inp):
    if i % 20 == 0:
        new_input += '\n'
    new_input += letter

# this is just because at the beginning too a `\n` character gets added
new_input = new_input[1:]
print(new_input)