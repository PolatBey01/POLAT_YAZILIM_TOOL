print("DÜNYADAN OBEZLERİ TEMİZLEME DERNEĞİ ?")
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
yaş = int(input("Yaş (gerçek):")) 
cinsiyet = input("cinsiyet(E/K):")
isim = input("Resmi Doğrulama İçin İsim,Soyisim Öğrenebilirmiyim")


 
endeks  = kilo/(boy*boy)
if endeks <18:
    print("\n olm sen ne zayıfsın aq zarganası:{}".format(endeks))
elif endeks >= 18 and endeks <25 :
    print("\n olm normalsin lan:{}".format(endeks))
elif endeks >= 25 and endeks <30:
    print("\n Knkm kilona dikkat et ama iyisin:{}".format(endeks))
elif endeks >= 30 and endeks <35:
    print("\n Yediklerini çıkar bence ayı değilsin lazım olmaz sana:{}".format(endeks))
else:
    print("\n Lan Siktir Git Uygulamadan Obez Orospu Evladı:{}".format(endeks))
 