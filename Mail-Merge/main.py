PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt') as names_list:
    names = names_list.readlines()

with open('Input/Letters/starting_letter.txt') as starting_letter:
    birthday_letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = birthday_letter.replace(PLACEHOLDER, stripped_name)
        with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)
