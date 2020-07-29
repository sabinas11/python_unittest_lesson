def gcd(number1, number2):
    while True:
        big = max(number2, number1)
        small = min(number2, number1)
        remainder = big % small
        if remainder == 0:
            return small
        else:
            number1 = remainder
            number2 = small