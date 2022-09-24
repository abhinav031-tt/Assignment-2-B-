'''' Name = Abhinav tiwari

program = dictionary whose keys should be the alphabet from a-z and
          the value should be corresponding ASCII values



'''


dict = {}
for i in range (97,123):
    dict[chr(i)] = i     # return the characters that represents the specified unicode
print(dict)    