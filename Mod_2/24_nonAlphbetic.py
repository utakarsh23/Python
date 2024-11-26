# Write a Python program to remove all non-alphanumeric characters (i.e., characters that
# are neither letters nor digits) from a given string using regular expressions.
# Input: “ Hello ! This is a test string. ”
# Output: “HelloThisisateststring”
# Note: All spaces are also considered as Non-alphanumeric character.

w = 'Hello ! The String was idk.'
for i in w:
    if(i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' ):
        print(i, end='')