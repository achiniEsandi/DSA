def selectionSort(A):
    n = len(A)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]
