def Fibonacci(n):
    if n<1 : 
        return n
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)


def main ():
    while True:
        try:
            num = int(input("Enter a non negative integer. press -1 to quit"))
        if num == -1 :
            print("Program terminated ")
            break
        elif num <-1 :
            print("Enter a positive number")

        else :
            result = Fibonacci(num)
            print(f"Fibonacci({num}) = {result}")



        
        


        



