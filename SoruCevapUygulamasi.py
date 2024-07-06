class Soru:
    def __init__(self, metin, secimler, cevap):
        self.metin = metin
        self.secimler = secimler
        self.cevap = cevap
        self.skor = 0
        self.index = 0

    def soruyuAl(self):
        print(self.metin)
        

    def secenekleriGoster(self):
        for secenek in self.secimler:
            print("-", secenek)

    def tahminEt(self):
        tahmin = input("Cevap: ")
        if tahmin == self.cevap:
            print("Doğru bildiniz, tebrikler.")
            self.skor += 1
        else:
            print("Yanlis cevap.")
        self.index += 1

    def skoruGoster(self):
        print("Skorunuz =", self.skor)

    def oyunBittiMi(self,toplamSoruSayisi):
        
        if self.index >= toplamSoruSayisi:
            print("Oyun bitmiştir.")


# Soru nesnesi oluşturma
s1 = Soru("En iyi programlama dili hangisi ?", ["C#", "Python", "Javascript", "Java"], "Python")

# Soruyu gosterme ve secenekleri gosterme
s1.soruyuAl()
s1.secenekleriGoster()  # Bu satirda seçeneklerin dogru sekilde gorunmesi saglaniyor.
s1.tahminEt()
s1.skoruGoster()
s1.oyunBittiMi(1)