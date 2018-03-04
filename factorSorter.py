maxNum = int(input("Max value: "))
order = str(input("Order [y/n]: "))


factors = []

for num in range(1,maxNum+1):
    a = [x for x in range(1,maxNum+1) if num % x == 0]
    factors.append(a)

if order == "y":
    factors = sorted(factors, key=len)

for array in factors:
    print(array)
