def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

number = int(raw_input("Factorial of what number? "))
print(factorial(number))
