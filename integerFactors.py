def divisors(maxNum):

    for i in range(1, maxNum + 1):
        factors = [x for x in range(1, maxNum + 1) if maxNum % x == 0]

    i = 2
    primeFactors = []
    for num in range(1, maxNum + 1):
        if maxNum % i != 0:
            i = i + 1
        if maxNum % i == 0:
            primeFactors.append(i)
            maxNum = maxNum/i

    #primeFactors = " x ".join(str(x) for x in primeFactors)
    # Used to replace list with expanded form
    print("n(f) :", factors)
    print("n(p) :", primeFactors)

number = int(input("Number to be factored: "))

divisors(number)
