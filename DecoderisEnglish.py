import sys

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
FreqVecEngl = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 1.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]

#---------------------------------------
# End of Global Arrays/Variables
#---------------------------------------

# Creates a freq vec
def createFreqVec(string):
    total = 0
    freqVecInput = []
    for x in string:
        if x != " ":
            total += 1
    lowString = string.lower()
    for x in alphabet:
        temp = 0  # Reset temp for each letter
        for a in lowString:
            if a == x:
                temp += 1
        freq = (temp / total) * 100
        freqVecInput.append(freq)
    return freqVecInput

# Compares the freq vec based on input to English freq vec
def compareVec(list1, list2):
    FreqTotInput = 0
    for val in range(26):  # Should run for over 26 elements
        diff = list1[val] - list2[val]
        diff2 = (diff * diff)
        FreqTotInput += diff2
    return FreqTotInput


#---------------------------------------------
#              End of Functions
#--------------------------------------------



# Asks user for the initial message
initialMessage = input("Input the text you want to decrypt: \n")
print("What you inputted: " + initialMessage)

# Translates the word, letter by letter
minFreqTotInput = float('inf')
bestShift = 0
bestDeshiftedText = ""

for x in range(26):  # try all 26 possible shifts
    deshiftedText = ""  # Reset deshiftedText for each shift attempt
    for char in initialMessage:
        if char.isupper():
            newUpperChar = chr((ord(char) - ord("A") - x) % 26 + ord("A"))
            deshiftedText += newUpperChar
        elif char.islower():
            newLowerChar = chr((ord(char) - ord("a") - x) % 26 + ord("a"))
            deshiftedText += newLowerChar
        else:
            deshiftedText += char
    freqVecInput = createFreqVec(deshiftedText)
    FreqTotInput = compareVec(freqVecInput, FreqVecEngl)
    
 #     
    if FreqTotInput < minFreqTotInput:
        minFreqTotInput = FreqTotInput
        bestShift = x
        bestDeshiftedText = deshiftedText

print(f"Best Shift: {bestShift}")
print(f"Here is the original Unshifted Word: {bestDeshiftedText}")
