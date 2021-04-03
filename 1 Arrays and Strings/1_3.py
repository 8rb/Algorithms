# 1.3 URLify

# Write a method to replace all spaces in a string with %20.
# You may assume that the string has sufficient space at the end
# to hold additional characters, and that you are given the "true"
# length of the string

# The following solution has a runtime of O(n) since we just iterate over
# the size of the string. This solution creates a new string from an array.

def urlify(s, n):
    new_string = []
    for i in range(n):
        if(s[i] == " "):
            new_string.append("%20")
        else:
            new_string.append(s[i])
    return "".join(new_string)

print(urlify("Mr John Smith", 13))

# A different solution without using an extra 
# string/list might be asked.