def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if(A[i]> A[j]) :
               A[i], A[j] = A[j], A[i]

A= []
while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        break
    elif(num<-1):
        print("Enter a positive number")
        continue
    else:
        A.append(num)
        
print("Before sorting: ",A)
bubbleSort(A)
print("After sorting: ",A)


descending = sorted(A, reverse=True)
print("After reversing: ",descending)


