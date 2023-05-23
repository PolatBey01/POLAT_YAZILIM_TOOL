import time
print("HOŞGELDİNİZ BEN ZEUS SİZİ TANIMAK İSTERİM")
time.sleep(1)
isim = input("Resmi Doğrulama İçin İsim,Soyisim Öğrenebilirmiyim:")
yaş = int(input("Yaş (gerçek):")) 
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
cinsiyet = input("cinsiyet(E/K):")


print("""
_____________________________________________
""")
print(isim)
print(yaş)
print(boy)
print(kilo) 
if cinsiyet == "e" :
    print("erkek")
elif cinsiyet == "k" :
    print("kız")

print("_____________________________________________")
 

 
