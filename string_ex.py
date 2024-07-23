## Note : Strings are immutable iterable. This means that irrespective of whatever function is called on the string, the original string remains unchanged.
# Important string functions :
# 1. string.endswith("rry") - this function tells whether the string ends with the string "rry" or not. Return true if the string ends with the string "rry and false otherwise.
# 2. string.count("v")  - this function counts the total number of occurrences of any character in the string.
# 3  string.capitalize() - capitalizes the first character of the string
# 4. string.find(word) - this function finds the word and returns the index of the first occurrence of the word in the string
# 5. string.strip() - this function strips the leading and trailing whitespace from the string
# 6. string.lstrip() - this function strips the leading whitespace from the string
# 7. string.rstrip() - this function strips the trailing whitespace from the string
# 8. string.replace(old, new) - this function replaces the old character with the new character
# 9. string.split() - this function splits the string into list of substrings based on the given separator.
# 10. string.join(iterable) - this function joins the elements of an iterable with the string as a separator. Example: " ".join(["hello", "world"]) returns "hello world"


""" Practice set"""

# 1. Write a python program to display a user entered name followed by good Afternoon.
name = input("Enter your name\n")
print(f"{name}, Good Afternoon!")

# 2. Write a python program to fill in a letter template
letter = """
     Dear <|Name|>, 
     You are selected!
     <|Date|>
     """
print(letter.replace("<|Name|>", name).replace("<|Date|>", "23rd July, 2024"))


# 3. Write a program to detect a double space in  a string
print(name.find("  "))
# replace the double spaces with single spaces
print(name.replace("  ", " "))
# 4. Write a program to foramt the following letter using escape sequence characters.  Letter = " Dear John, this python cocurse rocks!!!"
print(f"Dear John,\n\t This python cocurse rocks!,\nThanks.")
