def palindrome_check(string):
    string = string.lower()
    if string == string[::-1]:
        print(f"Yes-{string} is a palindrome")
    else:
        print(f"No-{string} is not a palindrome")

string = "malayalam"
palindrome_check(string)
