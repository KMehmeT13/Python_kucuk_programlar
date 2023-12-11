import tkinter as tk
from tkinter import messagebox

def calculate_kdv(): #Kdv hesaplama fonksiyonu
    try: #Olası hata olması halinde hatayı yakalaması için try-except yapısı içerisine alınıyor (except 19.satırda)
        value = float(entry.get()) #Kullanıcıdan textbox aracılığı ile parametre alınması
        selected_index = dropdown_value.get() #Selected index ile dropdown menüsündeki var olan değer ilk başta %1 olarak alınıyor.
        kdv_orani = 0.01 #%1 değer ataması

        if selected_index == "%18": #%18 adlı dropdown menü seçeneğine değer atanması
            kdv_orani = 0.18
        elif selected_index == "%20":#%20 adlı dropdown menü seçeneğine değer atanması
            kdv_orani = 0.20

        kdv_miktari = value * kdv_orani #Hangi kdv oranı seçilirse seçilsin yapılan sabit matematiksel kdv orani hesabı
        toplam = value + kdv_miktari #Hesaplanan kdv yi değere atıyarak kdv li oranın gösterilmesi

        result_label.config(text=f"KDV Sonucu: {kdv_miktari:.2f}, Toplam: {toplam:.2f}") #Çıkan sonuçların ekrana yazdırılması
    except ValueError:
        messagebox.showwarning("Hata", "Geçersiz değer!")
        entry.delete(0, tk.END) #hata kullanıcıya verildikten sonra bütün verilerin silinmesi

def clear_fields(): #Temizle butonu ile sonuçlanan değerlerin sıfırlanması
    entry.delete(0, tk.END)
    result_label.config(text="KDV Sonucu: ")

#Buradan aşağısı arayüz düzenlemeleri ve fonksiyon arayüz bağlantılarını içerir

root = tk.Tk()
root.title("KDV Hesaplayıcı") 
root.geometry("700x300")  

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

info_text = (
    "Aşağıdaki boşluğa hesaplanılacak ücretin kdvsiz değerini giriniz. "
    "Metin boşluğunun yanında bulunan menüden kdv oranını seçin ve "
    "hesapla butonuna basın. Yeniden işlem yapmak istiyorsanız "
    "temizle butonunu kullanarak bütün değerleri silebilirsiniz. "
    )

info_label = tk.Label(main_frame, text=info_text, wraplength=380, justify=tk.LEFT)
info_label.pack()

input_frame = tk.Frame(main_frame)
input_frame.pack()

label = tk.Label(input_frame, text="Değer:")
label.grid(row=0, column=0)

entry = tk.Entry(input_frame)
entry.grid(row=0, column=1)

dropdown_value = tk.StringVar()
dropdown = tk.OptionMenu(input_frame, dropdown_value, "%1", "%18", "%20")
dropdown.grid(row=0, column=2)

calculate_button = tk.Button(main_frame, text="Hesapla", command=calculate_kdv)
calculate_button.pack(pady=10)

result_label = tk.Label(main_frame, text="KDV Sonucu: ")
result_label.pack()

clear_button = tk.Button(main_frame, text="Temizle", command=clear_fields)
clear_button.pack()

root.mainloop()
