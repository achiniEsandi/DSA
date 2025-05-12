print("Hello World")

def Multiply(M, n):
    if n == 1:
        return M
    else:
        return M + Multiply(M, n - 1)

while True:
    M = int(input("Enter the first number or enter -1 to quit: "))
    if M == -1:
        print("Program ended")
        break
    n = int(input("Enter second Number: "))
    if n < 1:
        print("Number should be greater than 0")
        continue

    result = Multiply(M, n)
    print(f"{M} * {n} = {result}")
