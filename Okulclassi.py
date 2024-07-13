class Okul:
    def __init__(self,isim,kacYillik):
        self.isim = isim
        self.kacYillik = kacYillik
    
    class Ogrenci():
        def __init__(self,isim,soyad,no,disiplinPuani,ders={"Turkce":0,"Matematik":0}):
            self.isim = isim
            self.soyad = soyad
            self.no = no
            self.disiplinPuani = disiplinPuani 
            self.ders = ders
            

        def disiplinDurumu(self):
            disiplin = input("Disiplin cezasi aldi mi ? (Evet/Hayir)")
            if(disiplin == "Evet"):
                self.disiplinPuani -= 10
                if(self.disiplinPuani <= 0):
                    self.isim = None
                    self.soyad = None
                    self.no = None
                    self.disiplinPuani = None
                else:
                    print(f"Ogrencimizin disiplin puani 10 puan dusmustur.Yeni disiplin puani = {self.disiplinPuani}")
            else:
                print("Ogrenci disiplin cezasi almamistir.")

        def puanDegis(self):
            girdi = input("Lutfen puani degistirmek istediginiz dersi giriniz: (Turkce ya da Matematik)")

            if(girdi == "Turkce"):
                self.ders["Turkce"] = int(input("Lutfen puani giriniz: "))
                if(0<self.ders["Turkce"] <=100):
                    print(f"Basarili bir sekilde puan degisti.Turkce puaniniz={self.ders["Turkce"] }")
                else:
                    print("Puan degisemedi!")
                    self.ders["Turkce"] = 0
            elif(girdi == "Matematik"):
                self.ders["Matematik"] = int(input("Lutfen puani giriniz: "))
                if(0<self.ders["Matematik"] <=100):
                    print(f"Basarili bir sekilde puan degisti.Matematik puaniniz={self.ders["Matematik"] }")
                else:
                    print("Puan degisemedi!")
                    self.ders["Matematik"] = 0
            else:
                print("Boyle bir ders yok")


        def puanGoruntule(self):
            print(f"Turkce notunuz = {self.ders["Turkce"]} Matematik notunuz = {self.ders["Matematik"]}")
        
        def dersOrtalamaGoruntule(self):
            ortalama = (self.ders["Turkce"] + self.ders["Matematik"]) / 2
            print(f"Derslerin ortalamasi = {ortalama}")


o1 = Okul.Ogrenci("Ali","Veli",12345,100)
o1.disiplinDurumu()
o1.puanDegis()
o1.puanDegis()
o1.puanGoruntule()
o1.dersOrtalamaGoruntule()