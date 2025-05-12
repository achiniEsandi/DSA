#Paper 2A
#selectionSort

def selectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1, n):
            if(A[i] < A[smallest]):
               smallest = i
        A[j] , A[smallest] =  A[smallest], A[j] 


def calRange(A):
    range = A[-1] - A[0]
    return range


def calMedian(A):
    if(len(A)%2 ==0):
        median = (A[len(A) // 2] + A[(len(A) // 2)-1] ) / 2

    else:
        median = A[len(A) // 2]

    return median


A = []

for i in range(9):
    mark = int(input("Enter mark of student "+str(i+1)+": "))
    A.append(mark)

print("Before sorting: ", A)

selectionSort(A)

print("After sorting: ", A)

print("Range: ",calRange(A))
print("Median: ",calMedian(A))
        
    
