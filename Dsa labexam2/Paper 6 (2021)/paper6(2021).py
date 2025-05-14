
def seq(n):
    if(n == 1):
        return n
    else:
        return 2 * seq(n - 1) + 1


while(True):
    num = int(input("Enter number: "))

    if(num == -1):
        print("Output: Finished")
        break

    elif(num < -1):
        print("Enter a positive number")
        continue

    else:
        print("Output: ",seq(num))
        
