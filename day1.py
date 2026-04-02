print("Day 1 - Numerical Operations ")
print(5 + 3)    # Addition        → 8
print(5 - 3)    # Subtraction     → 2
print(5 * 3)    # Multiplication  → 15
print(5 / 3)    # Division        → 1.6666...
print(5 // 3)   # Floor Division  → 1 (removes decimal)
print(5 % 3)    # Modulus         → 2 (remainder only)
print(5 ** 3)   # Exponent        → 125 (5 to the power of 3)
x = 10        # Integer (whole numbers)
y = 3.14      # Float (decimal numbers)
z = 2 + 3j    # Complex number (rare, used in advanced math)

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>
print(0b1010)   # Binary (base 2)       → 10
print(0o12)     # Octal (base 8)        → 10
print(0xFF)     # Hexadecimal (base 16) → 255
print(5 == 3)   # Equal to              → False
print(5 != 3)   # Not equal to          → True
print(5 > 3)    # Greater than          → True
print(5 < 3)    # Less than             → False
print(5 >= 5)   # Greater or equal to   → True
print(5 <= 3)   # Less or equal to      → False
x = 10
x += 5    # same as x = x + 5  → 15
x -= 3    # same as x = x - 3  → 12
x *= 2    # same as x = x * 2  → 24
x /= 4    # same as x = x / 4  → 6.0
x //= 2   # same as x = x // 2 → 3.0
x %= 2    # same as x = x % 2  → 1.0
x **= 3   # same as x = x ** 3 → 1.0
print(x)
print(round(3.7))       # 4     - rounds to nearest whole number
print(abs(-10))         # 10    - removes negative sign
print(max(5, 10, 3))    # 10    - largest number
print(min(5, 10, 3))    # 3     - smallest number
print(sum([1,2,3,4]))   # 10    - adds up a list
print(pow(2, 8))        # 256   - same as 2 ** 8
print(int(3.9))         # 3     - converts to integer
print(float(5))         # 5.0   - converts to float
import math

print(math.sqrt(25))        # 5.0       - square root
print(math.pi)              # 3.14159   - value of pi
print(math.e)               # 2.71828   - value of e
print(math.ceil(3.2))       # 4         - rounds UP always
print(math.floor(3.9))      # 3         - rounds DOWN always
print(math.factorial(5))    # 120       - 5 x 4 x 3 x 2 x 1
print(math.log(100, 10))    # 2.0       - logarithm
print(math.sin(90))         # sine of 90
print(math.cos(0))          # cosine of 0
print(math.tan(45))         # tangent of 45
print(2 + 3 * 4)        # 14  (multiplication first)
print((2 + 3) * 4)      # 20  (brackets first)
print(2 ** 3 + 1)       # 9   (exponent first)
print(10 / 2 + 3)       # 8.0 (division first)
print((5+2)*2)