a = int(input("Enter your number"))
arr = []
if a % 2 != 0:
    for num in range(1,2*a):
        if num%2 != 0:
            arr.append(str(num))
            join = ','.join(arr)
else:
    for num in range(1,2*(a-1)):
        if num%2 != 0:
            arr.append(str(num))
            join = ','.join(arr)
  
print(join)