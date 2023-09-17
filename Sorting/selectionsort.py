# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

for i in range(0,len(A)):
    lowest=i
    for j in range(i+1,len(A)):
        if (A[j]<A[lowest]):
            lowest = j
    A[i],A[lowest] = A[lowest],A[i]

print (A)
        
