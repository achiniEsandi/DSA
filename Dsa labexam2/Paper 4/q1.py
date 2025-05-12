def power(base, exp):
    if(exp == 0):
        return 1
    else:
        return base * power(base, exp-1)
    


while(True):
    x = int(input("Enter base: "))
    if (x == -1):
        break
    
    n = int(input("Enter exp: "))
    while(n<0):
        print("Negative numbers cannot be entered")
        n = int(input("Enter exp: "))

    print("Output: ", power(x,n))
        
