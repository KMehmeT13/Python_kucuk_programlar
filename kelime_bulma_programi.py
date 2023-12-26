import tkinter as tk
from tkinter import messagebox

def kelimeyi_bul(): #Aranılacak kelimeyi bulan fonksiyon
    cumle = metin_alani.get("1.0", "end-1c") #metin alanına yazılan veriyi cumle adlı değişkene atar
    aranan_kelime = aranan_kelime_alani.get()#aranılacak kelime alanına yazılan veriyi aranan kelime adlı değişkene atar
    
    if not cumle.strip(): #metin alanının dolu olup olmadığını kontrol eden fonksiyon
        messagebox.showinfo("Uyarı", "Metin alanı boş bırakılamaz!") #Metin alanı boş ise kullanıcıya verilen uyarı mesajı
        return

    if " " in aranan_kelime: #aranan kelime alanınında tek kelime olmasını kontrol eden fonksiyon
        messagebox.showinfo("Uyarı", "Aranılacak kelime boş bırakılamaz veya bir den fazla kelime yazılamaz lütfen tek bir kelime yazın!")#aranan kelime alanı boşluk kullanıldı ise kullanıcıya verilen uyarı mesajı
        return

    if not aranan_kelime: #aranılacak metin kutusu boş olup olmadığını kontrol eden fonksiyon
        messagebox.showinfo("Uyarı", "Aranacak kelimeyi yazmadan bulma işlemi yapılamaz!") #Aranılacak metin kutusu boş olmnası halinde kullanıcıya verilen hata mesajı
        return
    
    # Metin varsa işlemlere devam eder
    metin_alani.tag_remove("kelime", "1.0", "end")
    
    start = "1.0" #Döngünün metin kutusunun başında olması için 
    while start: #döngü başlıyor
        start = metin_alani.search(aranan_kelime, start, stopindex=tk.END) #döngünün nerede başladığını ve bittiğini gösterir
        if start: #kelimeyi arayan karar yapısı
            end = f"{start}+{len(aranan_kelime)}c"
            metin_alani.tag_add("kelime", start, end) 
            metin_alani.tag_config("kelime", foreground="red", underline=True)
            start = end

    kelime_sayisi = cumle.lower().count(aranan_kelime.lower()) #aranılan kelimenin kaç defa geçtiğini sayar
    sayac_etiket.config(text=f"'{aranan_kelime}' kelimesi cümle içinde {kelime_sayisi} kez geçiyor.") #aranılan kelimenin kaç defa geçtiğini gösteren parametreyi etikette gösterir

def temizle(): #temizle tuşuna basıldığında girilen bütün parametreleri ve sonuçları temizleyen fonksiyon
    confirm = messagebox.askyesno("Temizleme İşlemi", "Tüm metni temizlemek istediğinizden emin misiniz?")
    if confirm:
        metin_alani.delete("1.0", "end")
        aranan_kelime_alani.delete(0, "end")
        sayac_etiket.config(text="")
        aranan_kelime_alani.delete(0, tk.END)
        aranan_kelime_alani.insert(0, 'Aranılacak Kelimeyi Buraya yazın')
        aranan_kelime_alani.config(fg='grey') 
    else:
        messagebox.showinfo("İptal", "Temizleme işlemi iptal edildi.")

def Tiklama(event): #Aranılacak kelime textboxunda kullanıcıyı bilgilendirmek için verilen bilginin fonksiyonu (tıklanıldığı zaman bilgi mesajı kaybolur)
    if aranan_kelime_alani.get() == 'Aranılacak Kelimeyi Buraya yazın':
       aranan_kelime_alani.delete(0, tk.END)
       aranan_kelime_alani.insert(0, '')  
       aranan_kelime_alani.config(fg = 'black')  # 

root = tk.Tk()
root.title("Kelime Bulma Uygulaması")
root.geometry("800x600")

# Metin alanı ve scrollbar
metin_alani = tk.Text(root, height=30, width=50, wrap="word")
metin_alani.grid(row=0, column=0, padx=10, pady=10)
scrollbar = tk.Scrollbar(root, command=metin_alani.yview)
scrollbar.grid(row=0, column=1, sticky="NS")

metin_alani.config(yscrollcommand=scrollbar.set)

# Etiket oluştur
talimat_etiketi = tk.Label(root, text="Program Talimatı\n\n İçinde arama yapılacak metini yan tarafta \n bulunan kutuya yapıştırın veya  yazın. \n Ardından aşağıda bulunan ""Bul"" butonuna basın\n işleminiz bittiğinde temizle butonunu kullanarak\n sonuçları temizleyebilirsiniz. ")
talimat_etiketi.grid(row=0, column=2, padx=10)



aranan_kelime_alani = tk.Entry(root, width=30)
aranan_kelime_alani.grid(row=1, column=0, padx=(10, 0))  

#Aranılacak 
default_text = "Aranılacak Kelimeyi Buraya yazın"
aranan_kelime_alani = tk.Entry(root, width=30, fg='grey')
aranan_kelime_alani.insert(0, default_text)
aranan_kelime_alani.bind('<FocusIn>', Tiklama)
aranan_kelime_alani.grid(row=1, column=0, padx=(10, 0))  

# Bul butonu
bul_butonu = tk.Button(root, text="Bul", command=kelimeyi_bul)
bul_butonu.grid(row=1, column=1, padx=10)

# Kelime sayısı gösteren etiket
sayac_etiket = tk.Label(root, text="")
sayac_etiket.grid(row=2, column=0, columnspan=2, pady=10)

# Temizle butonu
temizle_butonu = tk.Button(root, text="Temizle", command=temizle)
temizle_butonu.grid(row=1, column=2, padx=10)

root.mainloop()
