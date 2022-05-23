print("Hello, it is improved solver which can deal with more difficult problems, that first version.")
print("Please, give me the task.")
print("For example: mul(multiplication), sub(substraction), discriminant(solver of quadrtic equation)")
task = input()
if task == "mul":
        a = int(input('Enter first value: '))
        b = int(input('Enter second value: '))
        print("Result: ", a*b)
if task == "sub":
        a = int(input('Enter first value: '))
        b = int(input('Enter second value: '))
        print("Result: ", a+b)
if task == "discriminant":
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = int(input('Enter c: '))
        D = b*b - 4*a*c
        if D < 0:
            print("Discriminant < 0 -> no real roots")
        if D == 0:
            print("X = ", -b/(2*a))
        if D > 0:
            X1 = (-b + D**(1/2))/(2*a)
            X2 = (-b - D**(1/2))/(2*a)
            print("X1 = ", X1, " X2 = ", X2)
print("Thanks for work")
