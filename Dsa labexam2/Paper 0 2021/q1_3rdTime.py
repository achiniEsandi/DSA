def sequence(n):    #defining function
    if(n==1):
        return n
    else:
        return n + sequence(n-1)


while(True):
    num = int(input("Enter number: "))    #taking user inputs
    if(num == -1):
        print("Output: Finished")
        break    #the loop will exit 
    else:
        print("Output: ",sequence(num))
