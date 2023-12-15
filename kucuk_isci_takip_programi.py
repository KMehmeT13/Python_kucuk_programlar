import tkinter as tk #arayüz için kütüphane
from tkinter import ttk, messagebox #mesaagebox için tkinterden çekme
from datetime import datetime #Giriş çıkış zamanı hesaplaması için kütüphane

def hesapla_gun_sayisi(): #gün hesaplama fonksiyonu
    selected_item = listbox.selection() #listede seçilen elemanı manipüle eder
    if selected_item: #seçilen parametrede hangi verileri çekeceğini gösteren karar yapısı 
        is_giris_str = listbox.item(selected_item, 'values')[3]
        is_cikis_str = listbox.item(selected_item, 'values')[4]
        
        try: #alınan verileri try-except yapısı içerisinde matematiksel hesaplamasını yapıp değişkene atama işlemini yapıyor
            is_giris = datetime.strptime(is_giris_str, "%d/%m/%Y")
            is_cikis = datetime.strptime(is_cikis_str, "%d/%m/%Y")
            
            if is_cikis < is_giris: #iştençıkış tarihi işe giriş tarihinden küçükse kullanıcıya hata verir
                messagebox.showerror("Hata", "İşten çıkış tarihi işe giriş tarihinden önce olamaz.")
                return  
            
            calisma_gunu = (is_cikis - is_giris).days
                 
            listbox.set(selected_item, column="#6", value=calisma_gunu) #Yapılan işlemin sonucunu 6.kolona atar
        except ValueError as e: #Girilen hesaplarda yanlış bilgi olursa yakalaması ve kullanıcıya bilgi veren yapı
            print("Hesaplama Hatası:", e)
            messagebox.showerror("Hata", "Tarih formatı hatalı. (gg/aa/yyyy)")

def dogrulama(ad, soyad): #İsim ve soy isimde sadece harf olduğunu doğrulayan fonksiyon
    return ad.isalpha() and soyad.isalpha()

def dogum_tarihi_kontrol(girilen): #Tarih girilen alanda tarih dışında bir veri girip girilmediğini kontrol eden fonksiyon
    try:
        datetime.strptime(girilen, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def is_giris_kontrol(girilen): #Tarih girilen alanda tarih dışında bir veri girip girilmediğini kontrol eden fonksiyon
    try:
        datetime.strptime(girilen, "%d/%m/%Y")
        return True
    except ValueError:
        return False    

def is_cikis_kontrol(girilen): #Tarih girilen alanda tarih dışında bir veri girip girilmediğini kontrol eden fonksiyon
    try:
        datetime.strptime(girilen, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def bosluk_kontrol(): # Text boxlarda tüm boşlukların doldurulup doldurulmadığını kontrol eden fonksiyon
    if not all(entry.get() for entry in [entry_ad, entry_soyad, entry_dogum, entry_giris, entry_cikis]):
        messagebox.showwarning("Uyarı", "Lütfen tüm boşlukları doldurun.")
        return False
    return True

        
def ekle(): #Textboxlara girilen verilerin ilgili değişkenlere atanmasını sağlayan fonksiyon
    if bosluk_kontrol():
        ad = entry_ad.get()
        soyad = entry_soyad.get()
        dogum_tarihi = entry_dogum.get()
        ise_giris = entry_giris.get()
        ise_cikis = entry_cikis.get()
        entry_ad.delete(0, tk.END)
        entry_soyad.delete(0, tk.END)
        entry_dogum.delete(0, tk.END)
        entry_giris.delete(0, tk.END)
        entry_cikis.delete(0, tk.END)

        if dogrulama(ad, soyad): #Kayıt işlemi yapılırken Doğrulama yapan kara yapısı
            if dogum_tarihi_kontrol(dogum_tarihi):
                listbox.insert("", "end", values=(ad, soyad, dogum_tarihi, ise_giris, ise_cikis))
                listbox.column("#0", width=100)
                listbox.heading("#0", text="No.")
                listbox.column("#1", width=100)
                listbox.heading("#1", text="Adı")
                listbox.column("#2", width=100)
                listbox.heading("#2", text="Soyadı")
                listbox.column("#3", width=100)
                listbox.heading("#3", text="Doğum Tarihi")
                listbox.column("#4", width=100)
                listbox.heading("#4", text="İşe Giriş Tarihi")
                listbox.column("#5", width=100)
                listbox.heading("#5", text="İşten Çıkış Tarihi")
                listbox.column("#6", width=100)
                listbox.heading("#6", text="Çalışma Günü")
            else:
                messagebox.showerror("Hata", "Lütfen doğru tarih formatı girin (gg/aa/yyyy).")
        else:
            messagebox.showerror("Hata", "Lütfen sadece harf içeren bir ad ve soyad girin.")

def sil(): #Listeden seçilen sonucu listeden kaldırmak için kullanılan fonksiyon
    selected_item = listbox.selection()
    if selected_item:
        confirm = messagebox.askokcancel("Silme İşlemi", "Seçili öğeyi silmek istediğinizden emin misiniz?")
        if confirm:
            listbox.delete(selected_item)

def temizle(): #bütün textboxları temizleyen fonksiyon
    entry_ad.delete(0, tk.END)
    entry_soyad.delete(0, tk.END)
    entry_dogum.delete(0, tk.END)
    entry_giris.delete(0, tk.END)
    entry_cikis.delete(0, tk.END)

def belgeye_aktar(): #Girilen bilgileri not defterine aktaran fonksiyon
    with open("isci_bilgileri.txt", "w") as file:
        for item in listbox.get_children():
            content = listbox.item(item)["values"]
            file.write("|".join(str(x) for x in content) + "\n")

#####Arayüz kodları

root = tk.Tk()
root.title("Bilgi Girişi")

label_ad = tk.Label(root, text="Adı:")
label_ad.grid(row=0, column=0)
entry_ad = tk.Entry(root)
entry_ad.grid(row=0, column=1)

label_soyad = tk.Label(root, text="Soyadı:")
label_soyad.grid(row=1, column=0)
entry_soyad = tk.Entry(root)
entry_soyad.grid(row=1, column=1)

label_dogum = tk.Label(root, text="Doğum Tarihi:")
label_dogum.grid(row=2, column=0)
entry_dogum = tk.Entry(root)
entry_dogum.grid(row=2, column=1)

label_giris = tk.Label(root, text="İşe Giriş Tarihi:")
label_giris.grid(row=3, column=0)
entry_giris = tk.Entry(root)
entry_giris.grid(row=3, column=1)

label_cikis = tk.Label(root, text="İşten Çıkış Tarihi:")
label_cikis.grid(row=4, column=0)
entry_cikis = tk.Entry(root)
entry_cikis.grid(row=4, column=1)

ekle_button = tk.Button(root, text="Ekle", command=ekle)
ekle_button.grid(row=5, column=0, columnspan=2)

sil_button = tk.Button(root, text="Sil", command=sil)
sil_button.grid(row=6, column=0, columnspan=2)

temizle_button = tk.Button(root, text="Boşlukları Temizle", command=temizle)
temizle_button.grid(row=7, column=0, columnspan=2)

hesapla_button = tk.Button(root, text="Çalışma Gününü Hesapla", command=hesapla_gun_sayisi)
hesapla_button.grid(row=10, column=0, columnspan=2)

belgeye_aktar_button = tk.Button(root, text="Belgeye Aktar", command=belgeye_aktar)
belgeye_aktar_button.grid(row=8, column=0, columnspan=2)

columns = ("Adı", "Soyadı", "Doğum Tarihi", "İşe Giriş Tarihi", "İşten Çıkış Tarihi", "Çalışma Günü")
listbox = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    listbox.heading(col, text=col)
    listbox.column(col, width=100)
listbox.grid(row=9, column=0, columnspan=2, sticky="nsew")

root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
