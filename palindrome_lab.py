#
# Course:       CCPS 109
# Lab:          2 Palindromes
# Due Date:     Feb 10th @ 23:00 hrs
#
# Student:      Sivatma Maharaj
# Student ID:   501043693


# This program demonstrates the use of functions, variable scope and
# recursion.  It asks the user to input a string, it reverses it using a 
# recursive function it and compares it to the original string.  
# If they are the same then the string is a palindrome.
#
# The main loop will repeat indefinitely until the user inputs 'exit'


# format the input string by striping leading and trailing spaces
# changes the string to a lower case
def formatInput(inputstring):
    return inputstring.strip().lower()

# recursive function that reverses the input string
def reverse(inputstring):
    if len(inputstring) == 1:
        return inputstring
    else:
        return reverse(inputstring[1:]) + inputstring[0]

# compares two strings, if they are the same then returns True
# otherwise if the strings are not the same then it returns False
def palindrome(inputstring, reversestring):
    if inputstring == reversestring:
        return True
    else:
        return False

# prints the program output.
# if it's a palindrome it lets you know that it is
# if not a palindrome it lets you know that it is not
def result(inputstring, reversestring):
    if palindrome(inputstring, reversestring):
        print("Your input is a palindrome!!")
    else:
        print("Your input is NOT a palindrome!!")
    print("Original String: "+inputstring)
    print("Reversed String: "+reversestring)
    print("\n")    

# checks to see if the user is trying to exit
# if the input is 'exit' then it returns true
def exitcheck(inputstring):
    if inputstring == "exit":
        return True
    else: 
        return False


# Main section of program
# Runs indefinitely until the user types 'exit'
while True:
    # Game message
    print("Palindrome Game.  Type 'exit' to quit.")

    # Get the user input, format it and reverse it
    inputStr = formatInput(input("Enter your string: "))
    reverseStr = reverse(inputStr)

    # Break from the main loop if it passes the exitcheck
    if exitcheck(inputStr):
        break

    # Print the result of the string reversal    
    result(inputStr, reverseStr)

# Print the exit message
print("\nThanks for playing the Palindrome Game.")     
print("Run 'py palindrome_lab.py' to play again.")
