# 1.4 Palindrome Permutation

# Given a string, write a function to check if it is a permutation
# of a palindrome. A palidnrome is a word or phrase that is the same
# forwards and backwaards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters.

from collections import deque

def count_chars(s):
    char_count = {}
    s = s.lower()
    real_size = 0
    for c in s:
        if(c in char_count):
            char_count[c]+=1
            real_size+=1
        else:
            if(c != " "):
                char_count[c]=1
                real_size+=1
    return char_count, real_size

def generate_permutations(char_count, odd_key):
    chars = char_count
    d = deque()

    if(odd_key != ""): # There's an odd char count
        d.append(odd_key)
        chars[odd_key]-=1
    
    for key in chars:
        for i in range(chars[key]):
            if(i % 2 == 0):
                d.append(key)
            else:
                d.appendleft(key)
    
    ans = "True (permutations: '" + "".join(d) + "', etc)"
    return ans

def palindrome_permutation(s):
    char_count, s_size = count_chars(s)
    odd_key = ""
    if(s_size % 2 != 0):
        odd_count = 0
        for key in char_count:
            if(char_count[key] % 2 != 0):
                odd_count+=1
                odd_key = key
            if(odd_count > 1):
                return False
    else:
        for key in char_count:
            if(char_count[key] % 2 != 0):
                return False

    return generate_permutations(char_count, odd_key)

print(palindrome_permutation("taco cat"))