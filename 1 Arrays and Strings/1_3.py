# 1.3 URLify

# Write a method to replace all spaces in a string with %20.
# You may assume that the string has sufficient space at the end
# to hold additional characters, and that you are given the "true"
# length of the string

# The following solution has a runtime of O(n) since we just iterate over
# the size of the string. This solution creates a new string from an array.

def urlify(s, n):
    new_string = []
    for c in s:
        if(c == " "):
            new_string.append("%20")
        else:
            new_string.append(c)
    return "".join(new_string)

print(urlify("Mr John Smith", 13))

# A different solution without using an extra 
# string/list might be asked.

# Since strings in Python are immutable, it's impossible to
# Give a solution without using an extra list/string
# Here's a second solution using an empty string instead of a list

def urlify2(s, n):
    new_string = ""
    i = 0
    while i != len(s):
        if(s[i] != " "):
            new_string+=s[i]
        else:
            new_string+="%20"
        i+=1
    return new_string

# print(urlify2("Mr John Smith", 13))