import math

cat_a = int(input("Введите катет a:"))
cat_b = int(input("Введите катет b:"))

s = 0.5 * cat_a * cat_b
hypotenuse = round(math.sqrt(cat_a**2 + cat_b**2), 2)

print("Площадь трегольника = ", s, "\nГипотенуза = ", hypotenuse)
