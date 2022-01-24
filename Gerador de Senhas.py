import random
from symtable import Symbol
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER = '0123456789'
Symbol = '[]{}#()*;._-'

all = lower + upper + NUMBER + Symbol
lenght = 9
password = "".join(random.sample(all,lenght))
print('The password you generated is:' ,password)