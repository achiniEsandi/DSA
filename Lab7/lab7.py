
def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key



A = []
count = 1
while(True):
    num = int(input("Enter a number "+str(count)+" (-1 to exit after 10th number): "))  #enter -1 to exit
    count+=1
    if(count>20):
        break
    elif(count>10 and num == -1):
        break
    A.append(num)

        
print("Before sorting: ",A)    
insertionSort(A)
print("After sorting: ",A)
