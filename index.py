class Kitap:
    kitapListesi = []

    def __init__(self, yazarAdi, eserAdi, tarih):
        self.eserAdi = eserAdi
        self.yazarAdi = yazarAdi
        self.tarih = tarih
        Kitap.kitapListesi.append(self)


    def kutuphanedenCek(self, dosyaAdi):                                ############# Bir dosyadan önceki kaydedilmiş verileri çeker
        try:
            kitaplarDosya = open(dosyaAdi, "r")
            for i in kitaplarDosya.readlines():
                bilgiler = i.split(",")
                Kitap(bilgiler[0], bilgiler[1], bilgiler[2])
            kitaplarDosya.close()
        except FileNotFoundError:
            print("Belirtilen Kütüphane Dosyası Bulunamadı!")
        except:
            print("Belirtilen Kütüphane Dosyası Boş!")


    def kitabiDosyayaYaz(self, birKitap, dosyaAdi):                     ############ Yeni eklenen kitapları dosyaya kaydeder
        kitaplarDosya = open(dosyaAdi, "a")
        kitaplarDosya.write("{},{},{}\n".format(birKitap.yazarAdi, birKitap.eserAdi, birKitap.tarih))
        kitaplarDosya.close()

    def yeniKitapKaydi(self, dosyaAdi):                                 ############ Yeni kitap kaydı yapar
        yazarAdi = input("Lütfen yazarın adını giriniz: ")
        eserAdi = input("Lütfen eserin adını giriniz: ")
        tarih = input("Lütfen tarihi giriniz: ")
        print("Kitap başarıyla eklendi!\n")
        kitap = Kitap(yazarAdi, eserAdi, tarih)
        self.kitabiDosyayaYaz(kitap, dosyaAdi)

    def kitaplariListele(self):                                         ############ Dosyadan çekilen ve sonradan kaydedilen kitapları listeler
        if len(Kitap.kitapListesi) == 1:
            print("Hiç kitap bulunamadı!")
        else:
            print("\n----- Yazar Adı ----- | ------ Eser Adı ------ | --- Tarih ---")
            for kitap in Kitap.kitapListesi:
                if len(kitap.yazarAdi) > 0:
                    print("{:24}{:25}{}".format(kitap.yazarAdi, kitap.eserAdi, kitap.tarih.rstrip("\n")))
            print()

    def kitapAra(self):                                                 ############ Dosyadan çekilen ve sonradan kaydedilen kitaplar arasında arama yapar
        cevap = input("""Aramanızı Neye Göre yapmak İstiyorsunuz?
    1. Kitap Adına Göre
    2. Yazar Adına Göre
    3. Tarihe Göre
Lütfen isteğinizin yanındaki numarayı giriniz: """)
        if (cevap == "1"):
            bulunamadı = True
            eserAdi = input("Lütfen kitabın adını giriniz: ")
            for kitap in Kitap.kitapListesi:
                if eserAdi in kitap.eserAdi:
                    bulunamadı = False
                    break

            if bulunamadı:
                print("Aradığınız isimde bir kitap bulunamadı!")
            else:
                print("\n          *** Bulunan Kitaplar Listesi ***")
                print("\n----- Yazar Adı ----- | ------ Eser Adı ------ | --- Tarih ---")
                for kitap in Kitap.kitapListesi:
                    if eserAdi in kitap.eserAdi:
                        print("{:24}{:25}{}".format(kitap.yazarAdi, kitap.eserAdi, kitap.tarih.rstrip("\n")))
        elif (cevap == "2"):
            bulunamadı = True
            yazarAdi = input("Lütfen yazarın adını giriniz: ")
            for kitap in Kitap.kitapListesi:
                if yazarAdi in kitap.yazarAdi:
                    bulunamadı = False
                    break

            if bulunamadı:
                print("Aradığınız isimde bir yazar bulunamadı!")
            else:
                print("\n          *** Bulunan Kitaplar Listesi ***")
                print("\n----- Yazar Adı ----- | ------ Eser Adı ------ | --- Tarih ---")
                for kitap in Kitap.kitapListesi:
                    if yazarAdi in kitap.yazarAdi:
                        print("{:24}{:25}{}".format(kitap.yazarAdi, kitap.eserAdi, kitap.tarih.rstrip("\n")))
        else:
            bulunamadı = True
            tarih = input("Lütfen tarihi giriniz: ")
            for kitap in Kitap.kitapListesi:
                if tarih in kitap.tarih.rstrip("\n"):
                    bulunamadı = False
                    break

            if bulunamadı:
                print("Aradığınız tarihli bir kitap bulunamadı!")
            else:
                print("\n          *** Bulunan Kitaplar Listesi ***")
                print("\n----- Yazar Adı ----- | ------ Eser Adı ------ | --- Tarih ---")
                for kitap in Kitap.kitapListesi:
                    if tarih == kitap.tarih.rstrip("\n"):
                        print("{:24}{:25}{}".format(kitap.yazarAdi, kitap.eserAdi, kitap.tarih.rstrip("\n")))
        print()

    def uygulamayiCalistir(self):                                     ########## Uygulamanın doğru çalışmasını sağlar

        self.kutuphanedenCek("kutuphaneDosyasi.txt")

        print("*** Kütüphane Katalogu Uygulamasına Hos Geldiniz ***")
        while True:
            islem = input("""    1. Yeni Kitap Kaydı Oluştur
    2. Kitapları Listele
    3. Kitap Sorgula
    4. Çıkış
Lütfen yapmak istediğiniz işlemin yanındaki numarayı giriniz: """)

            if (islem == "4"):
                break

            elif (islem == "1"):
                self.yeniKitapKaydi("kutuphaneDosyasi.txt")

            elif (islem == "2"):
                self.kitaplariListele()

            elif (islem == "3"):
                self.kitapAra()

kitap = Kitap("","","")
kitap.uygulamayiCalistir()
