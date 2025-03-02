print("Hesap Makinesi" ) 
print("Toplama (+), Cikarma (-), Carpma (*), Bolme (/)")
print("Islem yapmak icin: sayi1 operator sayi2 formatinda giriniz") 
print("örnegin 5+3 formatinda girirniz.")
sayi1 = float(input("İlk sayiyi girin: "))
op = input("operatörü giriniz: ")
sayi2 = float(input("İkinci sayiyi girin: "))

if op == '+':
    print("Sonuc:", sayi1 + sayi2)
elif op == '-':
    print("Sonuc:", sayi1 - sayi2)
elif op == '*':
    print("Sonuc:", sayi1 * sayi2)
elif op == '/':
    if sayi2 != 0:
        print("Sonuc:", sayi1 / sayi2)
    else:
        print("Hata: Sifira bolme yapilamaz!")
else:
    print("Gecersiz operator!")