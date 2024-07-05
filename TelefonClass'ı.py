class Telefon:

    def __init__(self,marka,model,isletimSistemi,onTanimliProgramlar,hafiza):
        self.marka = marka
        self.model = model
        self.isletimSistemi = isletimSistemi
        self.onTanimliProgramlar = onTanimliProgramlar
        self.hafiza = hafiza

    def bilgileriGoster(self):
        print(self.marka,self.model,self.isletimSistemi,self.onTanimliProgramlar,self.hafiza)

    def onTanimliProgramlariGoster(self):
        print(self.onTanimliProgramlar)
        

    def onTanimliProgramEkle(self,program):
        self.onTanimliProgramlar.append(program)
        print("Bir program eklendi.")

    def onTanimliProgramSil(self,program):
        self.onTanimliProgramlar.remove(program)
        print("Bir program silindi.")

    def onTanimliProgramGuncelle(self,program,newInfo):
        self.onTanimliProgramlar[self.onTanimliProgramlar.index(program)] = newInfo
        print("Bir program guncellendi.")
    def hafizaArttir(self,ekHafiza):
        self.hafiza += ekHafiza
        print("Hafiza arttirildi.")
        print(self.hafiza)
    def aramaYap(self,numara):
        print(f"{numara} numarasi araniyor.")
    def mesajGonder(self,numara,mesaj):
        print(f"{numara} numarasina mesaj gönderildi : {mesaj}")

telefon1 = Telefon("Samsung","Note 10" ,"Android",["Rehber","Galeri","Kamera"],64)
telefon1.bilgileriGoster()
telefon1.onTanimliProgramlariGoster()
telefon1.onTanimliProgramEkle("Navigasyon")
telefon1.onTanimliProgramlariGoster()
telefon1.onTanimliProgramGuncelle("Rehber","Kisiler")
telefon1.onTanimliProgramlariGoster()
telefon1.onTanimliProgramSil("Galeri")
telefon1.onTanimliProgramlariGoster()
telefon1.hafizaArttir(100)
telefon1.bilgileriGoster()

telefon1.aramaYap(555555)
telefon1.mesajGonder(11111,"Merhaba Dunya!")
