#python2.7.18

"""

### 1. Let's generate list of prime numbers
from 0 to 1000000000000000

using python2 for e

end of 1 


### 2. Time for prime Relate to #30 
- Using list of 
- set time 
- Generate a radom 100 digit
- Loop over if it's prime (do we already have list prime numbers)

#

"""

# Start of code 

import time

## First let's be simple, we just iterate over 8,9 10, 11 digits just to
# to compare time with python3.12, as written in study_notes/test_fermat..

import os

print("os pid",os.getpid())

def time_for_digits(p):
	then = time.time()
	p = int(p/2)
	for i in range(2,p):
		if (( p % i) != 0):
			continue # nothing no need to write
	end = time.time() - then
	print("total time in seconds is ", end)
print("time for 1000000 7")
time_for_digits(1000000)
print("time 10000000 8")
time_for_digits(10000000)
print("time for 9 time_for_digits(1000000)")
time_for_digits(100000000)
print("time_for_digits(10000000)) 10")
time_for_digits(1000000000)

print("time_for_digits(10000000)) 11")
time_for_digits(10000000000)
