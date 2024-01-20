import random
ps = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ps2 = ps.upper()
ps = ps + ps2
try:
    length = int(input("Введите длину пароля: "))

except:
    length = int(input("Введите число!: "))
password = ''
for i in range(length):
    password = password + random.choice(ps)
print("Ваш пароль:",password)