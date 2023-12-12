import tkinter as tk #Arayüz kütüphanesi
import socket #ağ iletişimi kütüphanesi

def internet_check(): #internet kontrol fonksiyonu
    try:#try-except yapısı ile internet olmaması halinde olumsuz dönüşü yakalayıp except tarafına iletir 
        socket.create_connection(("www.google.com", 80)) #socket kütüphanesi ile url ye bağlantı kurup cevap alma 
        status_label.config(text="İnternet Var :)", fg="green") #sonucun olumlu gelmesi halinde ekranda yazıcak bilgilendirme yazısı
    except OSError: #internet olmaması halinde verecek bağlantı hatasını yakalayan yapı
        status_label.config(text="İnternet Yok :(", fg="red") #alınan hata karşılığında ekrana yazdırılacak bilgilendirme yazısı

#kullanıcı arayüzü ayarları

root = tk.Tk()
root.title("İnternet Bağlantı Kontrolü")#pencere başlığı

root.geometry("400x200")  # Pencere boyutu

info_text = ( #Kullanıcı bilgilendirme mesajı
    "İnternet bağlantınızın olup olmadığını \n\n kontrol etmek için aşağıdaki butonu kullanabilirsiniz.\n\n"
    "Bağlantı Durumu:"
)

info_label = tk.Label(root, text=info_text, font=("Arial", 12)) #bilgilendirme mesajının yazılacağı alan
info_label.pack()

status_label = tk.Label(root, text="", font=("Arial", 16))#hata mesajı veya olumlu dönüş sonucunun yazılacağı alan
status_label.pack(pady=20)

check_button = tk.Button(root, text="Kontrol Et", command=internet_check, font=("Arial", 12)) #İnternet kontrol fonksiyonunu çalıştırıcak buton
check_button.pack()

root.mainloop()
