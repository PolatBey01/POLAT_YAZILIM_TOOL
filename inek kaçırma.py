from tkinter import *
import random
import time
from PIL import ImageTk


class Ufo:
    def __init__(self, Inek, UfoResim, canvas):
        self.canvas = canvas
        self.Ineks = Inek
        self.UfoResim = UfoResim
        self.skor = 0
        self.hiz = 0

        
        self.idUFO = canvas.create_image(50, 100, image=UfoResim)  

        
        self.textSkor = self.canvas.create_text(610, 30, text="Skor : 0", font=("Arial", 16), fill="red")
        self.textHiz = self.canvas.create_text(510, 30, text="Hız : 0", font=("Arial", 16), fill="blue")

        self.x = 0 
        self.y = 0  

        
        self.canvas.bind_all('<KeyPress-Left>',
                             self.hareket_sag)  
        self.canvas.bind_all('<KeyPress-Right>',
                             self.hareket_sol)  
        self.canvas.bind_all('<KeyPress-Up>',
                             self.hareket_ust)  
        self.canvas.bind_all('<KeyPress-Down>',
                             self.hareket_alt)  

    
    def Ciz(self):
        self.canvas.move(self.idUFO, self.x,
                         self.y) 
        Koordinat = self.canvas.coords(self.idUFO)  
        
        if Koordinat[0] < 10:  
            self.Kaybettin()  
        if Koordinat[0] > 670:  
            self.Kaybettin()  
        if Koordinat[1] < 10:  
            self.Kaybettin()  
        if Koordinat[1] > 364:  
            self.Kaybettin()  
            
        if self.InekKacir(Koordinat) == True:
            self.skor = self.skor + 1  
            startsX = float(
                random.randint(50, 620))  
            startsY = float(
                random.randint(50, 320))  
            self.canvas.coords(self.Ineks.idInek, startsX, startsY)  
            self.hiz = self.hiz + 1  
            self.canvas.itemconfig(self.textSkor, text="Skor : %s" % self.skor) 
            self.canvas.itemconfig(self.textHiz, text="Hız : %s" % self.hiz)  

    
    def hareket_sag(self, event):
        self.x = -1 - (self.hiz / 100)
        self.y = 0

    def hareket_sol(self, event):
        self.x = 1 + (self.hiz / 100)
        self.y = 0

    def hareket_ust(self, event):
        self.x = 0
        self.y = -1 - (self.hiz / 100)

    def hareket_alt(self, event):
        self.x = 0
        self.y = 1 + (self.hiz / 100)

    
    def InekKacir(self, pos):
        InekKoordinat = self.canvas.coords(self.Ineks.idInek)
        if pos[0] >= InekKoordinat[0] and pos[0] <= InekKoordinat[0] + 50:
            if pos[1] >= InekKoordinat[1] and pos[1] <= InekKoordinat[1] + 50:
                return True

        return False

    
    def Kaybettin(self):
        self.x = 0  
        self.y = 0
        self.canvas.coords(self.idUFO, 700, 700)  
        self.textid = self.canvas.create_text(350, 150, text="Kaybettin", font=("Arial", 25),
                                              fill="red")  


class Inek:
    def __init__(self, canvas, InekResim):
        self.canvas = canvas
        self.idInek = canvas.create_image(10, 10, image=InekResim)  
        self.canvas.move(self.idInek, 150, 20)

    def Ciz(self):
        self.canvas.move(self.idInek, 0, 0)


tk = Tk()
tk.title('Inek Kacirma Oyunu')  # Oyun basligimiz
canvas = Canvas(tk, width=679, height=374, bd=0,
                highlightthickness=0)  

UFO = PhotoImage(file='')  
INEK = PhotoImage(file='')  
ArkaPlan = ImageTk.PhotoImage(file="MainBackground.png") 
canvas.create_image(0, 0, image=ArkaPlan, anchor=NW)  # Ekranimizin arkaplanini belirliyoruz :)
canvas.pack()
tk.update()

Inek = Inek(canvas, INEK)  # Inek Nesnemize Gerekli Parametreleri Yolluyoruz. Veeee :)
Ufo = Ufo(Inek, UFO, canvas)  # Ufo Nesnemize Gerekli Parametreleri Yolluyoruz. AND THE GAME İS READY :) 

while 1:
    Inek.Ciz()
    Ufo.Ciz()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)