print("Enter elements of array separated by spaces")
lst = [int(x) for x in input().split()]
count =0
dict = {}
for i in range(1,10):
    for j in range(len(lst)):
        
        if lst[j]%i == 0:
            count +=1
        if len(lst)-1 == j:
            dict[i] = count
            count = 0
print(dict)