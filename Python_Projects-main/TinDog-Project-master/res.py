n = int(input().strip())
    
    #List to store the binary format
lst = []
    
    #Convert the number to binary and store in list
while n > 0:
    remainder = n % 2
    n = n//2
    lst.append(n)
print(lst)