# 1.1 Is unique

#Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?.

def is_unique(string):
    chars = {}
    for c in string:
        if(chars.get(c)):
            return False
        else:
            chars[c] = 1
    return True


ans = is_unique("HELLO")
print(ans)