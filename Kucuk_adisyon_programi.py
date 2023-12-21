import tkinter as tk
from tkinter import ttk, messagebox

# Ürünler ve fiyatları
products = {
    "Çay": 5,
    "Gazoz": 10,
    "Su": 2,
    "Oralet": 7,
    "Kek": 10,
    "Tost": 20
}

def add_to_order(): # Ürün ekleme fonksiyonu
    global total_price #Toplam ücret değişkenini tanımlıyoruz
    selected_product = product_option.get() #drop down listesindeki ürünü seçince seçilen ürünü göstermek ve hesaplamak için sabitler
    quantity = quantity_entry.get() #miktar parametre girişini miktar adlı değişkene atar

    try:
        quantity = int(quantity) #girilen miktar int ifade ise izin verir
        if quantity <= 0: #girilen miktar 0 dan küçük veya 0 olma durumunu kontrol eder
            raise ValueError #Karar yapısını hatasını yakalar
            

        price = products[selected_product] * quantity #seçili ürün adeti ile ürüne girilen ücreti çarpar
        order_tree.insert("", tk.END, values=(selected_product, quantity, price, "TL")) #arayüzdeki order tree yani adisyon bölümüne parantez içindeki değerleri ekler
        total_price += price #bu satırdan bir önceki satırdaki değerlerin içindeki ücreti toplam ücrete ekler
        total_label.config(text=f"Toplam Ücret: {total_price} TL") #total_price adlı değişkenin değerini toplam ücret adlı label a ekler 
        quantity_entry.delete(0, tk.END)  # Adet girişini temizleme
        quantity_entry.insert(0, "1")  # Adet textbox'ına otomatik olarak 1 değerini yapar
        
    except ValueError as e:
        # Hata durumunda messagebox ile kullanıcıya uyarı verme
        tk.messagebox.showerror("Hata!", "Sadece sayı giriniz!")
        quantity_entry.delete(0, tk.END) 

def delete_selected(): #ürün ekleme fonksiyonu ile eşdeğer çalışır ancak bu sefer tam tersini !! SEÇİLEN !! ürünü adisyon listesinden siler
    selected_item = order_tree.selection()
    if selected_item:
        item = order_tree.item(selected_item)['values']
        price = int(item[2])
        order_tree.delete(selected_item)
        global total_price
        total_price -= price
        total_label.config(text=f"Toplam Ücret: {total_price} TL")
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, "1")  #silindikten sonra default olarak 1 değerini yerleştirir

def clear_order(): #listedeki bütün verileri temizler
    result = messagebox.askquestion("Adisyonu Temizle", "Emin misiniz?")
    if result == "yes":
        for item in order_tree.get_children():
            order_tree.delete(item)
        global total_price
        total_price = 0
        total_label.config(text="Toplam Ücret: 0 TL")
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, "1")  # Temizlendikten sonra default olarak 1 değerini yerleştirir

def increase_quantity(): #adet bölümünün yanında bulunan aşağı yukarı butonların (yukarı) butonudur adet değerini her basıldığında 1 arttırır
    current_value = int(quantity_entry.get())
    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(0, str(current_value + 1))

def decrease_quantity():#adet bölümünün yanında bulunan aşağı yukarı butonların (aşağı) butonudur adet değerini her basıldığında 1 azaltır
    current_value = int(quantity_entry.get())
    if current_value > 0:
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, str(current_value - 1))

def on_dropdown_select(*args): #dropdown menüyü manipüle eder
    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(0, "1")  # Seçildiğinde default olarak 1 değerini yerleştirir


#
#Arayüz düzenlemeleri
#

root = tk.Tk()
root.title("Adisyon Programı")
root.geometry("1200x400")

# Sol taraftaki ürünlerin listesi
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20)

products_label = tk.Label(left_frame, text="Ürünler")
products_label.pack()

product_option = tk.StringVar(root)
product_option.set(list(products.keys())[0])

product_dropdown = tk.OptionMenu(left_frame, product_option, *products.keys(), command=on_dropdown_select)
product_dropdown.pack()

quantity_label = tk.Label(left_frame, text="Adet")
quantity_label.pack()

quantity_frame = tk.Frame(left_frame)
quantity_frame.pack()

quantity_entry = tk.Entry(quantity_frame)
quantity_entry.pack(side=tk.LEFT)
quantity_entry.insert(0, "1")

increase_button = tk.Button(quantity_frame, text="▲", command=increase_quantity, width=3)
increase_button.pack(side=tk.LEFT)

decrease_button = tk.Button(quantity_frame, text="▼", command=decrease_quantity, width=3)
decrease_button.pack(side=tk.LEFT)

add_button = tk.Button(left_frame, text="Adisyona Ekle", command=add_to_order)
add_button.pack()


right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=20)

order_label = tk.Label(right_frame, text="Adisyon")
order_label.pack()

scroll_y = tk.Scrollbar(right_frame, orient="vertical")
order_tree = ttk.Treeview(right_frame, columns=("Ürün", "Adet", "Ücret", "Birim"), show="headings", yscrollcommand=scroll_y.set)
order_tree.heading("Ürün", text="Ürün")
order_tree.heading("Adet", text="Adet")
order_tree.heading("Ücret", text="Ücret")
order_tree.heading("Birim", text="Birim")
order_tree.pack(side=tk.LEFT)

scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_y.config(command=order_tree.yview)

total_label = tk.Label(right_frame, text="Toplam Ücret: 0 TL")
total_label.pack()

delete_button = tk.Button(right_frame, text="Sil", command=delete_selected)
delete_button.pack(side=tk.BOTTOM)

clear_button = tk.Button(right_frame, text="Temizle", command=clear_order)
clear_button.pack(side=tk.BOTTOM)

total_price = 0

root.mainloop()
