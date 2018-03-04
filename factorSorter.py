def factorSorter(maxNum, order):

    factors = []

    for i in range(1,maxNum+1):
        a = [x for x in range(1,maxNum+1) if i % x == 0]
        factors.append(a)

    if order == "y":
        factors = sorted(factors, key=len)

    for array in factors:
        print(array)

maxVal = int(input("Max value: "))
orderVal = str(input("Order [y/n]: "))

factorSorter(maxVal, orderVal)
