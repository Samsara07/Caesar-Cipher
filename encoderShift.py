import sys

# Asks user for the initial message
initialMessage = input("Input the text you want to encrypt: ")
print("What you inputted: " + initialMessage)

# Asks user for the shift number
shift = input("Input what you want your message to be shifted by: ")
shiftInt = int(shift)

# Translates the word, letter by letter
shiftedText = ""
for char in initialMessage:
    if char.isupper():
        newUpperChar = chr((ord(char) - ord("A") + shiftInt) % 26 + ord("A"))
        shiftedText += newUpperChar
    elif char.islower():
        newLowerChar = chr((ord(char) - ord("a") + shiftInt) % 26 + ord("a"))
        shiftedText += newLowerChar
    else:
        shiftedText += char

# Prints the final shifted word
print(shiftedText)