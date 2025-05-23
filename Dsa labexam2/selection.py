def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
             A[i + 1] = A[i]
             i = i - 1
        A[i + 1] = key    
        
def calRange(A):
    return A[-1] - A[0]



        
A = []
i=0
while(i<9):
    num = int(input("Enter marks:"))
    if(num < 0):
        print("Enter a valid number")
        continue

    A.append(num)
    i=i+1

total = sum(A)

print("Before sorting:",A)
insertionSort(A)
print("After Sorting",A)
print("Range:", calRange(A))

print(total)

def median(A):
    if(len(A)% 2 == 0):
        return ( A[len(A) // 2] + A[(len(A) // 2)-1] ) / 2

    else:
        return A[len(A) // 2]

print(median(A))
        
decending = sorted(A, reverse = True)
print(decending)
