
def binarySearch(A, min, max, key):
    if(max < min):
        return False
    else:
        mid = (min + max) // 2
        if (A[mid] > key):
            return binarySearch(A, min, mid-1, key)

        elif(A[mid] < key):
            return binarySearch(A, mid+1, max, key)
        else:
            return mid


A = []
while(True):
    num = int(input("Enter a number: "))
    if(num == -1):
        break
    elif(num < -1):
        print("Enter a positive number")
        continue
    else:
        A.append(num)


print()
print("Elements: ",A)
print()

key = int(input("Enter a key to search: "))
index = binarySearch(A,0,len(A),key)

if(index == -1):
    print("Element not forund")

else:
    print(str(key)+" found at index ",str(index))
