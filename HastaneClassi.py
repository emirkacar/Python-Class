


class Doktor:
    def __init__(self,isim,soyad,maas,izinHakki):
        self.isim = isim
        self.soyad = soyad
        self.maas = maas
        self.izinHakki = izinHakki
    
    def maasGuncelle(self,artisMiktari):
        self.maas += artisMiktari
    
    def bilgileriGoster(self):
        print(f"{self.isim} {self.soyad} {self.maas} {self.izinHakki}",end=" ")
        
class Uzman(Doktor):

    def __init__(self, isim, soyad, maas,departman,arabaBilgisi):
        super().__init__(isim, soyad, maas,30)
        self.departman = departman
        self.arabaBilgisi = arabaBilgisi
        self.nobet = 0
    
    def arabaDegistir(self,araba):
        print("Araba degistirildi.")
        self.arabaBilgisi = araba
    
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(f"{self.departman} {self.arabaBilgisi}")

class Pratisyen(Doktor):
    def __init__(self, isim, soyad, maas,nobetGunleri):
        super().__init__(isim, soyad, maas,20)
        self.nobetGunleri = nobetGunleri

    def bilgileriGoster(self):
        super().bilgileriGoster()
        print(f"{self.nobetGunleri}")

    def nobetGunleriniGuncelle(self,gunler):
        self.nobetGunleri = gunler

u1=Uzman("Emir","Kacar",50000,"KBB","Renault")
p1=Pratisyen("Ali","Veli",10000,["Sali","Persembe"])

u1.bilgileriGoster()
p1.bilgileriGoster()
u1.arabaDegistir("Toyota")
u1.bilgileriGoster()
liste = ["Pazartesi","Carsamba"]
p1.nobetGunleriniGuncelle(liste)
p1.bilgileriGoster()
print()
u1.maasGuncelle(8000)
u1.bilgileriGoster()
print()
p1.maasGuncelle(2000)
p1.bilgileriGoster()