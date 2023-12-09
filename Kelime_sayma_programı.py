import tkinter as tk
from tkinter import messagebox

def kelime_say():
    try: #Olası bir hata olması halinde kullanıcıya uyarı vermek için try-except yapısı (5.satırda try 10.satırda except fonksiyonu)
        metin = metin_alani.get("1.0", tk.END) #metin kutusu içerisinde ilk kelimeden son kelime aralığını seçer.
        kelimeler = metin.split() #split fonksiyonu ile "kelimeler" adlı değişkene kelimeleri atar.
        kelime_sayisi = len(kelimeler) #len fonksiyonu ile kelime adetini belirler.
        messagebox.showinfo("Kelime Sayısı", f"Metindeki kelime sayısı: {kelime_sayisi}") #Ekrana messagebox ile kelime sayısını gösteren fonksiyon.
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
def karakter_say():
    try:#Olası bir hata olması halinde kullanıcıya uyarı vermek için try-except yapısı (13.satırda try 17.satırda except fonksiyonu)
        metin = metin_alani.get("1.0", tk.END) # Metin kutusu içerisinde ilk karakter ile son karakter aralığını seçer.
        karakter_sayisi = len(metin) - metin.count("\n")  # Satırbaşı karakterlerini saymamak için ve len fonksiyonu ile karakterleri sayar.
        messagebox.showinfo("Karakter Sayısı", f"Metindeki karakter sayısı(Boşluklar ile birlikte): {karakter_sayisi}") #Ekrana messagebox ile kelime sayısını gösteren fonksiyon.
    except Exception as e:
        messagebox.showerror("Hata", f"bir hata oluştu: {e}")
def temizle():
    metin_alani.delete("1.0", tk.END) #Delete fonksiyonu ile metin alanındaki ilk kelimeden son kelimeye kadar siler

# Tkinter penceresini oluşturma
pencere = tk.Tk()
pencere.title("Kelime ve Karakter Sayacı")
pencere.geometry("600x500")  # açılır pencere boyutu

# Metin kutusu oluşturma ve yerleştirme
metin_alani = tk.Text(pencere, height=20, width=80)
metin_alani.grid(row=0, column=0, columnspan=3, pady=10)  # Metin kutusunu tam genişlikte yerleştirme

# "Hesapla" butonu oluşturma ve yerleştirme
hesapla_buton = tk.Button(pencere, text="Kelime Sayısı", command=kelime_say)
hesapla_buton.grid(row=1, column=0, padx=5, pady=5)  # Hesapla butonunu sola yerleştirme

# "Karakter Sayısı" butonu oluşturma ve yerleştirme
karakter_sayi_buton = tk.Button(pencere, text="Karakter Sayısı", command=karakter_say)
karakter_sayi_buton.grid(row=1, column=1, padx=5, pady=5)  # Karakter Sayısı butonunu ortaya yerleştirme

# "Temizle" butonu oluşturma ve yerleştirme
temizle_buton = tk.Button(pencere, text="Temizle", command=temizle)
temizle_buton.grid(row=1, column=2, padx=5, pady=5)  # Temizle butonunu sağa yerleştirme

pencere.mainloop()
