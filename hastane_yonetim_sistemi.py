# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 14:23:13 2025

@author: Emir Kaçar
"""

class Hastane:
    def __init__(self):
        self.hastaneler = {}
        self.hastalar = {}
        self.hasta_ve_bulundugu_hastane={}
    
    def hastane_bilgileri_ekle(self,hastane_adi,sehir,toplam_yatak_kapasitesi,gunluk_kalma_ucreti,puan):
        hastane_adi = str(hastane_adi).upper().strip()
        kontrol = 1
        for hastane in list(self.hastaneler.values()):
            if(hastane==hastane_adi):
                print("Hastane önceden eklenmistir.Tekrar ekleyemezsiniz.")
                kontrol = 0
                break
        if(kontrol==1):
            self.hastaneler[hastane_adi] = [sehir,toplam_yatak_kapasitesi,gunluk_kalma_ucreti,puan]
            print(f"{hastane_adi} yönetim sistemimize eklenmistir.")
        
    def hasta_bilgierini_bastir(self):
        print(f"{self.hastalar}")
    
    def gunluk_kalma_ucretine_gore_hesapla(self,kac_gun,hangi_hastane):
        bulundu = False
        for hastane,bilgi in self.hastaneler.items():
            if(hangi_hastane==hastane):
                total = kac_gun * bilgi[2]
                bulundu = True
                break
        if not bulundu:
            print(f"{hangi_hastane} hastanesi sistemimizde bulunmamaktadır.")
        else:
            print(f"Toplam ucretiniz: {total}")
                
        
    
    def yatak_seviyesine_gore_sirala(self):
        hastane_yatak_sayilari = []
        for k,v in self.hastaneler.items():
            hastane_yatak_sayilari.append((k,v[1]))
        uzunluk = len(hastane_yatak_sayilari)
        for i in range(uzunluk):
            for j in range(uzunluk-1-i):
                if hastane_yatak_sayilari[j][1] > hastane_yatak_sayilari[j+1][1]:
                    hastane_yatak_sayilari[j], hastane_yatak_sayilari[j + 1] = hastane_yatak_sayilari[j + 1], hastane_yatak_sayilari[j]
        for i,(hastane,sayi) in enumerate(hastane_yatak_sayilari,1):
            print(i,(hastane,sayi))
            
            
            
    
    def adina_gore_sirala(self):
        sorted(self.hastaneler)
        for k,v in self.hastaneler.items():
            print(k,v)  
    
    def puanina_gore_sirala(self):
        puanina_gore = []
        for k,v in self.hastaneler.items():
            puan = v[3]
            puanina_gore.append((puan,k))
        puanina_gore.sort()
        if not puanina_gore:
            print("Liste boş")
        else:
            for hastane_adi,puan in puanina_gore:
                print(hastane_adi,puan)
    
    def girilen_sehirdeki_hastaneleri_bastir(self,sehir):
        
        sehir=str(sehir).upper().strip()
        bulundu = False
        for k,v in self.hastaneler.items():
            if(sehir==v[0]):
                print(f"Hastane Adı: {k}")
                print(f"Şehir: {v[0]}")
                print(f"Yatak Kapasitesi: {v[1]}")
                print(f"Günlük Ücret: {v[2]}")
                print(f"Puan: {v[-1]}")
                print("-" * 30)
                bulundu = True
        if( not bulundu):
            print("Girdiğiniz şehirde hastane bulunamadı.")
                    
    def hasta_bilgileri_ekle(self,hasta_adi_soyadi,yas,ID,hangi_hastane):
        hasta_adi_soyadi = str(hasta_adi_soyadi).upper().strip()
        hangi_hastane = str(hangi_hastane).upper().strip()
        
        for hasta in list(self.hastalar.values()):
            if(hasta==hasta_adi_soyadi):
                print("Hasta eklenmiyor cunku hasta hastanemizde.")
        else:
            self.hastalar[hasta_adi_soyadi] = [yas,ID,hangi_hastane]
            self.hasta_ve_bulundugu_hastane[hasta_adi_soyadi] = hangi_hastane
            print(f"{hasta_adi_soyadi} sisteme eklenmiştir.")
            
    def hastane_bilgilerini_bastir(self):
        sirali_anahtarlar = sorted(self.hastaneler.keys())
        sayac = 1
        for isim in sirali_anahtarlar:
            bilgiler = self.hastaneler[isim]
            print(f"{sayac}. HASTANE = {isim}")
            print(f"BULUNDUGU SEHIR = {bilgiler[0]}")
            print(f"YATAK SAYISI = {bilgiler[1]}")
            print(f"GUNLUK KALMA UCRETI = {bilgiler[2]}")
            print(f"PUANI = {bilgiler[3]}")
            print("-" * 30)
            sayac += 1
                
            
    
    def hangi_hasta_hangi_hastanede(self,hasta_adi_soyadi):
        for hasta in self.hasta_ve_bulundugu_hastane.keys():
            if(hasta == hasta_adi_soyadi):
                print(f"{self.hasta_ve_bulundugu_hastane[hasta_adi_soyadi]}")
            
    def ucrete_gore_hastane_getir(self,ucret):
        if(ucret<200):
            print("400'den az gunluk yatak ucretine sahip hastane yoktur.Tekrar ucretinizi giriniz.")
        else:
            ucret_listesi = []
            for hastane_adi,bilgiler in self.hastaneler.items():
                gunluk_ucret = bilgiler[2]
                if gunluk_ucret >= ucret:
                    ucret_listesi.append((gunluk_ucret, hastane_adi))
            ucret_listesi.sort()
            if(not ucret_listesi):
                print(f"{ucret} TL veya daha fazla ücrette hastane bulunamadı.")
            else:
                print(f"\nGunluk {ucret} TL ve üstü ucrete sahip hastaneler:")
                for fiyat,ad in ucret_listesi:
                    print(f"{ad} → {fiyat} TL")
    def hastaneleri_goster(self):
        print(self.hastaneler)
    
    

hastane=Hastane()

while(True):
    print("\nHASTANE YONETIM SISTEMINE HOSGELDINIZ")
    print(40 * "-")
    print()
    print("1-HASTANE BILGILERI EKLE")
    print("2-HASTA BILGILERINI BASTIR")
    print("3-HASTANELERI GUNLUK KALMA UCRETINE GORE SIRALA")
    print("4-HASTANELERI YATAK SEVIYESINE GORE SIRALA(ARTAN)")
    print("5-HASTANELERI ADINA GORE SIRALA")
    print("6-HASTANELERI PUANINA GORE SIRALA")
    print("7-GIRILEN SEHIRDEKI HASTANELERI BASTIR")
    print("8-HASTA BILGILERI EKLE")
    print("9-HASTANE BILGILERINI BASTIR")
    print("10-HANGI HASTA HANGI HASTANEDE OLDUGUNU OGREN")
    print("11- UCRETE GORE HASTANE GETIR")
    print("12 CIKIS")
    secim = int(input("1-12 arasi secim yapiniz: "))
    
    if(secim==1):
        kac_tane = int(input("Kac tane hastane ekleyeceksiniz: "))
        
        for i in range(kac_tane):
            hastane_adi=input("Hastane adini giriniz: ").upper()
            sehir=input("Sehiri giriniz: ").upper()
            toplam_yatak_kapasitesi =int(input("Toplam yatak kapasitesi: "))
            gunluk_kalma_ucreti = float(input("Gunluk kalma ucreti: "))
            puan = float(input("Puan: "))
            hastane.hastane_bilgileri_ekle(hastane_adi,sehir,toplam_yatak_kapasitesi,gunluk_kalma_ucreti,puan)
        
    elif(secim==2):
        hastane.hasta_bilgierini_bastir()
        
    elif(secim==3):
        kac_gun = int(input("Kac gun kalicaksiniz? "))
        hastane.hastaneleri_goster()
        hastane_adi= input("Hastane adini giriniz: ")
        hastane.gunluk_kalma_ucretine_gore_hesapla(kac_gun,hastane_adi)
        
    elif(secim==4):
        hastane.yatak_seviyesine_gore_sirala()
        
    elif(secim==5):
        hastane.adina_gore_sirala()
        
    elif(secim==6):
        hastane.puanina_gore_sirala()
        
    elif(secim==7):
        sehir=input("Sehir giriniz: ").upper()
        hastane.girilen_sehirdeki_hastaneleri_bastir(sehir)
        
    elif(secim==8):
        kac_tane = int(input("KAC TANE HASTA EKLEYECEKSINIZ: "))
        for i in range(kac_tane):
            hasta_adi_soyadi = input("HASTA ADINI VE SOYADINI GIRINIZ: ").upper()
            yas = int(input("HASTANIN YASINI GIRINIZ: "))
            ID=int(input("HASTANIN ID GIRINIZ: "))
            hangi_hastane=input("Hasta hangi hastanede yaticak: ").upper()
            hastane.hasta_bilgileri_ekle(hasta_adi_soyadi,yas,ID,hangi_hastane)
    
    elif(secim==9):
        hastane.hastane_bilgilerini_bastir()
    
    elif(secim==10):
        print("HANGI HASTANIN HANGI HASTANEDE OLDUGU GOSTERILIYOR.")
        hasta_adi_soyadi = input("Hastanın adı ve soyadını giriniz: ").upper()
        hastane.hangi_hasta_hangi_hastanede(hasta_adi_soyadi)
    
    elif(secim==11):
        ucret= float(input("En az istediginiz ucreti giriniz: "))
        hastane.ucrete_gore_hastane_getir(ucret)
    
    elif(secim==12  ):
        print("CIKIS YAPILIYOR...")
        break
 
    else:
        
        print("Lutfen 1-8 arasi secim yapiniz.")
        break
    
        

    
    
    
    
    
    
