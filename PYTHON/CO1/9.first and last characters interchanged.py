#exchanging first and last character
def stringch(str1):
    return str1[-1:]+str1[1:-1]+str1[:1]
print(stringch('python'))
print(stringch('data structure'))

