num=int(input("Enter the height of triangle"))
c=num
for i in range(1,num+1):
    while(c!=0):
        for j in range(1,c+1):
            print("*",end=" ")
        print("\n")
        c=c-1
    print()
            
