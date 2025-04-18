'''
You are given a list of strings and a list of int pairs ranges. Each range [x,y] points to the index of list of strings. 
You are given a list of strings and a list of int pairs ranges. Each range [x,y] points to the index of list of strings. Your job is to find out how many strings from list[x] to listy have valid strings. A valid string is basically a string whose starting letter and ending letter is a vowel.

for ex - ["axe", "bat", "ten", "aa", "e"], ranges = [[0,2], [1,4], [1,1]]

O/p - [1, 2, 0]
'''

def vowels(value, ranges):
    k = 'aeiou'
    y = []
    for i in ranges:
        temp = []
        t = 0
        temp = value[i[0]: i[1] + 1]
        for i in temp:
            if i[0] in k and i[-1] in k:
                t += 1      
        y.append(t)
    return y

print(vowels(["axe", "bat", "ten", "aa", "e"], [[0,2], [1,4], [1,1]]))