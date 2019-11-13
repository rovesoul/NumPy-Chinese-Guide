import numpy as np  

b = [1,2,3,4,5]
c = [6,7,8,9,0]
# 得到二维矩阵
d = np.r_[[b],[c]]
print(d)

# 分行取出矩阵
e=d[0]
f=d[1]
g=np.r_[[f],[e]]
print('\n',g)


def is_even(num):
  return num % 2 == 0
is_even(10)

import sys
print(sys.getsizeof(99999999)) # 28
print(sys.getsizeof("Python")) # 55

language = "sumer-minus"
reversed_language = language[::-1]
print(reversed_language)  # sunim-remus


def repeat(string, n):
    return (string * n)
a=repeat('oop!',10) 
print(a)

def palindrome(string):
    return string == string[::-1]
print(palindrome('python')) # False

strings = ['老虎', '老鼠', '蟑螂']
print('kill'.join(strings))
