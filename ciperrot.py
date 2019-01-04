
from pprint import pprint

s = raw_input('Please Enter Your caesar chiffre:\n').upper()
Z = ord('Z')
every = []

print('\n')
for i in range(0,25):
        z = ''
        for c in s:
                if c.isalpha():
                        f  = (ord(c) + i - 26) if ord(c)+i > Z else ord(c)+i
                else:
                        f  = 32
                z += chr(f)
        print( z )
