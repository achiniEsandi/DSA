
def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if(A[j] <= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A,p,r):
    if(p<r):
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)



A = []
while(True):
    num = int(input("Enter a number: "))

    if(num == -1):
        print("Progam ended")
        break

    elif(num < 0):
        print("Enter a positive number")
        continue

    A.append(num)
    
print("Original list: ",A)  

p=0
r = len(A)-1

q = partition(A,p,r)
#quicksort(A,p,r)
print(A)

    
