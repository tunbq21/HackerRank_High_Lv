

def said_hello(name: str, age:int) -> str:
    return f"Hello {name}, you are {age} years old!"


print(said_hello("Alice", 30))

# ==========================================================================
import math

def v_circle (radius: float) -> float:
    pi = math.pi
    return pi * radius ** 2

result = v_circle(5)
print(result.__floor__())
print(f"The area of the circle with radius 5 is: {result:.1f}")


# =========================================================================

a = 10
b = 20 

a = a + b
b = a - b
a = a - b

print ( f"After swapping: a = {a}, b = {b}")

x = 5
y = 10

x,y = y,x

print ( f"After swapping: x = {x}, y = {y}")

# ==========================================================================


def check_point(num: float) -> str:
    if num >= 8: return "Grood"
    if num >= 6.5: return "Not bad"
    if num >= 5: return "Bad"
    return "Very bad"

print(check_point(8.5))
print(check_point(7))
print(check_point(6))
print(check_point(4.5))


# =========================================================================


def kiem_tra_nam_nhuan(nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return f"Năm {nam} là năm nhuận (366 ngày)."
    else:
        return f"Năm {nam} là năm thường (365 ngày)."

# nam_nhap = int(input("Nhập năm bạn muốn kiểm tra: "))
# print(kiem_tra_nam_nhuan(nam_nhap))

# =========================================================================

def bang_cuu_chuong(n : int) -> list:
    return [n *i  for i in range(0, 11)]

print(bang_cuu_chuong(5))

# =========================================================================

def tinh_giai_thua_cua_n(n : int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(tinh_giai_thua_cua_n(4))



# =========================================================================

def kiem_tra_so_nguyen_to(n : int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(kiem_tra_so_nguyen_to(11))
print(kiem_tra_so_nguyen_to(15))

# =========================================================================
