import time
print("""
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            ) 
              ^^\..___,.--`     POLAT YAZILIM TOOL'UNA HOŞ GELDİNİZ
""")
plt_kullanıcı_adı = "Polat Efe Akçay"
plt_şifre = "pltyazılımtool"

kullanıcı_adı = input("Kullanıcı Adı:")
şifre = input("Şifre:")



if (kullanıcı_adı == plt_kullanıcı_adı and plt_şifre != şifre):
    print ("şifren yanlış knkm")

elif (kullanıcı_adı != plt_kullanıcı_adı and şifre == plt_şifre):
    print("böyle bir kullanıcı adı yok")    

elif (kullanıcı_adı != plt_kullanıcı_adı and şifre != plt_şifre):
    print("bu bilgiler yanlış")


else :
    yaş = int(input("yaşınızı öğrenebilirmiyim: "))

if yaş <18:
    print("toola giremezsin")

else:
    print("HOŞGELDİNİZ")
    time.sleep(1)
    print("POLAT YAZILIM TOOLUNUN ANA BİLGİ MERKEZİNE HOŞGELDİNİZ")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("""
    YAPIMCI: POLAT EFE AKÇAY
    SÜRÜM: 1.1
    DEVAMI YAKINDA GELECEK
    ...
    ERROR
    """)
