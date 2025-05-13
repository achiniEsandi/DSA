def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
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
        
print("Before sorting: ",A)

partition(A,2,5)

print("After partitioning:", A)
    























































    
