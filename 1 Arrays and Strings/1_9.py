# 1.9 String Rotation

# Assume you have a method isSubstring which checks if one
# word is a substring of another. Given two strings, s1 and s2
# write code to check if s1 is a rotation of s2 using only
# one call to isSubstring.

# Test case:
# "waterbottle" is a rotation of " erbottlewat

# The following solution uses a two pointers approach to solve
# the problem String Rotation. It has a runtime of O(N) since
# s1 and s2 are supposed to have the same length and at most
# we iterate over the length of the concatenated string (2N).

def string_rotation(s1, s2):
    s2 = s2 + s2
    n1 = len(s1)
    n2 = len(s2)
    i = 0
    j = 0
    while(i != n1 and j != n2):
        if(s1[i] == s2[j]):
            i+=1
            j+=1
        else:
            j+=1
            i=0
    
    if(i == n1):
        return True
    return False

print(string_rotation("waterbottle", "erbottlewat"))

# The second approach uses a method called "isSubstring"
# which returns true if the second string is a substring 
# of the first one. We concatenate the first string
# so that if the second one is a substring of the first one
# it means that is also a rotation.

def string_rotation2(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    s1s1 = s1 + s1
    if(n1 == n2):
        return isSubstring(s1s1, s2)
