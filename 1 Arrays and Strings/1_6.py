# 1.6 String Compression

# Implement a method to perform basi string compression using
# the counts of repeated characters. For example, the string
# aabcccccaaa would become a2b1c5a3. If the "compressed"
# string would not become smaller than the original string,
# your methoud should return the original string.
# You can assume the string has only uppercase and lowercase letters.

def string_compression(orig_string):
    string_arr = []
    actual = orig_string[0]
    count = 1
    for i in range(len(orig_string) - 1):
        if(actual == orig_string[i+1]):
            count+=1
        else:
            string_arr.append(actual+str(count))
            actual = orig_string[i+1]
            count = 1
        
        if(i + 1 == len(orig_string) - 1):
            string_arr.append(actual+str(count))

    comp_string = "".join(string_arr)

    if(len(comp_string) >= len(orig_string)):
        return orig_string
    return comp_string

print(string_compression("aabcccccaaa"))
print(string_compression("aabbccddeeff"))
print(string_compression("aaabbddcceeff"))