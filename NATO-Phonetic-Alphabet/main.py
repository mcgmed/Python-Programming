# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)

def generate_phonetic():
    name = input('What is your name?: ').upper()
    try:
        nato_coded = [nato_dict[letter] for letter in name]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(nato_coded)
generate_phonetic()
