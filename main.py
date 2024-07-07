import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input("kaç karakterli bir şifre istiyorsun?"))

sifre = ""

for i in range(count):
    sifre += random.choice(karakterler)

print(sifre)