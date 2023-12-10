import tkinter as tk

def hesapla(): #Kullanıcı verilerine göre hesaplama yapan fonksiyon
    try: #Kullanıcıdan beklenmedik bir veri girişi olması halinde hatayı yakalaması için try-except yapısı (except 9.satırda)
        maas = float(entry_maas.get().replace(',', '')) #Kullanıcıdan alınan maas parametresi
        zam_orani = float(entry_zam.get().replace(',', '')) #Kullanıcıdan alınan zam parametresi
        yeni_maas = maas + (maas * zam_orani / 100) #Kullanıcıdan alınan parametrelerin matematiksel işlemlerinin yapılması
        label_sonuc["text"] = f"Maaşın zamlı hali: {yeni_maas:.2f} TL" #Zamlı maaş bilgisinin ekrana yazdırılması
    except ValueError:
        label_sonuc["text"] = "Geçersiz veri. Lütfen sayı girin." #Olağandışı durum yaşanması halinde ekrana yazılan hata mesajı

def temizle(): #Temizle butonu ile girilen ve sonuçlanan verilerin silinmesi fonksiyonu
    entry_maas.delete(0, tk.END)
    entry_zam.delete(0, tk.END)
    label_sonuc["text"] = ""

#Arayüz Ayarları

#Program başlığı
root = tk.Tk() 
root.title("Maaş Zammı Hesaplama")

#Arayüz öğelerini düzenlemek ve gruplamak için frame
frame = tk.Frame(root)
frame.pack(padx=40, pady=40)

#Kullanıcıya programın kullanışı hakkında verilen bilgi metini
label_info = tk.Label(frame, text="Zamlı maaşı hesaplamak için hesaplanması istenilen güncel maaşı aşağıdaki ilgili kutucuğa sadece sayı olarak giriş yapınız.\n\nHesaplanmasını istediğiniz zam oranını sayı olarak aşağıda belirtilen ilgili kutucuğa girin ardından 'Hesapla' butonuna basınız.\n\nİşlemlerinizin bitmesi ve yeniden bir hesaplama işlemi yapmak istiyorsanız 'Temizle' butonunu kullanarak ekrandaki verileri silebilir ve yeni hesaplama yapabilirsiniz.", fg='grey')
label_info.pack(padx=5, pady=5)

#Maas textboxu için kullanıcı bilgilendirmesi
label_maaş_miktarı = tk.Label(frame, text="Maaş Miktarı")
label_maaş_miktarı.pack(padx=5, pady=5)

#Maas textboxu
entry_maas = tk.Entry(frame, fg='grey')
entry_maas.pack(padx=5, pady=5)

#Zam textboxu için kullanıcı bilgilendirmesi
label_zam = tk.Label(frame, text="Zam Oranı (%):")
label_zam.pack(padx=5, pady=5)

#Zam textboxu
entry_zam = tk.Entry(frame)
entry_zam.pack(padx=5, pady=5)

#Hesapla butonu
button_hesapla = tk.Button(frame, text="Hesapla", command=hesapla)
button_hesapla.pack(padx=5, pady=5)

#Temizle butonu
button_temizle = tk.Button(frame, text="Temizle", command=temizle)
button_temizle.pack(padx=5, pady=5)

#Sonucun ekrana yazdırıldığı metin bölgesi
label_sonuc = tk.Label(frame, text="")
label_sonuc.pack(padx=5, pady=5)

#geliştirici bilgisi
label_info = tk.Label(frame, text="©T13.Developer")
label_info.pack(padx=5, pady=5)

root.mainloop()
