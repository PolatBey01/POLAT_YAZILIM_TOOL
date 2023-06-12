import time

print("""
[P]==========ZEUS=========[-][o][x]
|     ZEUS Kayıt Programına       |
|          Hoşgeldiniz!           |
|           Sürüm 0.8             |
|    Devam Etmek için Lütfen      |
|          Bekleyiniz             |
|             ...                 |
|=================================|
""")
time.sleep(1)
isim = input("Resmi Doğrulama İçin İsim,Soyisim Öğrenebilirmiyim:")
yaş = (input("Yaş (gerçek):")) 
boy = (input("Boy (m):"))
kilo = (input("Kilo (kg):"))
cinsiyet = input("cinsiyet(Erkek/Kız):")


print("""
_____________________________________________
""")
print(isim)
print(int (yaş))
print(float(boy))
print(int(kilo)) 
print(cinsiyet)

print("_____________________________________________")
time.sleep(1)
doğruluk = input("BİLGİLER DOĞRUMU(DOĞRU İSE (e)YANLIŞ İSE (q)): ")

while True:
  if doğruluk == "q":
    break
  
  elif doğruluk == "e":
    print("Yukaridaki Bilgileri Ekran Görüntüsü Alarak Bu Bağlantidaki Whatsapp Hesabimiza Göndererek Kayit Olabilirsiniz")
    print("Bağlanti;")
    print("https://wa.me/13854943023")
    break
  else :
    break