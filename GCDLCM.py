#Write a function to find the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

print(f"GCD of {a} and {b} is: {gcd_result}")
print(f"LCM of {a} and {b} is: {lcm_result}")
