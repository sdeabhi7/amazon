'''
Given an array of alphabets - ['b','f','a','c','g','a','f','b','b','d']
arrange them in a manner such that alphabets which are > 1 appears first with their frequency of alphabets to follow 
and all those aplhabets that are single appear at the end in the same order of their appearance.

output - [b,b,b,f,f,a,a,c,g,d]
'''

def arrange_alphabets(alphabets):
    value = {}
    temp = []
    for i in alphabets:
        value[i] = alphabets.count(i)
    for i in value.items():
        temp += list(i[0] * i[1])
    return temp

print(arrange_alphabets(['b','f','a','c','g','a','f','b','b','d']))