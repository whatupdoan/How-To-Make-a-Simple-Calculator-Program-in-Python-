# Python ile Basit Hesap Makinesi Yapımı.
import time
class Hesapla:
    def SayıAl(self):
        time.sleep(2)
        print("")
        self.sayi1 = float(input("1.Sayıyı giriniz: "))
        time.sleep(1)
        self.sayi2 = float(input("2.Sayıyı giriniz: "))

    def İslem(self):
        self.islem = input("""
[1] = Toplama
[2] = Çıkarma
[3] = Çarpma
[4] = Bölme
[5] = Üs Alma
[6] = Çıkış

""")

    def Sonuc(self):
        if self.islem == "1":
            self.sonuc = self.sayi1 + self.sayi2
            print("Sonuç: ", self.sonuc)
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
        elif self.islem == "2":
            self.sonuc = self.sayi1 - self.sayi2
            print("Sonuç: ", self.sonuc)
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
        elif self.islem == "3":
            self.sonuc = self.sayi1 * self.sayi2
            print("Sonuç: ", self.sonuc)
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
        elif self.islem == "4":
            self.sonuc = self.sayi1 / self.sayi2
            print("Sonuç: ", self.sonuc)
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
        elif self.islem == "5":
            self.sonuc = self.sayi1 ** self.sayi2
            print("Sonuç: ", self.sonuc)
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
        elif self.islem == "6":
            print("Veriler Sıfırlanıyor...")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            quit()
    def AnaProgram(self):
        self.SayıAl()
        self.İslem()
        self.Sonuc()


hesapla = Hesapla()
while True:
    hesapla.AnaProgram()

# Python ile Basit Hesap Makinesi Yapımı.