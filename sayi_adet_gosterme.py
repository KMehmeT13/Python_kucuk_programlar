import tkinter as tk

def sayi_adetini_goster(): #Girilen sayıların arasındaki adeti hesaplayan fonksiyon
    try:
        # Text boxlardan girilen değerleri al
        baslangic = int(entry_baslangic.get())
        bitis = int(entry_bitis.get())
        
        
        adet = abs(baslangic - bitis) + 1 # Girilen değerler arasındaki sayı adedini hesapla
        
        
        label_sonuc["text"] = f"Girilen aralıkta {adet} adet sayı var."  # Sonucu ekranda göster
    except ValueError:
        label_sonuc["text"] = "Lütfen sadece tamsayı girin!" #Kutulara değer girilirken sayı dışında bir değer girilmesi halinde yakalanan hatanın cevabı

def bilgileri_temizle(): #işlem sonuçlandıktan sonra kutucukların ve pencerenin temizlenmesi fonksiyonu
    entry_baslangic.delete(0, tk.END)
    entry_bitis.delete(0, tk.END)
    label_sonuc["text"] = ""

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Sayı Adedi Hesaplama") #Programın penceresinin üst kısmında yazan başlık

# Giriş kutularını oluşturma ve hizalama
#Başlangıç sayısının yazılacağı metin kutusunun düzeni
label_baslangic = tk.Label(root, text="Başlangıç:")
label_baslangic.pack()
entry_baslangic = tk.Entry(root)
entry_baslangic.pack()

#Bitiş sayısının yazılacağı metin kutusunun düzeni
label_bitis = tk.Label(root, text="Bitiş:")
label_bitis.pack()
entry_bitis = tk.Entry(root)
entry_bitis.pack()

# Butonları oluşturma ve hizalama
frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_hesapla = tk.Button(frame_buttons, text="Hesapla", command=sayi_adetini_goster)
button_hesapla.pack(side=tk.LEFT, padx=5, pady=5)

button_temizle = tk.Button(frame_buttons, text="Temizle", command=bilgileri_temizle)
button_temizle.pack(side=tk.LEFT, padx=5, pady=5)

# Sonucu gösterecek olan etiket
label_sonuc = tk.Label(root, text="")
label_sonuc.pack()

# Pencere boyutunu büyüt
root.geometry("500x300")

# Pencereyi göster
root.mainloop()
