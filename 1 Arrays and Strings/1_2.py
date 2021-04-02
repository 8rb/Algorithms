# 1.2 Check-Permutation

# Given two strings, write a method to decide if one is 
# a permutation of the other

# First Solution is O(NlogN) since the sorting operation
# is O(NlogN) and string comparison is at most O(n)

def check_permutation(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if(s1 == s2):
        return True
    else:
        return False

print(check_permutation("ABBBBBB", "BBBABBB"))

# Second Solution is O(N) since we iterate over each string
# and adding/accesing/modifying a value in a dictionary has
# an amortized complexity of O(1)

def check_permutation2(s1, s2):
    dic1 = {}
    dic2 = {}
    for c in s1:
        if(c in dic1):
            dic1[c]+=1
        else:
            dic1[c]=1

    for c in s2:
        if(c in dic2):
            dic2[c]+=1
        else:
            dic2[c]=1
    
    if(dic1 == dic2):
        return True
    else:
        return False

print(check_permutation2("ABBBBBB", "BBBABBB"))
