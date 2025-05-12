#Paper number 2(2021)

def seq(n):
    if (n == 1):
        return 2
    else:
        return seq(n-1)/2




while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        print("Output: Finished")
        break
    else:
        print("Output: ",seq(num))
