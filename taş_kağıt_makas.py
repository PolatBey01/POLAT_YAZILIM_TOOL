import random

tas = '''taş:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagıt = '''kağıt:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''makas:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

oyun_resimleri = [tas, kagıt, makas]

insan_secimi = int(input('''Taş, kağıt, makas? "Taş" seçmek için "0", "kağıt" seçmek için "1" ve "makas" seçmek için "2" rakamına basın...\n'''))

if (insan_secimi > 2 or insan_secimi < 0):
  print("Geçersiz değer girdiniz...") 
else:
  print("Seçiminiz...")
  print(oyun_resimleri[insan_secimi])
  
  bilgisayar_secimi = random.randint(0, 2)
  print("ZAZ seçiyor...")
  print(oyun_resimleri[bilgisayar_secimi])
  
  
  if insan_secimi == 0 and bilgisayar_secimi == 2:
    print("Kazandınız!")
  elif bilgisayar_secimi == 0 and insan_secimi == 2:
    print("Kaybettiniz!")
  elif bilgisayar_secimi > insan_secimi:
    print("Kaybettiniz")
  elif insan_secimi > bilgisayar_secimi:
    print("Kazandınız!")
  elif bilgisayar_secimi == insan_secimi:
    print("Berabere kaldınız!")