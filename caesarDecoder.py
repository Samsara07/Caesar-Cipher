# Inverts the process done by the encoderShift

import sys

# Asks user for the initial message
initialMessage = input("Input the text you want to decrypt: \n")
print("What you inputted: " + initialMessage)
shiftVal = input("Input what the original shift used to encrypt your message was: \n")
print("What you inputted: " + shiftVal)



# Translates the word, letter by letter
shiftInt = int(shiftVal)
deshiftedText = ""
for char in initialMessage:
    if char.isupper():
        newUpperChar = chr((ord(char) - ord("A") - shiftInt) % 26 + ord("A"))
        deshiftedText += newUpperChar
    elif char.islower():
        newLowerChar = chr((ord(char) - ord("a") - shiftInt) % 26 + ord("a"))
        deshiftedText += newLowerChar
    else:
        deshiftedText += char

# Prints the final shifted word
print("Here is the original Unshifted Word: " + deshiftedText)