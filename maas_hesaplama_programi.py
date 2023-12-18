import tkinter as tk
from tkinter import messagebox


def hesapla(): #hesapla fonksiyonu ile temel hesapların ve sonuçlarının nereye yazılacağını gösteriyoruz.
    try: #try - except yapısı ile veri türü girişlerini kontrol etmek
        gunluk_ucret = float(entry_gunluk_ucret.get()) #gunluk ücret textboxundan veri çekip değişkene atar
        calisma_gunu = int(entry_calisma_gunu.get())#calisma günü textboxundan veri çekip değişkene atar
        vergi_orani = int(entry_vergi_orani.get())#vergi oranı textboxundan veri çekip değişkene atar

               
        aylik_ucret = gunluk_ucret * calisma_gunu        #aylık ücret matematik hesaplaması
        label_aylik_ucret["text"] = f"Aylık Ücret: {aylik_ucret} TL" #aylık ücret sonucunu ilgili etikete (label) yazdırır

        vergi_miktari = aylik_ucret * vergi_orani / 100  #vergi oranı matematik hesaplaması
        label_vergi_miktari["text"] = f"Gelir Vergisi: {vergi_miktari} TL" #vergi oranı sonucunu ilgili etikete (label) yazdırır 

        kalan_ucret = aylik_ucret - vergi_miktari # kalan ücretin matematik hesaplaması
        label_kalan_ucret["text"] = f"Vergi Sonrası Kalan Ücret: {kalan_ucret} TL" #kalan ücretin sonucunu ilgili etikete (label) yazdırır

        if not gunluk_ucret or not calisma_gunu or not vergi_orani: #belirtilen textboxların boş kalması halinde kullanıcıyı uyarır
            raise ValueError("Lütfen bütün boşlukları doldurun!") #Kullanıcıya bilgi mesajı
    except ValueError: #Yakalanan değer hatalarının kullanıcıya bilgilendirilmesi
        label_vergi_miktari["text"] = "Geçersiz veri girişi!"
        label_aylik_ucret["text"] = "Geçersiz veri girişi!"
        label_kalan_ucret["text"] = "Geçersiz veri girişi!"
        messagebox.showwarning("Uyarı", "Lütfen bütün boşlukları doldurun!\n Boş veya sayı harici giriş yapmayın!")





def temizle(): #girilen parametreleri temizleyen fonksiyon
    result = messagebox.askquestion("Onay", "Tüm verileri silmek istediğinize emin misiniz?")
    if result == "yes": #textboxların dolu olup olmadığı kontrolünü sağlayan karar yapısı
        entry_gunluk_ucret.delete(0, tk.END) #günlük ücreti silen metod
        entry_calisma_gunu.delete(0, tk.END)#çalışma gününü silen metod
        entry_vergi_orani.delete(0, tk.END)#vergi oranını silen metod
        label_aylik_ucret["text"] = "Aylık Ücret: " #aylik ücret etiketine aktarılan sonuçların temizlenip eski haline getiren metod
        label_vergi_miktari["text"] = "Gelir Vergisi:" #vergi miktarı etiketine aktarılan sonuçların temizlenip eski haline getiren metod
        label_kalan_ucret ["text"] = "Vergi Sonrası Kalan Ücret:"#kalan ücret etiketine aktarılan sonuçların temizlenip eski haline getiren metod
#
#
#
#arayüz düzenlemeleri

#açılır pencere
root = tk.Tk()
root.title("Ücret ve Vergi Hesaplama")
root.geometry("500x400")

# Günlük Ücret
label_gunluk_ucret = tk.Label(root, text="Günlük Ücret :")
label_gunluk_ucret.grid(row=0, column=0)
entry_gunluk_ucret = tk.Entry(root)
entry_gunluk_ucret.grid(row=0, column=1)

# Çalışma Günü
label_calisma_gunu = tk.Label(root, text="Çalışma Günü :")
label_calisma_gunu.grid(row=1, column=0)
entry_calisma_gunu = tk.Entry(root)
entry_calisma_gunu.grid(row=1, column=1)

# Gelir Vergisi Oranı
label_vergi_orani = tk.Label(root, text="Gelir Vergisi Oranı (%):")
label_vergi_orani.grid(row=2, column=0)
entry_vergi_orani = tk.Entry(root)
entry_vergi_orani.grid(row=2, column=1)

# Hesapla Butonu
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
button_hesapla.grid(row=3, column=0)

button_temizle = tk.Button(root, text="Temizle", command=temizle)
button_temizle.grid(row=4, column=0, )

# Gelir Vergisi Sonucu
label_vergi_miktari = tk.Label(root, text="Gelir Vergisi: ")
label_vergi_miktari.grid(row=3, column=1)

# Aylık Ücret
label_aylik_ucret = tk.Label(root, text="Aylık Ücret: ")
label_aylik_ucret.grid(row=4, column=1)

# Kalan Ücret
label_kalan_ucret = tk.Label(root, text="Vergi Sonrası Kalan Ücret: ")
label_kalan_ucret.grid(row=5, column=1)

root.mainloop()
