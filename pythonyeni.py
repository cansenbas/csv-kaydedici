import csv

ad = input("Adınızı Giriniz: ")
soyad = input("Soyadınızı Giriniz: ")
tc = input("TC Kimlik Numaranızı Giriniz: ")
tel = input("Telefon Numaranızı Giriniz: ")
vk = input("Vergi Numaranızı Giriniz: ")

with open('kayit.csv', mode='w') as kayit_dosyasi:
    kayit_yazici = csv.writer(kayit_dosyasi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    kayit_yazici.writerow(['Ad', 'Soyad', 'TC Kimlik No', 'Telefon No', 'Vergi  Linki'])
    kayit_yazici.writerow([ad, soyad, tc, tel, vk])

print("Kayıt başarıyla kaydedildi.")
