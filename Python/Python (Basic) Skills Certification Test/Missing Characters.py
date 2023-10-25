# This question is a part of Python (Basic) Skills Certification Test

def missingCharacters(s):
    updatedString = ""
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
         ]
    for i in d:
        if (str(i) not in s):
            updatedString += str(i)
    for j in l:
        if (j not in s):
            updatedString += j
    return updatedString


s = "7985interdisciplinary12"
print(missingCharacters(s))
