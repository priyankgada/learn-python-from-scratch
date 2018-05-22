#!/usr/bin/python
#www.youtube.com/priyankgada

num = int(raw_input("Give me a number : "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print num, " is not a prime number"
            break
        else:
            print num, "is a prime number"
            break
            
else:
    print num, "is not valid"
            
