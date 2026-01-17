# Mad Libs Game
# A fun word game where the user creates a story
# by filling in the blanks with random words

print("🎉 Welcome to the Mad Libs Game 🎉")
print("Please enter the following words:\n")

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter another adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter one more adjective (description): ")

print("\n📝 Your Mad Libs Story:\n")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")
