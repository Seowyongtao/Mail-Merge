# TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter = starting_letter.read()

for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as specific_letter:
        specific_letter.write(f"{new_letter}")
