#Paper 2A
#insertionSort


def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j -1 
        while (i>-1 and A[i] > key):
            A[i+1] = A[i]
            i = i -1
        A[i + 1] = key


def calRange(A):
    range = A[-1] - A[0]
    print("The range is ",range)


def calMedian(A):
    if(len(A)%2 == 0):
        median = (A[len(A) // 2] + A[(len(A) // 2) - 1]) / 2

    else:
        median = A[len(A) // 2]

    
    print("The median is", median)
    

##########################


A = []

for i in range(9):
    mark = int(input("Enter mark of student "+str(i+1)+": "))
    A.append(mark)


print("Before sorting: ",A)
insertionSort(A)
print("After sorting: ",A)


calRange(A)
calMedian(A)

