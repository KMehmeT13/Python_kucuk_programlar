import tkinter as tk #Arayüz için python kütüphanesi
from tkinter import messagebox #Kullanıcıya uyarı vermek için tkinter kütüphanesinin modülü

def sayi_kontrol():
    try: #fonkisyonun çalışmasından beklenilmeyen hata olmaması için fonksiyonu try yapısı içine alıyoruz
        sayi = int(entry.get())
        if sayi % 2 == 0: #girilen sayıyı 2 ye bölümünün 0 olması halinde çalışan karar yapısı
            messagebox.showinfo("Sonuç", "Girilen sayı çifttir.")
        else:#girilen sayıyı 2 ye bölümünün 0 olmaması halinde çalışan karar yapısı
            messagebox.showinfo("Sonuç", "Girilen sayı tektir.")

        devam = messagebox.askquestion("Devam", "Başka bir sayı girmek istiyor musunuz?")
        if devam == 'no': #ekrana gelen uyarı penceresine hayır butonuna tıklanılması halinde çalışan karar yapısı.
            messagebox.showinfo("Çıkış", "Programı kullandığınız için teşekkür ederim.")
            root.destroy()  # Pencereyi kapatır
        entry.delete(0, tk.END)  # Hata olmadığında metin kutusunu temizler

    except ValueError: #fonksiyon çalışırken fonksiyonda oluşan hatanın yakalanması ve ekrana messagebox olarak geri bildirim yapılması. 
        messagebox.showerror("Hata", "Yanlış giriş yaptınız. Lütfen bir sayı girin.")
        entry.delete(0, tk.END)  # Hata durumunda metin kutusunu temizler

root = tk.Tk()
root.title("Çift-Tek Sayı Kontrolcüsü") # Program penceresinde yazan isim


root.geometry("300x150")# Pencere boyutunu ayarla

label = tk.Label(root, text="Bir sayı girin:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Kontrol Et", command=sayi_kontrol)
button.pack()

root.mainloop()
