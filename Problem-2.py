a = int(input("Enter your number"))
arr = []

for num in range(1,2*a):
    if num%2 != 0:
        arr.append(str(num))
        join = ','.join(arr)
        

print(join)