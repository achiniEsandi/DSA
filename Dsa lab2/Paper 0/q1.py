
M = int(input("Enter number m: "))
n = int(input("Enter number n: "))


def Multiply(M, n):
    if n == 1:
        return M
    else:
        return M + Multiply(M, n - 1)


while True:
    result = Multiply(M, n)
    print(result)

    M = int(input("Enter M (-1 to exit) : "))
    if M == -1:
        break

    n = int(input("Enter N : "))
    if n == -1:
        break
    elif n == 0:
        n = 1  # Fallback to 1 




    
#Multiply(5,2)

#5 + Multiply(5,1)
#5 + 1
