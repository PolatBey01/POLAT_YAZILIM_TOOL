import time


print("Merhaba PolatJNR. projesinin tool'una hoşgeldiniz ")
time.sleep(2)
isim = input("isminizi öğrenebilirmiyim = ")
if isim =="Polat Efe Akçay":
     print("""
     HOŞGELDİNİZ POLAT BEY NASILSINIZ İYİSİNİZDİR UMARIM
     TOOL ŞUANDA GELİŞTİRİLİYOR
     EN YAKIN ZAMANDA YAYINLANACAKTIR
     """)
if isim =="DARK":
     print("""
     HOŞGELDİNİZ DARK BEY NASILSINIZ İYİSİNİZDİR UMARIM
     TOOL ŞUANDA GELİŞTİRİLİYOR
     EN YAKIN ZAMANDA YAYINLANACAKTIR
     """)
time.sleep(3)
print("Hoşgeldin " + isim)
time.sleep(2)
print("Bu tool deneme amacı ile yapılmıştır")
time.sleep(2)
print("ilerleyen zamanlarda sık güncelleme alarak geliştirilecektir")
time.sleep(2)
print("diğer toollara bakabilirsin")
time.sleep(2)
print("""
ULAŞABİLİCEĞİNİZ ADRESLER;
1)İNSTAGRAM
2)TWİTTER
3)TELEFON NUMARASI
4)TOPLULUĞUMUZ
""")
a = input("SEÇİM YAPINIZ :")
if a == "1":
     print("@_polat_efe_akc_")
if a == "2":
    print("twitterimiz yoktur")
if a == "3":
     print("+1 (385) 494-3023")
if a == "4":
     print("!!ERROR!!")
