def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

        

def median(A):
    if(len(A)%2 == 0):
        median = (A[len(A) // 2] + A[(len(A) // 2) - 1]) / 2
        return median
    else:
        median = A[len(A) // 2]

    return median


def calRange(A):
    return (A[-1] - A[0])
        


A = []
i = 0
while i < 8:
    mark = int(input("Enter mark of student " + str(i+1) + " : "))

    if mark < 0:
        print("Enter a positive mark\n")
        continue

    A.append(mark)
    i += 1   # Only increment i if a valid mark is entered




print("List of marks: ",A)
insertionSort(A)
print("List of sorted marks: ",A)
print("Range: ", calRange(A))
print("Median: ",median(A))
    
    
               
