def factorial(n):
    fact=1
    while n>=1:
        fact=fact*n
        n=n-1
    print("Factorial of 5 is: ",fact)
factorial(int(input("Enter a number: ")))