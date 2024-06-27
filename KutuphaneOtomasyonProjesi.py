
class Kitap():

    def __init__(self,isim,yazar,kategori,sayfaSayisi):
        print("init fonksiyonu calisiyor...")
        self.isim = isim
        self.yazar = yazar
        self.kategori = kategori
        self.sayfaSayisi = sayfaSayisi
    def bilgileriGoster(self):
        print("Bilgiler gosteriliyor...")
        print(f"Isim = {self.isim} \n Yazar = {self.yazar} \n Kategori = {self.kategori} \n Sayfa Sayisi = {self.sayfaSayisi}\n ")
class OduncDurumu():
    def __init__(self,kitap):
        self.kitap = kitap
        self.kiralandi = False
    def kiralanmaDurumu(self):
        if (self.kiralandi):
            print(f"{self.kitap.isim} zaten kiralanmistir.")
        else:
            print(f"{self.kitap.isim} kiralanmamistir.")
    def kirala(self):
        if(self.kiralandi):
            print(f"Kitap {self.kitap.isim} zaten kiralanmistir.")
        else:
            self.kiralandi = True
            print(f"Kitap {self.kitap.isim} basariyla kiralanmistir.")

    def geriAl(self):
        if not self.kiralandi:
            print(f"Kitap {self.kitap.isim} zaten kutuphanede.")
        else:
            self.kiralandi = False
            print(f"Kitap '{self.kitap.isim}' başariyla geri alindi.")
    def bilgileriGoster(self):
        print("Bilgiler gosteriliyor....")
        self.kitap.bilgileriGoster()
        if(self.kiralandi):
            kiralanmaDurumu = "Evet"
        else:
           kiralanmaDurumu = "Hayir"
        print(f"Kiralanmis mi ? {kiralanmaDurumu}")



kitap1 = Kitap("Simyaci", "Paulo Coelho", "Roman", 184)
kitap2 = Kitap("Python ile Programlama", "Ahmet Yilmaz", "Programlama", 350)


odunc = OduncDurumu(kitap1)
odunc.bilgileriGoster()

odunc.kirala()
odunc.geriAl()
odunc.geriAl()  #Kutuphanede olan kitabi geri alma denemesi.

odunc.bilgileriGoster()







    
        

