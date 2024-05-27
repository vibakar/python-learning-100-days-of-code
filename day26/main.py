import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
csv_dict = {row.letter:row.code for (index, row) in df.iterrows()}
user_input = input("Enter the word: ")

# result = [csv_dict[letter] for letter in user_input.upper()]
result = []
for letter in user_input.upper():
    try:
        word = csv_dict[letter]
    except KeyError:
        pass
    else:
        result.append(word)
        
print(result)
