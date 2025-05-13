def selectionSort(A):
    n = len(A)
    for j in range(n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]



def maxSize(A):
    max = A[-1]
    return max

def minSize(A):
    min = A[0]
    return min

def calRange(A):
    range = A[-1] - A[0]
    return range

def median(A):
    if(len(A) % 2 == 0):
        median = ( A[len(A) // 2] + A[(len(A) // 2) - 1] ) // 2

    else:
        median = A[len(A) // 2]
        
    return median
        
        
def descendingOrder(A):
    return sorted(A, reverse=True)

#############################################

A = []
while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        break
    A.append(num)

print()
print("Before sorting: ",A)
selectionSort(A)

print("After sorting: ",A)
print("Max num of list: ",maxSize(A))
print("Min num of list: ",minSize(A))
print("Range of list: ",calRange(A))
print("Median of list: ",median(A))
print("Descending order of the list:",descendingOrder(A))   


