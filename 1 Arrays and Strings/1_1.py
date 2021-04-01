# 1.1 Is unique

#Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?.

def is_unique(string):
    chars = {}
    for c in string:
        if(c in chars):
            return False
        else:
            chars[c] = 1
    return True

ans = is_unique("HELO")
print(ans)

# Time complexity: Amortized O(n) where n is the length of the string
# Amortized since adding a value to a dictionary is amortized O(1)
# And checking if a key exists is also amortized O(1)
# Pros: Algorithm will stop when it finds the first repeated character inside
# the string, so most of the times, runtime would be less than O(n)