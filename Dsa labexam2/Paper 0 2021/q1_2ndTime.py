#Paper Number 0


def cal(n):
    if (n == 1):
        return n
    else:
        sum = 0
        for i in range(n+1):
            sum = sum + i
        return sum








while(True):
    num = int(input("Enter number: "))
    if(num == -1):
        print("Output: Finished")
        break

    else:
        print("Output: ",cal(num))





