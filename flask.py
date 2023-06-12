print("İşte Pizza'ya hoşgeldiniz...\n")

boyut = input('Ne boyut bir pizza istiyorsunuz? "S", "M" veya "L"')
ekstra_peynir = input('Fazladan peynir istiyor musunuz? "Evet" veya "Hayır"')
icecek = input ('İçecek alıyor musunuz? "Evet" veya "Hayır"')

hesap = 0

if boyut == "S":
  hesap += 20
elif boyut == "M":
  hesap += 25
else:
  hesap += 30

if ekstra_peynir == "Evet":
  if boyut == "S":
    hesap += 2
  else:
    hesap += 3
    
if icecek == "Evet":
  hesap += 2
  
print(f"Toplam tutarı: {hesap} TL.")