# This code loops through each character in the input string, checks if it's a lowercase letter, 
# and decodes it using the formula chr(ord('a') + ord('z') - ord(char)). 
# This formula takes the ASCII value of the input character, subtracts it from the ASCII value of 'z', adds the ASCII value of 'a', 
# and converts the resulting ASCII value back to a character. If the character is not a lowercase letter, it's left untouched.

#Note that this solution assumes that the input string only contains lowercase letters, uppercase letters, and punctuation. If there are any other characters (such as spaces or numbers), they will also be left untouched.

def solution(s):
    decoded = ""
    for char in s:
        if char.islower():
            decoded += chr(ord('a') + ord('z') - ord(char))
        else:
            decoded += char
    return decoded