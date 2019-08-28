n=int(input("Enter the height of pyramid"))
c=n
j=1
for i in range(1,n+1):
    for i in range(1,c,1):
        print(" ",end=" ")
    for i in range(1,j+1,1):
        print(" * ",end=" ")
    c=c-1
    j=j+1
    print("\n")
        
