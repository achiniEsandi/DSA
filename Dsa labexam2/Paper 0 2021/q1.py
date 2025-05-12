#2021 Paper 0

def triangleNum(n):
    if(n == 1):
        return 1;
    else:
        return n + triangleNum(n - 1)


num = int(input("Enter number: "))

while(True):
    
    
