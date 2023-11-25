sayı = input("Sayı girin:")

a = len(sayı)

sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam += basamak ** a

    gecici_sayı //= 10

if toplam == sayı:
    print("Armstrong sayısı")
else:
    print("Değil")
