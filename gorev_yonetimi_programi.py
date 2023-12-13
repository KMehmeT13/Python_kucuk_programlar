import tkinter as tk
from tkinter import messagebox

def gorev_ekle(event=None): # gorev ekleme fonksiyonu
    yeni_gorev = entry.get() # textboxa girilen parametreyi yeni_gorev adlı değişkene atama
    if yeni_gorev:
        listbox.insert(tk.END, yeni_gorev) #girilen parametreyi listeye ekleme
        entry.delete(0, tk.END) # listeye ekleme yapıldıktan sonra textboxu temizleme

def gorev_sil(): #gorev silme fonksiyonu
    secili = listbox.curselection() #listenin içinden seçili olan öğeyi secili atlı değişkene atar
    if secili: 
        index = secili[0] #secili adlı değişkene atanmış değerin 0 ıncı öğesini index adlı değişkene atar
        listbox.delete(index) # index adlı değişkeni siler

def temizle(): #gorevlerin hepsini silme fonksiyonu
    cevap = messagebox.askquestion("Onay", "Listeyi temizlemek istediğinizden emin misiniz? (Bütün öğeler silinecektir)") #yanlışlıkla bütün listenin silinmesini engellemek için onay kutusu açılması
    if cevap == 'yes': # cevap evet olması halinde aşağıdaki metodu çalıştırır
        listbox.delete(0, tk.END)  #listedeki bütün öğeleri siler

def alfabetik_sirala(): #alfabetik sıralama fonksiyonu
    items = list(listbox.get(0, tk.END)) #items adlı yeni bir liste oluşturup bu listeyi "listbox" adlı listeden alır.
    items.sort() #sort adlı metod ile listeyi alfabetik olarak sıralar
    listbox.delete(0, tk.END) #listedeki bütün öğeleri siler
    for item in items: #items adlı değişkenin içindeki öğe kadar döngüye sokar
        listbox.insert(tk.END, item) #döngü her döndüğünde listbox adlı listeye geri yazdırma yapar buda alfabetik sıralamayı sağlar
        
def klavye_o(event): #Klavyeden etkinlik alma fonksiyonu
    if event.keysym == 'Delete': #delete adlı tuşa basıldığında yakalanması için if yapısı
        gorev_sil() #delete tuşuna basınca çalışan fonksiyon

#Arayüz Düzenlemeleri

root = tk.Tk()
root.title("Görev Yöneticisi")

entry = tk.Entry(root, width=35)
entry.pack(padx=10, pady=5)
entry.bind('<Return>', gorev_ekle)  

ekle_button = tk.Button(root, text="Görev Ekle", command=gorev_ekle)
ekle_button.pack(padx=10, pady=5)

frame = tk.Frame(root)
frame.pack(padx=10, pady=5)

listbox = tk.Listbox(frame, height=15, width=40)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

y_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

x_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scrollbar.pack(fill=tk.X)

listbox.config(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
y_scrollbar.config(command=listbox.yview)
x_scrollbar.config(command=listbox.xview)

sil_button = tk.Button(root, text="Seçili Görevi Sil", command=gorev_sil)
sil_button.pack(padx=10, pady=5)

temizle_button = tk.Button(root, text="Listeyi Temizle", command=temizle)
temizle_button.pack(padx=10, pady=5)

siralama_button = tk.Button(root, text="Listeyi Alfabetik Sırala", command=alfabetik_sirala)
siralama_button.pack(padx=10, pady=5)



x_scrollbar.place(in_=listbox, relx=0, rely=1, anchor=tk.SW)

root.bind('<Key>', klavye_o)

root.mainloop()
