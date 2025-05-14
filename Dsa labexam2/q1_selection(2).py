def selectionSort(A):
    n = len(A)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if(A[i] < A[smallest]):
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]



def calRange(A):
    return A[-1] - A[0]


def median(A):
    if(len(A)%2 == 0):
        median = (A[len(A)//2] + A[(len(A)//2)-1] ) / 2

    else:
        median = A[len(A)//2]

    return median


A = []
i = 0
while(i < 9):
    mark = int(input("Enter mark of student "+str(i+1)+": "))

    if(mark < 0):
        print("Enter a positive number\n")
        continue

    i+=1
    A.append(mark)


print()
print("Before sorted: ",A)
selectionSort(A)
print("After sorted: ",A)
print("Range: ",calRange(A))
print("Median: ",median(A))


    
