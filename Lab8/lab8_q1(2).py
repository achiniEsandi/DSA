def selectionSort(A):
    n = len(A)
    for j in range(0,n):
        smallest = j
        for i in range(j+1,n):
            if(A[i] < A[smallest]):
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

def calMax(A):
    return A[-1]

def descending(A):
    return sorted(A, reverse=True)

def median(A):
    if(len(A)%2 == 0):
        median = ( A[len(A)//2] + A[(len(A)//2)-1] ) / 2

    else:
        median = A[len(A)//2]
    return median


A = []
while(True):
    num = int(input("Enter number (-1 to exit): "))

    if(num == -1):
        print("Program ended")
        break

    elif(num < 0):
        print("Enter a positive number")
        continue

    A.append(num)

print()
print("Before sorting: ",A)

selectionSort(A)
print("After sorting: ",A)


print("Max: ",calMax(A))
print("Min: ",A[0])

calRange = A[-1] - A[0]
print("Range: ",calRange)
        
print("Reverse order: ",descending(A))
print("Median: ",median(A))
















