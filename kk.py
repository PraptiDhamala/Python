def check_even_orodd(n):
    if n % 4 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter a number: "))
print(check_even_odd(num))