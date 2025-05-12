#bubble sort


#==============================
#B = [10, 30, 20, 50]

#temp = B[1]
#B[1] = B[3]
#B[3] = temp
#print(B)
#==============================

#B[1], B[3] = B[3], B[1]
#print(B)
#==============================


#def bubbleSort(A):
#    for i in range(len(A)):
#        for j in range(i+1, len(A)):
#           if(A[i]>A[j]):
#                A[i], A[j] = A[j], A[i]
        
#A = [12,3,56,7,20,1]

#bubbleSort(A)

#print(A)

#==============================

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if(A[i]> A[j]) :
               A[i], A[j] = A[j], A[i]
               

A = []  #empty array
for i in range(8):
    num = int(input("Enter number to sort: "))
    A.append(num)

               
bubbleSort(A)
print(A)               

#==============================
