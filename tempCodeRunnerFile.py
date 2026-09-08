n1 = int(input("Enter numerator 1: "))
d1 = int(input("Enter denominator 1: "))

n2 = int(input("Enter numerator 2: "))
d2 = int(input("Enter denominator 2: "))

# Add fractions
numerator = n1 * d2 + n2 * d1
denominator = d1 * d2

# Find GCD
num1 = numerator
num2 = denominator
if num1>num2:
    small=num2
else:
    small=num1
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        hcf=i

# Simplify
numerator = numerator // hcf
denominator = denominator // hcf

print("Numerator =", numerator)
print("Denominator =", denominator)