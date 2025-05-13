def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if(A[j] <= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


A = []
while(True):
    num = int(input("Enter number (-1 to exit) : "))
    if (num == -1):
        break
    elif(num < -1):
        print("Enter a positive number")
        continue
    else:
        A.append(num)
        
print("Before partitioning: ",A)


if len(A) > 1:
    pivot_index = partition(A, 0, len(A)-1)  # safer
    print("Pivot index:", pivot_index)
    print("After partitioning:", A)
else:
    print("Not enough elements to partition.")
    



#####################################

def quicksort(A,p,r):
    if(p<r):
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)




















































    
