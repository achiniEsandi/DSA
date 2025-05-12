#Paper Number 4


#def calSum(n):
#    if(n == 1):
#        return n
 #   else:
 #       sum = 1
 #       for i in range(1,n):
  #          sum= sum + i
  #      return sum


def calSum(n):
    if(n == 1):
        return n
    else:
        return calSum(n-1) + (n-1) 
    

while(True):
    num = int(input("Enter number: "))
    if(num == -1): 
        print("Output: Finished")
        break
    else:
        print("Output: ",calSum(num)) 
