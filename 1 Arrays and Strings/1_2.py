# Check-Permutation

# Given two strings, write a method to decide if one is 
# a permutation of the other

# First Answer is O(NlogN) since the sorting operation
# is O(NlogN) and string comparison is at most O(n)

def check_permutation(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if(s1 == s2):
        return True
    else:
        return False

print(check_permutation("ABBBBBB", "BBBABBB"))

