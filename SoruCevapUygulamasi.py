
import random

class Soru:
    def __init__(self,soruMetni,secenekler,dogruCevap):
        self.soruMetni=soruMetni
        self.secenekler=secenekler
        self.dogruCevap=dogruCevap

    def soruSor(self):
        print(f"{self.soruMetni}") 
        for i,secenek in enumerate(self.secenekler):
            print(f"{i}. {secenek}")
    
    def cevapKontrol(self,cevap):
        if(cevap==self.dogruCevap):
            print("Dogru cevap verdiniz,tebrikler.")
            return True
        else:
            print("Yanlis cevap verdiniz.")  
            return False      

class Quiz:
    def __init__(self):
        self.sorular=[]

    def soruEkle(self,soru):
        self.sorular.append(soru)
    
    def quizBaslat(self):
        random.shuffle(self.sorular)
        print("Quiz baslamistir.")
        return self.sorular
    
    def sonuclariGoster(self,puan,toplam):
        print(f"\nQuiz bitti! Skorunuz: {puan}/{toplam}")
        basariYuzdesi = (puan / toplam) * 100
        print(f"Basari yuzdesi: {basariYuzdesi}%") 
        

class Ogrenci:
    def __init__(self,ad):
        self.ad=ad 
        self.puan=0
    
    def cevapVer(self):
        cevap=input("Cevap veriniz(1-4): ")
        return int(cevap)
    
    def puanEkle(self):
        self.puan += 1

class QuizUygulamasi:
    def __init__(self):
        self.quiz=Quiz()
        self.oyuncu=None
        
        
    
    def quizOlustur(self):
        q1 = Soru("Türkiye'nin baskenti neresidir?", ["İstanbul", "Ankara", "İzmir", "Bursa"], 2)
        q2 = Soru("5+5=?", ["8", "9", "7", "10"], 4)
        q3 = Soru("Bir yilda kaç ay vardir?", ["10", "11", "12", "13"], 3)

        self.quiz.soruEkle(q1)
        self.quiz.soruEkle(q2)
        self.quiz.soruEkle(q3)

    def oyunuBaslat(self):
        print("OYUNA HOSGELDINIZ")
        kullaniciIsmi=input("Kullanici adiniz: ")
        self.oyuncu =Ogrenci(kullaniciIsmi)

        sorular=self.quiz.quizBaslat()
        for soru in sorular:
            soru.soruSor()
            kullanicininCevabi=int(self.oyuncu.cevapVer())
            if soru.cevapKontrol(kullanicininCevabi):  # cevapKontrol metodunu kullanın
                self.oyuncu.puanEkle()
           
        
        self.quiz.sonuclariGoster(self.oyuncu.puan,len(sorular))
            


uygulama=QuizUygulamasi()
uygulama.quizOlustur()
uygulama.oyunuBaslat()

            