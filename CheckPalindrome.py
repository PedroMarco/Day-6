__author__ = 'acpb859'
def main():
    # Prompt the user to enter a string (s in this case is the string variable)
    s1 = input("Enter a string: ").strip()
    s=s1.lower() ##  strip here removes white spaces before or after

    if isPalindrome(s):
      print(s1, "is a palindrome")
    else:
      print(s1, " is not a palindrome")

# Check if a string is a palindrome
def isPalindrome(s):
    # The index of the first character in the string (A letter in this case)
    low = 0

    # The index of the last character in the string
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False # Not a palindrome

        low += 1
        high -= 1

    return True # The string is a palindrome

main() # Call the main function