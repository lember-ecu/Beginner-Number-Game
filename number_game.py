import random

def tahmin(a,b):
    number = random.randint(a, b)
    tahmin = 0
    while tahmin != number:
        tahmin = int(input(f"Bir sayı tahmin edin ({a}-{b}): "))
        if tahmin < number:
            print("Daha yüksek bir tahmin yapın")
        elif tahmin > number:
            print("Daha düşük bir tahmin yapın")
    print(f"Tahmininiz doğru {number}")

a = int(input("Başlangıç sayısı: "))
b = int(input("Bitiş sayısı: "))
tahmin(a,b)
