file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()

# With the code below, we don't remember to close our file:

with open('my_file.txt', mode='r') as file:  # read only mode
    contents = file.read()
    print(contents)

with open('my_file.txt', mode='w') as file:  # write mode, in this mode, your document will be replaced with new text.
    file.write('New text.')

with open('my_file.txt', mode='a') as file:  # in this mode, new text appended to your original text.
    file.write('\nNew text.')

with open('new_file.txt', mode='w') as file:
    # if the file doesn't exist, it creates the file automatically in the same directory.
    file.write('New text.')
