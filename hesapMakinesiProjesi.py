
class hesapMakinesi():

    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        sonuc = self.sayi1 + self.sayi2
        return sonuc
    
    def carpma(self):
        sonuc = self.sayi1 * self.sayi2
        return sonuc

    def bolme(self):
        sonuc = self.sayi1 / self.sayi2
        return sonuc

print("1:Toplama 2:Carpma 3:Bolme")
secim = int(input("1,2 ya da 3 seciniz: "))
sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi 2 :"))
h1 = hesapMakinesi(sayi1,sayi2)
if(secim == 1):
    print(h1.toplama())
elif(secim == 2):
    print(h1.carpma())
elif(secim == 3):
    print(h1.bolme())


  


































        

        










