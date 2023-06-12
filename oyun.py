import time
print("|========================================|")
time.sleep(1)
print("|Polat Yazılım Oyun Merkezine Hoşgeldiniz|")
time.sleep(1)
print(" Yeni ZAZ sistemimiz devrede")
time.sleep(1)
print("      ASE")
time.sleep(1)
print("      HTU")
time.sleep(1)
print("      ARS")
time.sleep(1)
print("      RA ")
time.sleep(1)
print("      İ  ")
giriş = """
(1) ZAZ hakkında bilgi al
(2) taş kağıt makas
(3) sayı 
(4) adam infaz
"""
print(giriş)

while True:
    soru = input("yapmak istediğiniz işlemi yazınız(çıkmak için (imdat)yazınız:)")

    if soru == "imdat":
        print("def ediliyorsunuz")
        break

    elif soru == "4":
        import ADAM_İNFAZ_OYUNU
    
    elif soru == "3":
        import sayı_oyunu
        
    elif soru == "2":
        import taş_kağıt_makas

    elif soru == "1":
        import ZeusTanımaSistemi   

    else:
        print("yanlış işlem yapıldı")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)