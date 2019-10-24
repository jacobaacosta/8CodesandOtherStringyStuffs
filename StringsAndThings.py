# Strings

# Concatenation
#   2 or more strings and put them together

firstName = "Wilma"
lastName = "Flintstone"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition
#   repitition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row. "*3 + " your boat")
    print("gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()