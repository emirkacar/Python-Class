
class Araba:

    def __init__(self, marka, model, yil, renk,bakim=True):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk
        self.hiz = 0
        self.bakim = bakim
    
    def araba_bilgileri(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yil: {self.yil}, Renk: {self.renk}, Hiz: {self.hiz} km/h"

    def hizlan(self,artisMiktari):
        self.hiz += artisMiktari
        return (f"Araba {artisMiktari} km/h kadar hizlandi.Mevcut hiz : {self.hiz}")

    def yavasla(self,azalisMiktari):

        if(self.hiz - azalisMiktari < 0):
            self.hiz = 0
        else:
            self.hiz -= azalisMiktari
        
        return (f"Araba {azalisMiktari} km/h kadar yavaşladi. Mevcut hiz: {self.hiz} km/h")
    def bakimDurumunuGoster(self):
        if(self.bakim==True):
            print("Bakimi yapilmistir")
        else:
            print("Bakimi yapilmamistir.")
        

araba1 = Araba("Toyota", "Corolla", 2024, "Kirmizi",True)
print(araba1.hizlan(50))
print(araba1.yavasla(10))
print(araba1.araba_bilgileri())
print(araba1.bakimDurumunuGoster())








    
 








    






































