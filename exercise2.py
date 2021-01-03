def last_element(abc):
    x = len(abc)
    return abc[x-1]

print(last_element([1,2,3,5]))

def single_letter_count(word,l):
    x = word.upper().count(l.upper())
    return x

print(single_letter_count("ABCABC","A"))

def multiple_letter_count(str1):
    dic = {}
    str1.insert(0,'a')
    if type(str1).__name__ != "doc":
        print(str1[-1])
    for l in str1:
        print(type(str1).__name__)
        dic[l] = str1.count(l)
    return dic

print(multiple_letter_count(["a","e","i","o","u","a"]))
