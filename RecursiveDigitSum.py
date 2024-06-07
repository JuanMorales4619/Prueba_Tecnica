def superDigit(n,k):
    def super_digit_recursive(x):
        if len(x) == 1:
            return int(x)
        return super_digit_recursive(str(sum(int(digit) for digit in x)))
    
    initial_sum = sum(int(digit) for digit in n) * k     
    return super_digit_recursive(str(initial_sum))
print(superDigit("123",3))