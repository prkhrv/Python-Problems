a = int(input())

b = int(a/2)
c = b+1
for i in range(a):
    for j in range(a):
        if(i==0 or i==a-1):
             print("*",end=' ')
        elif(j==a-1):
            print("*",end=' ')
        elif(i>=2 and j==0):
            print("*",end=' ')
        elif(i==2 and j<a-2):
            print("*",end=' ')
        elif((i>1 and i<=a-3) and j==a-3):
            print("*",end=' ')
        elif(i==a-3 and (j!=1 and j<=a-3)):
            print("*",end=' ')
        elif((i>=a-6 and i<=a-3)and (j==2 and i!=1)):
            print("*",end=' ')
        elif((j!=1 and j<=a-5) and i==a-6 ):
            print("*",end=' ')
        elif(i==b and j==b):
            print("*",end=' ')
        elif(i==1 and j!=a-1):
            print(" ",end=' ')
        else:
            print(" ",end=' ')




    print("\r")
