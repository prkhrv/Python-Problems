n = int(input("Enter the size "))
arr = []
freq = []


for i in range(0,n):
    a = int(input())
    arr.append(a)
    b = -1
    freq.append(b)


lenarr = len(arr)

for i in range(0,lenarr):
    value = 1
    for j in range(i+1,lenarr):
        if(arr[i]==arr[j]):
            freq[j] = 0
            value = value+1
    if(freq[i]!=0):
        freq[i] = value

print(arr)

for i in range(0,lenarr):
    if(freq[i]!=0):
        print("Frequency of Element {} is {}".format(arr[i],freq[i]))
