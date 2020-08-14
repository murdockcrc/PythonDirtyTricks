from array import array
from random import random

# Super-efficient way to create and save large array in binary file format
floats = array('d', (random() for i in range (10**7)))
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

print(len(floats))