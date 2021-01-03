import sys
import os

# print('hello')

def interleave(str1, str2):
    output = zip(str1,str2)
    # print(output)

    output2 = ''.join(''.join(i) for i in zip(str1,str2))
    print(output2)

    return output

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(names):
    nz = list(map(lambda n: "{} {}".format(n['first'],n['last']),names))
    print(nz)


interleave('hi','no')

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names)
