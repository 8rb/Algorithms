# 1.5 One Away

# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are
# one edit (or zero edits) away

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# pale, alep -> false (To discard hash tables)

def one_away(s1, s2):
    size1 = len(s1)
    size2 = len(s2)
    if(size1 == size2):
        #Only replace is posible since the other operations take more than 1 edit
        one_diff = False
        if(s1 == s2):
            return True
        for i in range(size1):
            if(s1[i] != s2[i]):
                if(one_diff):
                    return False
                one_diff = True
        return True

    elif(abs(size1 - size2) <= 1):
        # Only one insert or remove is posible since replace would take more than 1 edit
        if(size1 < size2):
            # Swap so s1 is always the bigger string
            size2, size1 = size2, size1
            s1, s2 = s1, s2
        one_diff = False
        i1 = 0
        for i2 in range(size2):
            if(s1[i1] != s2[i2]):
                if(one_diff):
                    return False
                one_diff = True
                i1+=1
            i1+=1
        return True
    else:
        # A difference of more than one char between th strings is only possible by doing more than 1 edit
        return False

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bae"))
print(one_away("pale", "alep"))