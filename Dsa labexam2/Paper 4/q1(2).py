def power(base, exp):
    if(exp == 0):
        return 1
    else:
        return base * power(base,exp-1)


while(True):
    base = int(input("Enter base: "))   #user input for base
    if(base == -1):
        print("Program ended")
        break
    
    exp = int(input("Enter exp: "))     #user input for exp
    if( base<-1 or exp<-1):
        print("Enter positive numbers")
        continue

    print("Output: ",power(base,exp))
