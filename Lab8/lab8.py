def selectionSort(A):
    n = len(A)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]


A = []
while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        break
    A.append(num)

print("Before sorting: ",A)
selectionSort(A)

print("Before sorting: ",A)
