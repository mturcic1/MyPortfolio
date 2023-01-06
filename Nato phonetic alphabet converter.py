import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}

program_on = True
while program_on:
    word = input("Please enter a word: ")
    letters = [c.upper() for c in word]
    try:
        for item in letters:
            print(alphabet_dict[item])
            program_on = False
    except KeyError:
        print("Sorry, only letters in alphabet.")
