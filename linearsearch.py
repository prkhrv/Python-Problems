n =  int(input("Enter the size"))
a=[]
flag=0
print("Enter the list")
for i in range(0,n):
    b =int(input())
    a.append(b)

key = int(input("Enter Element to be searched"))

for i in a:
    if(i==key):
        print("Element Found ! ")
        flag = 1
        break

if(flag==0):
    print("Element not found")
