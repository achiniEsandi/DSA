def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


def calRange(A):
    return A[-1] - A[0]

def median(A):
    if(len(A)%2 == 0):
        median = ( A[len(A)//2] + A[(len(A)//2)- 1] ) / 2
    else:
        median = A[len(A)//2]
    return median
    


def descending(A):
    return sorted(A, reverse=True)



A = []
i = 0
while(i<8):
    mark = int(input("Enter mark: "))
    if (mark<0):
        print("Enter a valid mark")
        continue
    
    i = i + 1
    A.append(mark)
    
print()        
print("Before sorting: ",A)
bubbleSort(A)
print("After sorting: ",A)
print("Median",median(A))
print("Range: ",calRange(A))

