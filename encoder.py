import base64
key = 0 
while key == 0: 
     print(""" 
 <0><1><0><1><0><1><0><1><0><1><0><1><0> 
 <><><><><>DECODER B64 ENDCOER<><><><><><> 
 <0><1><0><1><0><1><0><1><0><1><0><1><0> 
 Şifrelemek için   - 1 
 Şifre çözmek için - 2 
 çıkış             - 0 
 """) 
     secim = int(input("İşlem numarası seçiniz :")) 
     if secim == 0: 
         break 
     elif secim == 1: 
         text1 = input("Lütfen şifrelenecek metini girin :") 
         text1Bytes = text1.encode("ascii") 
         base64Bytes = base64.b64encode(text1Bytes) 
         base64Strings = base64Bytes.decode("ascii") 
         print("Şifreli metin : ",base64Strings) 
         devam = input("Devam etmek için entere basın...") 
     elif secim == 2: 
         text1 = input("Lütfen çözülecek metni girin :") 
         base64Bytes = text1.encode("ascii") 
         text1Bytes = base64.b64decode(base64Bytes) 
         text1Strings = text1Bytes.decode("ascii") 
         print("Şifresi çözülen metin :", text1Strings) 
         devam = input("Devam etmek için entere basın...")