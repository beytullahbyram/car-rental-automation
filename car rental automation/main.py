import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox  
import mysql.connector as SQLC
#veri tabanı baglantısını yaptık
mysqlConnect = mysql.connector.connect(
    user='root',             
    host='localhost',       
    passwd='deneme',         
    database='arac_kiralama')
print('-----')
print(mysqlConnect)
print('-----')
print('open')
mysqlConnect.close()
print('close')

class Otomasyon:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('500x500+450+100')
        self.window.title('Otomasyon Giriş')
        self.window.config(bg='blue')
        self.butonOlustur()
    #ana ekran acılıs butonları
    def butonOlustur(self):
        self.musteriKayıt=tk.Button(text='Müşteri Kayıt',height=4,width=10,command=self.musteriKayıtFonkiyon).grid(row=0,column=0,padx=30,pady=30)
        self.aracKayıt=tk.Button(text='Araç Kayıt',height=4,width=10,command=self.aracKayıtFonksiyon).grid(row=1,column=0,padx=30,pady=30)
        self.aracListele=tk.Button(text='Araç Kirala',height=4,width=10,command=self.kirala).grid(row=0,column=1,padx=30,pady=30)
        self.aracListele=tk.Button(text='Araçları Listele',height=4,width=10,command=self.listele).grid(row=1,column=1,padx=30,pady=30)
        
        self.cıkıs=tk.Button(text='Çıkış',height=2,width=10,command=self.girisEkranıCıkısBtn).grid(row=2,column=1,padx=25,pady=25)

        self.kelime_ara=tk.Button(text='KELİME ARA BUTONU',height=4,width=20,command=self.final).grid(row=0,column=3,padx=30,pady=30)

        Label(self.window,text='ARAÇ OTOMASYONU').grid(row=2,column=0,padx=25,pady=25)
    #ana ekran cıkıs butonu
    def girisEkranıCıkısBtn(self):
        self.window.destroy()


#-----------------------------------------------------------KELİME ARA BUTONU
    def final(self):
        pencere=tk.Tk()
        pencere.geometry('500x500+450+100')
        pencere.title('FİNAL ÖDEV')
        pencere.config(bg='DarkSeaGreen1')
        self.finalEntry=tk.Entry(pencere)
        self.finalEntry.pack()

        yazi=tk.Label(pencere)
        yazi.config(text="yukarıya sorguya uygun doldurunuz")
        yazi.pack()
        dugme=tk.Button(pencere)
        dugme.config(text="arayınız")
        dugme.config(command=self.kelimeara)
        dugme.pack()
       
#-----------------------------------------------------------FİNAL ARAMA FONKSİYONU
    def kelimeara(self):
        istenenKelime=self.finalEntry.get()
        #databasebaglandık
        mysqlConnect.connect()
        fiyatGetirSorgu = mysqlConnect.cursor()
        #databasedeki tcye göre arama sorgusu
        #sorguyu gönderdik
        fiyatGetirSorgu.execute("SELECT  * FROM arac_kiralama.musteriler  where TC=%s", (istenenKelime,))
        data = fiyatGetirSorgu.fetchall()
        mysqlConnect.close()
        print('istenilen arama sonucları : ')
        print(data)



#------------------------------------ MÜŞTERİ FONKSİYONLARI -------------------------1.BUTTON
    #müşterileri kayıt ettiğimiz fonksiyon
    def musteriKayıtFonkiyon(self):
        self.musteriKayıtEkranı=tk.Tk()
        self.musteriKayıtEkranı.geometry('480x520+600+100')
        self.musteriKayıtEkranı.title('MÜŞTERİ KAYIT')
        Label(self.musteriKayıtEkranı,text='TC').grid(row=0,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Ad Soyad').grid(row=1,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Telefon').grid(row=2,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Dogum Tarihi').grid(row=3,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Mail').grid(row=4,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Meslek').grid(row=5,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Ehliyet Sınıfı').grid(row=6,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Medeni Durum').grid(row=7,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Eğitim Durumu').grid(row=8,column=0,pady=15,padx=15)
        Label(self.musteriKayıtEkranı,text='Araç Kiraladımı').grid(row=9,column=0,pady=15,padx=15)


        self.tcEntry=tk.Entry(self.musteriKayıtEkranı)
        self.tcEntry.grid(row=0,column=1,pady=15,padx=15)

        self.adSoyadEntry=tk.Entry(self.musteriKayıtEkranı)
        self.adSoyadEntry.grid(row=1,column=1,pady=15,padx=15) 

        self.telefonEntry=tk.Entry(self.musteriKayıtEkranı)
        self.telefonEntry.grid(row=2,column=1,pady=15,padx=15)
        
        self.dogumTarihEntry=tk.Entry(self.musteriKayıtEkranı)
        self.dogumTarihEntry.grid(row=3,column=1,padx=15)
        
        self.mailEntry=tk.Entry(self.musteriKayıtEkranı)
        self.mailEntry.grid(row=4,column=1,pady=15,padx=15)
        
        self.MeslekEntry=tk.Entry(self.musteriKayıtEkranı)
        self.MeslekEntry.grid(row=5,column=1,pady=15,padx=15)

        self.EhliyetEntry=tk.Entry(self.musteriKayıtEkranı)
        self.EhliyetEntry.grid(row=6,column=1,pady=15,padx=15) 

        self.MedeniDurumEntry=tk.Entry(self.musteriKayıtEkranı)
        self.MedeniDurumEntry.grid(row=7,column=1,pady=15,padx=15) 
        
        self.EgitimDurumEntry=tk.Entry(self.musteriKayıtEkranı)
        self.EgitimDurumEntry.grid(row=8,column=1,pady=15,padx=15) 

        self.aracKiraladımıEntry=tk.Entry(self.musteriKayıtEkranı)
        self.aracKiraladımıEntry.grid(row=9,column=1,pady=15,padx=15)
    

        self.buton=tk.Button(self.musteriKayıtEkranı,text='Kaydet',command=self.ekleBtn)
        self.buton.grid(row=0,column=2,pady=15,padx=15)

        self.buton=tk.Button(self.musteriKayıtEkranı,text='Cıkış',command=self.musteriKayıtEkranıCıkısBtn)
        self.buton.grid(row=0,column=3,pady=15,padx=15)

        self.buton2=tk.Button(self.musteriKayıtEkranı,text='Listele',command=self.müsteriListele)
        self.buton2.grid(row=0,column=4,pady=15,padx=15)
    #müsterileri listeliyoruz
    def müsteriListele(self):
        self.musteriListele=tk.Tk()
        self.musteriListele.geometry('900x300+0+0')
        self.musteriListele.title('KAYITLI MÜŞTERİLER')

        self.musteriler=ttk.Treeview(self.musteriListele)
        self.musteriler["columns"]=("A","B","C","D","E","F","G","H","I","J")
        
        self.musteriler.column("#0",width=5)
        self.musteriler.column("A",width=90)
        self.musteriler.column("B",width=90)
        self.musteriler.column("C",width=90)
        self.musteriler.column("D",width=75)
        self.musteriler.column("E",width=75)
        self.musteriler.column("F",width=70)
        self.musteriler.column("G",width=70)
        self.musteriler.column("H",width=70)
        self.musteriler.column("I",width=70)
        self.musteriler.column("J",width=90)

        self.musteriler.heading("#0",text="0000")
        self.musteriler.heading("A",text="TC")
        self.musteriler.heading("B",text="AD SOYAD")
        self.musteriler.heading("C",text="TELEFON")
        self.musteriler.heading("D",text="DOGUM T.")
        self.musteriler.heading("E",text="MAIL")
        self.musteriler.heading("F",text="MESLEK")
        self.musteriler.heading("G",text="EHLİET")
        self.musteriler.heading("H",text="MEDENİ D.")
        self.musteriler.heading("I",text="EGİTİM D.")
        self.musteriler.heading("J",text="KIRA_DURUM")


        self.musteriler.grid(row=2,column=0,padx=7,pady=15)

        #veri tabanı baglantısını yaptık
        mysqlConnect.connect()
        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.musteriler")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            self.musteriler.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()
        mysqlConnect.connect()
    #müşterileri veri tabanına ekliyoruz...
    def ekleBtn(self):
        #veri tabanımıza baglandık
        mysqlConnect.connect()
        musteriBilgiGiris2 = mysqlConnect.cursor()
        sql = "INSERT INTO arac_kiralama.musteriler (TC, AD_SOYAD, TELEFON, DOGUM_TARIH, MAIL, MESLEK, EHLIYET, MEDENI_DURUMU, EGITIM_DURUMU,KIRA_DURUM) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
        val = (self.tcEntry.get(),self.adSoyadEntry.get(),self.telefonEntry.get(),self.dogumTarihEntry.get(),self.mailEntry.get(),self.MeslekEntry.get(),self.EhliyetEntry.get(),self.MedeniDurumEntry.get(),self.EgitimDurumEntry.get(),self.aracKiraladımıEntry.get())
        musteriBilgiGiris2.execute(sql, val)
        mysqlConnect.commit()
        print(musteriBilgiGiris2.rowcount, "Ayrıntılar eklendi")
        mysqlConnect.close()
        self.musteriEntryTemizle()
    #müşteri kayıt ekranından cıkıs yapmak için     
    def musteriKayıtEkranıCıkısBtn(self):    
        self.musteriKayıtEkranı.destroy()
    #kayıt yaptıktan sonra entryleri temizler
    def musteriEntryTemizle(self):
        self.tcEntry.delete(0, 'end')  
        self.adSoyadEntry.delete(0, 'end')  
        self.telefonEntry.delete(0, 'end')  
        self.dogumTarihEntry.delete(0, 'end')  
        self.mailEntry.delete(0, 'end')  
        self.MeslekEntry.delete(0, 'end') 
        self.EhliyetEntry.delete(0, 'end') 
        self.MedeniDurumEntry.delete(0, 'end') 
        self.EgitimDurumEntry.delete(0, 'end')
        self.aracKiraladımıEntry.delete(0, 'end')
        

#------------------------------------ARAÇ FONKSİYONLARI-----------------------------2.BUTTON
    #araçları kayıt ettiğimiz fonksiyon
    def aracKayıtFonksiyon(self):

        self.aracKayıtEkranı=tk.Tk()
        self.aracKayıtEkranı.geometry('700x520+600+100')
        self.aracKayıtEkranı.title('ARAÇ KAYIT')
        labelframe = tk.LabelFrame(self.aracKayıtEkranı, text="ARAÇ BİLGİLERİ")
        labelframe.grid(row=0,column=0,pady=15,padx=15)
        Label(labelframe,text='Araç türü').grid(row=0,column=0,pady=15,padx=15)
        Label(labelframe,text='Marka').grid(row=1,column=0,pady=15,padx=15)
        Label(labelframe,text='Model').grid(row=2,column=0,pady=15,padx=15)
        Label(labelframe,text='Yıl').grid(row=3,column=0,pady=15,padx=15)
        Label(labelframe,text='Uretim Modeli').grid(row=4,column=0,pady=15,padx=15)
        Label(labelframe,text='Yakıt').grid(row=5,column=0,pady=15,padx=15)
        Label(labelframe,text='Vites').grid(row=6,column=0,pady=15,padx=15)
        Label(labelframe,text='Motor Gücü').grid(row=7,column=0,pady=15,padx=15)
        Label(labelframe,text='Motor Hacmi').grid(row=8,column=0,pady=15,padx=15)
        Label(labelframe,text='Motor No').grid(row=0,column=2,pady=15,padx=15)
        Label(labelframe,text='Kasa Tipi').grid(row=1,column=2,pady=15,padx=15)
        Label(labelframe,text='Çekiş').grid(row=2,column=2,pady=15,padx=15)
        Label(labelframe,text='Kapı').grid(row=3,column=2,pady=15,padx=15)
        Label(labelframe,text='Renk').grid(row=4,column=2,pady=15,padx=15)
        Label(labelframe,text='Şasi No').grid(row=5,column=2,pady=15,padx=15)
        Label(labelframe,text='Günlük Fiyatı').grid(row=6,column=2,pady=15,padx=15)
        Label(labelframe,text='Kirada mı?').grid(row=7,column=2,pady=15,padx=15)
        Label(labelframe,text='Kullanım Dışı mı?').grid(row=8,column=2,pady=15,padx=15) 
        
        self.AracTuruEntry=tk.Entry(labelframe)
        self.AracTuruEntry.grid(row=0,column=1,pady=15,padx=15)

        
        self.MarkaEntry=tk.Entry(labelframe)
        self.MarkaEntry.grid(row=1,column=1,pady=15,padx=15)
        self.ModelEntry=tk.Entry(labelframe)
        self.ModelEntry.grid(row=2,column=1,pady=15,padx=15)
        self.yılEntry=tk.Entry(labelframe)
        self.yılEntry.grid(row=3,column=1,pady=15,padx=15)
        self.uretimModeliEntry=tk.Entry(labelframe)
        self.uretimModeliEntry.grid(row=4,column=1,pady=15,padx=15)
        self.yakıtList = ["Benzin", "Elektirikli", "LPG","Mazot"]
        self.yakıt= ttk.Combobox(labelframe,values=self.yakıtList)
        self.yakıt.grid(row=5,column=1,pady=15,padx=15)
        self.vitesList = ["Otomatik", "Düz"]
        self.vites= ttk.Combobox(labelframe,values=self.vitesList)
        self.vites.grid(row=6,column=1,pady=15,padx=15)
        self.motorGücüEntry=tk.Entry(labelframe)
        self.motorGücüEntry.grid(row=7,column=1,pady=15,padx=15)
        self.motorHacmiEntry=tk.Entry(labelframe)
        self.motorHacmiEntry.grid(row=8,column=1,pady=15,padx=15)
        self.motorNoEntry=tk.Entry(labelframe)
        self.motorNoEntry.grid(row=0,column=4,pady=15,padx=15)
        self.kasaTipiList = ["Sedan", "Hatchback", "Station Wagon","Coupe", "CUV","Pick Up"]
        self.kasaTipi= ttk.Combobox(labelframe,values=self.kasaTipiList)
        self.kasaTipi.grid(row=1,column=4,pady=15,padx=15)
        self.cekisList = ["Önden", "Arkadan", "İki tekerlekten ","Dört tekerlekten ", "Altı tekerlekten"]
        self.cekis= ttk.Combobox(labelframe,values=self.cekisList)
        self.cekis.grid(row=2,column=4,pady=15,padx=15)
        self.kapıEntry=tk.Entry(labelframe)
        self.kapıEntry.grid(row=3,column=4,pady=15,padx=15)
        self.renkEntry=tk.Entry(labelframe)
        self.renkEntry.grid(row=4,column=4,pady=15,padx=15)
        self.sasiEntry=tk.Entry(labelframe)
        self.sasiEntry.grid(row=5,column=4,pady=15,padx=15)
        self.gunlukFiyatEntry=tk.Entry(labelframe)
        self.gunlukFiyatEntry.grid(row=6,column=4,pady=15,padx=15)
        self.kiradamıEntry=tk.Entry(labelframe)
        self.kiradamıEntry.grid(row=7,column=4,pady=15,padx=15)
        self.kullanımDısımıEntry=tk.Entry(labelframe)
        self.kullanımDısımıEntry.grid(row=8,column=4,pady=15,padx=15)

        self.cıkısBtn=tk.Button(labelframe,text='ÇIKIŞ',command=self.aracKayıtEkranıCıkısBtn)
        self.cıkısBtn.grid(row=0,column=5,pady=15,padx=15)

        self.kayıtBtn=tk.Button(labelframe,text='KAYIT',command=self.aracKayıtEkranıDB)
        self.kayıtBtn.grid(row=1,column=5,pady=15,padx=15)
        
        self.listelebuton=tk.Button(labelframe,text='LİSTELE',command=self.kayıtlıAraclarıListele)
        self.listelebuton.grid(row=2,column=5,pady=15,padx=15)
    #aracları veri tabanına eklediğimiz fonksiyon
    def aracKayıtEkranıDB(self):
        mysqlConnect.connect()
        print('veri tabanı acıldı')
        aracBilgiGiris = mysqlConnect.cursor()
        sql = "INSERT INTO aracbilgi (aracTur, marka, model, yıl, uretimModeli, yakıt, vites, motorGucu, motorHacmi, motorNo, kasaTip, cekis, kapi, renk, sasiNo, gunlukFiyat, kiradaMi, kullanimDisiMi) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.AracTuruEntry.get(), self.MarkaEntry.get(), self.ModelEntry.get(), self.yılEntry.get(),self.uretimModeliEntry.get(),self.yakıt.get(),self.vites.get(),self.motorGücüEntry.get(),self.motorHacmiEntry.get(),self.motorNoEntry.get(),self.kasaTipi.get(),self.cekis.get(),self.kapıEntry.get(),self.renkEntry.get(),self.sasiEntry.get(),self.gunlukFiyatEntry.get(),self.kiradamıEntry.get(),self.kullanımDısımıEntry.get())
        aracBilgiGiris.execute(sql, val)
        mysqlConnect.commit()
        print(aracBilgiGiris.rowcount, "Ayrıntılar eklendi")
        mysqlConnect.close()
        self.aracEntryTemizle()
    #araç kayıt ekranından çıkış yapıyoruz...
    def aracKayıtEkranıCıkısBtn(self):
        self.aracKayıtEkranı.destroy()
    #aracları listeliyoruz
    def kayıtlıAraclarıListele(self):
        self.aracListelemeEkranı=tk.Tk()
        self.aracListelemeEkranı.geometry('1300x500+0+400')
        self.aracListelemeEkranı.title('ARAÇLAR')

        self.araclar=ttk.Treeview(self.aracListelemeEkranı)
        self.araclar["columns"]=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S",)
        self.araclar.column("#0",width=5)
        self.araclar.column("A",width=65)
        self.araclar.column("B",width=65)
        self.araclar.column("C",width=65)
        self.araclar.column("D",width=55)
        self.araclar.column("E",width=60)
        self.araclar.column("F",width=60)
        self.araclar.column("G",width=60)
        self.araclar.column("H",width=60)
        self.araclar.column("I",width=60)
        self.araclar.column("J",width=60)
        self.araclar.column("K",width=60)
        self.araclar.column("L",width=60)
        self.araclar.column("M",width=50)
        self.araclar.column("N",width=60)
        self.araclar.column("O",width=70)
        self.araclar.column("P",width=70)
        self.araclar.column("R",width=70)
        self.araclar.column("S",width=130)

        self.araclar.heading("#0",text="0000")
        self.araclar.heading("A",text="TÜR")
        self.araclar.heading("B",text="MARKA")
        self.araclar.heading("C",text="MODEL")
        self.araclar.heading("D",text="YIL")
        self.araclar.heading("E",text="Ü.MODEL")
        self.araclar.heading("F",text="YAKIT")
        self.araclar.heading("G",text="VİTES")
        self.araclar.heading("H",text="GÜÇ")
        self.araclar.heading("I",text="HACİM")
        self.araclar.heading("J",text="M.NO")
        self.araclar.heading("K",text="KASA")
        self.araclar.heading("L",text="ÇEKİŞ")
        self.araclar.heading("M",text="KAPI")
        self.araclar.heading("N",text="RENK")
        self.araclar.heading("O",text="ŞASİ")
        self.araclar.heading("P",text="FİYAT")
        self.araclar.heading("R",text="KİRADA MI")
        self.araclar.heading("S",text="KULLANIM DIŞI MI")
        self.araclar.grid(row=0,column=0)
        #veri tabanı baglantısını yaptık
        mysqlConnect.connect()
        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.aracbilgi")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            self.araclar.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()
    #kayıt yaptıktan sonra entryleri temizler
    def aracEntryTemizle(self):
        self.AracTuruEntry.delete(0,'end')
        self.MarkaEntry.delete(0, 'end')  
        self.ModelEntry.delete(0, 'end')  
        self.yılEntry.delete(0, 'end')  
        self.uretimModeliEntry.delete(0, 'end')  
        self.yakıt.delete(0, 'end')  
        self.vites.delete(0, 'end') 
        self.motorGücüEntry.delete(0, 'end') 
        self.motorHacmiEntry.delete(0, 'end') 
        self.motorNoEntry.delete(0, 'end')
        self.kasaTipi.delete(0, 'end')
        self.cekis.delete(0, 'end')
        self.kapıEntry.delete(0, 'end')
        self.renkEntry.delete(0, 'end')
        self.sasiEntry.delete(0, 'end')
        self.gunlukFiyatEntry.delete(0, 'end')
        self.kiradamıEntry.delete(0, 'end')
        self.kullanımDısımıEntry.delete(0, 'end')

#-------------------------------------ARACI KİRALIYORUZ-------------------------3.BUTTON
    def kirala(self):
        self.KiralaEkran=tk.Tk()
        self.KiralaEkran.geometry('1500x600+0+0')
        self.KiralaEkran.title('ARAÇ KİRALAMA')
        kayıtlıEkran = tk.Frame(self.KiralaEkran, bg="seashell2", width=750, height=600)
        kayıtlıEkran.pack(fill=tk.BOTH,side = LEFT)

        kiralamaEkran = tk.Frame(self.KiralaEkran, bg="seashell2", width=750, height=600)
        kiralamaEkran.pack(fill=tk.BOTH, expand=1,side = RIGHT)

        labelframe = tk.LabelFrame(kayıtlıEkran, text="MÜŞTERİ KAYIT TABLOSU",border=6,bg='DarkSeaGreen',labelanchor=N,font=('Bahnschrift 11'))
        labelframe.grid(row=0,column=0,pady=10,padx=7)
        

        self.musteriTablo=ttk.Treeview(labelframe)
        self.musteriTablo["columns"]=("A","B","C","D","E","F","G","H","I","J")
        
        self.musteriTablo.column("#0",width=5)
        self.musteriTablo.column("A",width=90)
        self.musteriTablo.column("B",width=90)
        self.musteriTablo.column("C",width=90)
        self.musteriTablo.column("D",width=75)
        self.musteriTablo.column("E",width=75)
        self.musteriTablo.column("F",width=70)
        self.musteriTablo.column("G",width=65)
        self.musteriTablo.column("H",width=70)
        self.musteriTablo.column("I",width=70)
        self.musteriTablo.column("J",width=90)

        self.musteriTablo.heading("#0",text="0000")
        self.musteriTablo.heading("A",text="TC")
        self.musteriTablo.heading("B",text="AD SOYAD")
        self.musteriTablo.heading("C",text="TELEFON")
        self.musteriTablo.heading("D",text="DOGUM T.")
        self.musteriTablo.heading("E",text="MAIL")
        self.musteriTablo.heading("F",text="MESLEK")
        self.musteriTablo.heading("G",text="EHLİET")
        self.musteriTablo.heading("H",text="MEDENİ D.")
        self.musteriTablo.heading("I",text="EGİTİM D.")
        self.musteriTablo.heading("J",text="KIRA_DURUM")


        self.musteriTablo.grid(row=2,column=0,padx=7,pady=15)

        sb = tk.Scrollbar(kayıtlıEkran, orient=VERTICAL,width=13)
        sb.grid(row=0,column=2,sticky='nse')

        self.musteriTablo.config(yscrollcommand=sb.set)
        sb.config(command=self.musteriTablo.yview)
        deneme=tk.Entry(kiralamaEkran)
        deneme.grid(row=0,column=0)

        self.musteriListeleBtn=tk.Button(kayıtlıEkran, 
        text="LİSTELE", 
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.ekle)

        self.secBtn=tk.Button(kayıtlıEkran, 
        text="SEÇ", 
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.sec)

        self.musteriListeleBtn.grid(row=0,column=1,padx=1,pady=1)
        self.secBtn.grid(row=0,column=2,padx=1,pady=1)

        labelframe2 = tk.LabelFrame(kayıtlıEkran, text="ARAÇLAR",border=6,bg='DarkSeaGreen',labelanchor=N,font=('Bahnschrift 11'))
        labelframe2.grid(row=3,column=0,pady=7,padx=7)
        
        aracListele=tk.Button(labelframe2,
        text='ARAÇLARI LİSTELE',
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.aracListeleFonksiyon)
        aracListele.grid(row=3,column=2,padx=20,pady=20)

        Label(kayıtlıEkran,text="MÜŞTERİ VE ARACI SEÇİN SONRA SASE KONTROL TIKLAYIN FİYATI GELSİN",bg='DarkSeaGreen').grid(row=4,column=0)
        Label(kayıtlıEkran,text="SONRA TARİH VE YOLCULUK GİRİN VE KAC GÜN KİRALANACAK ONU GİRİN",bg='DarkSeaGreen').grid(row=5,column=0)
        Label(kayıtlıEkran,text="BU ADIMLARDAN SONRA EN SON FİYAT HESAPLADIKTAN SONRA ARACI KİRALAYABİLİRSİNİZ",bg='DarkSeaGreen').grid(row=6,column=0)
        Label(kayıtlıEkran,text="KİRALDIKTAN SONRA GEREKLİ TABLOLARA ARAC KİRA DURUMLARI GÜNCELLENECEKTİR... ",bg='DarkSeaGreen').grid(row=6,column=0)
        
        kiralamaEkranFrame = tk.LabelFrame(kiralamaEkran, text="KİRALAMA BİLGİLERİ",border=6,bg='seashell2',labelanchor=N,font=('Bahnschrift 11'))
        kiralamaEkranFrame.grid(row=0,column=0,pady=2,padx=2)

        Label(kiralamaEkranFrame,text="Müşteri Tc:",bg='seashell2').grid(row=0,column=0,pady=2,padx=2)
        self.musteriTcEntry=tk.Entry(kiralamaEkranFrame)
        self.musteriTcEntry.grid(row=1,column=0,pady=7,padx=7)

        Label(kiralamaEkranFrame,text="Arac Şase No:",bg='seashell2').grid(row=0,column=1,pady=2,padx=2)
        self.aracSasiEntry=tk.Entry(kiralamaEkranFrame)
        self.aracSasiEntry.grid(row=1,column=1,pady=10,padx=10)
        saseKontrolBtn=tk.Button(kiralamaEkranFrame,text='Şase Kontrol',borderwidth=3, relief="groove",padx=1, pady=1,bg='DarkSeaGreen',font=('Bahnschrift 9'),command=self.fiyatıGetir)
        saseKontrolBtn.grid(row=1,column=2,padx=2,pady=2)

        Label(kiralamaEkranFrame,text="Kiralama Tarihi:",bg='seashell2').grid(row=2,column=0,pady=2,padx=2)
        self.kiralamaTarihiEntry=DateEntry(kiralamaEkranFrame, date_pattern='y/mm/dd')
        self.kiralamaTarihiEntry.grid(row=3,column=0,padx=10,pady=10)
        
        Label(kiralamaEkranFrame,text="Teslim Tarihi",bg='seashell2').grid(row=2,column=1,pady=2,padx=2)
        self.teslimTarihiEntry=DateEntry(kiralamaEkranFrame, date_pattern='y/mm/dd')
        self.teslimTarihiEntry.grid(row=3,column=1,padx=10,pady=10)

        Label(kiralamaEkranFrame,text="Yolculuk:",bg='seashell2').grid(row=4,column=1,pady=2,padx=2)
        self.yolculuk=tk.Entry(kiralamaEkranFrame)
        self.yolculuk.grid(row=5,column=1,padx=10,pady=10)

        Label(kiralamaEkranFrame,text="Kaç Gün Kiralanacak:",bg='seashell2').grid(row=6,column=0,pady=4,padx=2)
        self.kiralamaGunu=tk.Entry(kiralamaEkranFrame)
        self.kiralamaGunu.grid(row=7,column=0,padx=10,pady=10)

        Label(kiralamaEkranFrame,text="Fiyat:",bg='seashell2').grid(row=6,column=1,pady=4,padx=2)
        self.ucret=tk.Entry(kiralamaEkranFrame)
        self.ucret.grid(row=7,column=1,padx=10,pady=10)

        self.aracıKiralaBtn=tk.Button(kiralamaEkran,text='ARACI KİRALA',borderwidth=4, relief="groove",padx=4, pady=4,bg='DarkSeaGreen',font=('Bahnschrift 12'),command=self.aracıKirala)
        self.aracıKiralaBtn.grid(row=5,column=0,padx=10,pady=10)

        self.hesaplaBtn=tk.Button(kiralamaEkranFrame,text='Hesapla',borderwidth=3, relief="groove",padx=1, pady=1,bg='DarkSeaGreen',font=('Bahnschrift 9'),command=self.hesapla)
        self.hesaplaBtn.grid(row=7,column=2,padx=10,pady=10)

        Label(kiralamaEkranFrame,text="TOPLAM FİYAT",bg='seashell2').grid(row=8,column=0,pady=4,padx=2)
        self.sonuc=tk.Entry(kiralamaEkranFrame,bg='seashell2')
        self.sonuc.grid(row=8,column=1,pady=4,padx=2)
    #aracın kiralama bedelini hesaplayan fonksiyon
    def hesapla(self):
        self.toplamUcret=(int(self.ucret.get()) * int(self.kiralamaGunu.get()))
        print(self.toplamUcret)
        self.sonuc.insert(0,str(self.toplamUcret))
    #müşteriye aracı kiralıyoruz...
    def aracıKirala(self):
        value=self.musteriTcEntry.get()
        mysqlConnect.connect()
        fiyatGetirSorgu = mysqlConnect.cursor()
        fiyatGetirSorgu.execute("SELECT KIRA_DURUM FROM arac_kiralama.musteriler  where TC=%s", (value,))
        data = fiyatGetirSorgu.fetchall()
        mysqlConnect.close()
        print(data)
        if data == [('hayır',)]:
            #müşteriye aracı kiraladıgımız fonksiyon
            mysqlConnect.connect()
            kiralananAracBilgileri = mysqlConnect.cursor()
            sql = "INSERT INTO arac_kiralama.kiralananaraclar (musteriTC, aracSasi, kiralamaTarihi, teslimTarihi,ucret, yolculuk)VALUES (%s,%s,%s, %s, %s, %s)"
            val = (self.musteriTcEntry.get(),self.aracSasiEntry.get(),self.kiralamaTarihiEntry.get(),self.teslimTarihiEntry.get(),self.toplamUcret,self.yolculuk.get())
            kiralananAracBilgileri.execute(sql, val)
            mysqlConnect.commit()
            print(kiralananAracBilgileri.rowcount, "Ayrıntılar eklendi")


            #BURADA ARACI KİRALADIKTAN SONRA SECİLEN ARACIN KİRA DURUMUNU EVET YAPIYOR CÜNKÜ O ARACI O AN KİRALADIK
            aracDurumGuncelle=mysqlConnect.cursor()
            val2=(self.aracSasiEntry.get())
            aracDurumGuncelle.execute("UPDATE aracbilgi SET kiradaMi='evet' WHERE sasiNo=%s", (val2,))
            mysqlConnect.commit()
            
            #müşteri kiralık arac durumunu güncellemek
            aracDurumGuncelle=mysqlConnect.cursor()
            val3=(self.musteriTcEntry.get())
            aracDurumGuncelle.execute("UPDATE musteriler SET KIRA_DURUM='evet' WHERE TC=%s", (val3,))
            mysqlConnect.commit()
            
            self.musteriTablo.delete(*self.musteriTablo.get_children())
            mycursor = mysqlConnect.cursor()
            mycursor.execute("SELECT * FROM arac_kiralama.musteriler")
            myresult = mycursor.fetchall()
            self.y=0
            for x in myresult:
                self.musteriTablo.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
            mysqlConnect.close()

        else:
            messagebox.showerror('DİKKAT','BU MÜŞTERİDE ZATEN BİR ARAÇ KİRALANDI')
    #seçilen aracın şaseno'sunu kontrol ederek bize fiyatını getiriyor
    def fiyatıGetir(self):
        #ŞASE NUMARASI
        sasi=self.aracSasiEntry.get()
        print(sasi)
        mysqlConnect.connect()
        fiyatGetirSorgu = mysqlConnect.cursor()
        val = (self.aracSasiEntry.get())
        fiyatGetirSorgu.execute("SELECT gunlukFiyat FROM arac_kiralama.aracbilgi where sasiNo=%s", (val,))
        data = fiyatGetirSorgu.fetchall()
        print(data)
        self.ucret.insert(END, data)
        print(self.ucret.get())
    #veri tabanındaki aracları Treeview'e getirdiğimiz fonksiyon
    def aracListeleFonksiyon(self):
            aracListeleEkran=tk.Tk()
            aracListeleEkran.geometry('1300x500+0+400')
            aracListeleEkran.title('ARAÇ LİSTESİ')
            aracListeleEkran.config( bg="seashell2")
            
            labelframe2 = tk.LabelFrame(aracListeleEkran, text="ARAÇLAR",border=6,bg='DarkSeaGreen',labelanchor=N,font=('Bahnschrift 11'))
            labelframe2.grid(row=0,column=0,pady=7,padx=7)
            
            self.aracTablo=ttk.Treeview(labelframe2)
            self.aracTablo["columns"]=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S",)
            self.aracTablo.column("#0",width=5)
            self.aracTablo.column("A",width=65)
            self.aracTablo.column("B",width=65)
            self.aracTablo.column("C",width=65)
            self.aracTablo.column("D",width=55)
            self.aracTablo.column("E",width=60)
            self.aracTablo.column("F",width=60)
            self.aracTablo.column("G",width=60)
            self.aracTablo.column("H",width=60)
            self.aracTablo.column("I",width=60)
            self.aracTablo.column("J",width=60)
            self.aracTablo.column("K",width=60)
            self.aracTablo.column("L",width=60)
            self.aracTablo.column("M",width=50)
            self.aracTablo.column("N",width=60)
            self.aracTablo.column("O",width=70)
            self.aracTablo.column("P",width=70)
            self.aracTablo.column("R",width=70)
            self.aracTablo.column("S",width=130)

            self.aracTablo.heading("#0",text="0000")
            self.aracTablo.heading("A",text="TÜR")
            self.aracTablo.heading("B",text="MARKA")
            self.aracTablo.heading("C",text="MODEL")
            self.aracTablo.heading("D",text="YIL")
            self.aracTablo.heading("E",text="Ü.MODEL")
            self.aracTablo.heading("F",text="YAKIT")
            self.aracTablo.heading("G",text="VİTES")
            self.aracTablo.heading("H",text="GÜÇ")
            self.aracTablo.heading("I",text="HACİM")
            self.aracTablo.heading("J",text="M.NO")
            self.aracTablo.heading("K",text="KASA")
            self.aracTablo.heading("L",text="ÇEKİŞ")
            self.aracTablo.heading("M",text="KAPI")
            self.aracTablo.heading("N",text="RENK")
            self.aracTablo.heading("O",text="ŞASİ")
            self.aracTablo.heading("P",text="FİYAT")
            self.aracTablo.heading("R",text="KİRADA MI")
            self.aracTablo.heading("S",text="KULLANIM DIŞI MI")

            sb = tk.Scrollbar(aracListeleEkran, orient=VERTICAL,width=13)
            sb.grid(row=0,column=1,sticky='nse')

            self.aracTablo.configure(yscrollcommand=sb.set)
            sb.configure(command=self.aracTablo.yview)

            self.aracTablo.grid(row=0,column=0,padx=7,pady=7)
            
            #veri tabanımıza baglandık
            mysqlConnect.connect()
            mycursor = mysqlConnect.cursor()
            mycursor.execute("SELECT * FROM arac_kiralama.aracbilgi")
            myresult = mycursor.fetchall()
            self.y=0
            for x in myresult:
                print(x)
                # if x ==('TURKLER'):
                #     print(x)
                self.aracTablo.insert('','end',text=self.y,values=(x))
                self.y=self.y+1
            mysqlConnect.close()

            aracSaseSecBtn=tk.Button(aracListeleEkran,text='SEÇ',borderwidth=3, relief="groove",padx=1, pady=1,bg='DarkSeaGreen',font=('Bahnschrift 9'),command=self.aracSec)
            aracSaseSecBtn.grid(row=0,column=1,padx=5,pady=5)
    #müşteriler listeleniyor
    def ekle(self):
        #veri tabanı baglantısını yaptık
        mysqlConnect.connect()
        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.musteriler")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            self.musteriTablo.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()
        mysqlConnect.connect()
        print('sssss')
        mysqlConnect.close()
    #musteriyi secip sağdaki ekrana tc'sini aktarıyoruz 
    def sec(self):
        selected = self.musteriTablo.focus()
        values = self.musteriTablo.item(selected, 'values')
        self.musteriTcEntry.insert(0, values[0])
    #arabayı secip sağdaki ekrana saseno'sunu aktarıyoruz 
    def aracSec(self):
        selected = self.aracTablo.focus()
        values = self.aracTablo.item(selected, 'values')
        self.aracSasiEntry.insert(0, values[14])        
#------------------------------------KİRALANAN ARACLAR-------------------------4.BUTTON
    #kiralanan araclar veri tabanından cekilerek listeleniyor
    def listele(self):
        self.kiralikAracListeleWindow=tk.Tk()
        self.kiralikAracListeleWindow.geometry('1500x350+0+0')
        self.kiralikAracListeleWindow.title('KİRALANAN ARAÇLARIN BİLGİLERİ')
        self.kiralikAracListeleWindow.configure(bg='seashell2')

        kiralıkAracFrame=tk.Frame(self.kiralikAracListeleWindow,height=350,width=700,bg='seashell2')
        kiralıkAracFrame.grid(row=0,column=0,padx=4,pady=4)

        butonFrame=tk.Frame(self.kiralikAracListeleWindow,height=350,width=800,bg='seashell2')
        butonFrame.grid(row=0,column=1)  


        labelframe = tk.LabelFrame(kiralıkAracFrame, text="KİRALIK ARAÇLAR TABLOSU",border=6,bg='DarkSeaGreen',labelanchor=N,font=('Bahnschrift 11'))
        labelframe.grid(row=0,column=0,pady=4,padx=4)

        self.kiralikAraclar=ttk.Treeview(labelframe)
        self.kiralikAraclar["columns"]=("A","B","C","D","F","G")
        
        self.kiralikAraclar.column("#0",width=5)
        self.kiralikAraclar.column("A",width=90)
        self.kiralikAraclar.column("B",width=90)
        self.kiralikAraclar.column("C",width=90)
        self.kiralikAraclar.column("D",width=90)
        self.kiralikAraclar.column("F",width=90)
        self.kiralikAraclar.column("G",width=90)


        self.kiralikAraclar.heading("#0",text="")
        self.kiralikAraclar.heading("A",text="TC")
        self.kiralikAraclar.heading("B",text="ŞASE NO")
        self.kiralikAraclar.heading("C",text="KİRALAMA T.")
        self.kiralikAraclar.heading("D",text="TESLİM T.")
        self.kiralikAraclar.heading("F",text="FİYAT")
        self.kiralikAraclar.heading("G",text="YOLCULUK")
        self.kiralikAraclar.grid(row=1,column=0,padx=4,pady=4)

        sb = tk.Scrollbar(kiralıkAracFrame, orient=VERTICAL,width=13)
        sb.grid(row=0,column=1,sticky='nse')

        self.kiralikAraclar.config(yscrollcommand=sb.set)
        sb.config(command=self.kiralikAraclar.yview)

        #veri tabanımıza baglanıp bir önceki sayfada kiralanan aracları listeleyeceğiz
        mysqlConnect.connect()
        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.kiralananaraclar")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            self.kiralikAraclar.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()

        sec=tk.Button(butonFrame,
        text='SEÇ',
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.kiralıkAracSecBtn
        )
        sec.grid(row=0,column=0,padx=4,pady=4)

        Label(butonFrame,text="TC",bg='seashell2').grid(row=0,column=1,pady=3,padx=3)

        self.secBtn1=tk.Entry(butonFrame)
        self.secBtn1.grid(row=1,column=1,padx=4,pady=4)

        Label(butonFrame,text="ŞASE NO",bg='seashell2').grid(row=0,column=2,pady=3,padx=3)
        self.secBtn2=tk.Entry(butonFrame)
        self.secBtn2.grid(row=1,column=2,padx=4,pady=4)

        Label(butonFrame,text="KİRALAMA T.",bg='seashell2').grid(row=2,column=1,pady=3,padx=3)
        self.secBtn3=DateEntry(butonFrame, date_pattern='y/mm/dd')
        self.secBtn3.grid(row=3,column=1,padx=4,pady=4)
        
        Label(butonFrame,text="TESLİM T.",bg='seashell2').grid(row=2,column=2,pady=3,padx=3)
        self.secBtn4=DateEntry(butonFrame, date_pattern='y/mm/dd',)
        self.secBtn4.grid(row=3,column=2,padx=4,pady=4)



        Label(butonFrame,text="FİYAT",bg='seashell2').grid(row=4,column=2,pady=3,padx=3)
        self.secBtn6=tk.Entry(butonFrame)
        self.secBtn6.grid(row=5,column=2,padx=4,pady=4)

        Label(butonFrame,text="YOLCULUK",bg='seashell2').grid(row=4,column=1,pady=3,padx=3)
        self.secBtn7=tk.Entry(butonFrame)
        self.secBtn7.grid(row=5,column=1,padx=4,pady=4)

        Label(butonFrame,text="İŞLEMLERİ YAPMADAN ÖNCE \n VERİYİ SEÇEREK ENTRYE GETİRİN",bg='DarkSeaGreen').grid(row=0,column=3)
        Label(butonFrame,text="ARAÇ TESLİM EDİLDİYSE SEÇ>TESLİM\n EDİLDİ BUTONLARINA BASIN",bg='DarkSeaGreen').grid(row=1,column=3)
        Label(butonFrame,text="İŞLEMLERİ YAPARKEN ENTRYLERİN BOŞ\n OLDUGUNA DİKKAT EDİN",bg='DarkSeaGreen').grid(row=2,column=3)
        Label(butonFrame,text="ARAÇ TESLİM EDİLDİKTEN SONRA ARACIN\n VE MÜSTERİNİN ARAC KİRALAMA İLE İLGİLİ BİLGİLERİNİ",bg='DarkSeaGreen').grid(row=3,column=3)
        Label(butonFrame,text="3.BUTONDAN TABLOLARA BAKARAK \nİNCELEYEBİLİRSİNİZ",bg='DarkSeaGreen').grid(row=4,column=3)
        Label(butonFrame,text="MÜŞTERİ BİR ARACI KİRALADIYSA İF \nİLE KONTROL EDİLDİĞİ İÇİN BASKA BİR ",bg='DarkSeaGreen').grid(row=5,column=3)
        Label(butonFrame,text="ARAC KİRALAYAMAZ... ",bg='DarkSeaGreen').grid(row=6,column=3)

        guncelle=tk.Button(butonFrame,
        text='GÜNCELLE',
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.kiralıkAracGuncelleBtn
        )
        guncelle.grid(row=1,column=0,padx=4,pady=4)

        sil=tk.Button(butonFrame,
        text='SİL',
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.kiralıkAracSilBtn
        )
        sil.grid(row=2,column=0,padx=4,pady=4)

        temizle=tk.Button(butonFrame,
        text='TEMİZLE',
        borderwidth=3, 
        relief="groove",padx=5, pady=10,
        bg='DarkSeaGreen',
        font=('Bahnschrift 10'),
        command=self.entryTemizle
        )
        temizle.grid(row=3,column=0,padx=4,pady=4)
        
        teslimedildiBtn=tk.Button(butonFrame,
        text='TESLİM EDİLDİ',
        borderwidth=3, 
        relief="groove",padx=4, pady=5,
        bg='DarkSeaGreen',
        font=('Bahnschrift 9'),
        command=self.teslimEdildi
        )
        teslimedildiBtn.grid(row=4,column=0,padx=4,pady=4)
    #kiralık aracı secip entrylere aktarıyoruz
    def kiralıkAracSecBtn(self):
        self.secBtn3.delete(0, 'end')
        self.secBtn4.delete(0, 'end')
        selected = self.kiralikAraclar.focus()
        values = self.kiralikAraclar.item(selected, 'values')
        self.secBtn1.insert(0, values[0])
        self.secBtn2.insert(0, values[1])
        self.secBtn3.insert(0, values[2])
        self.secBtn4.insert(0, values[3])
        self.secBtn6.insert(0, values[4])
        self.secBtn7.insert(0, values[5])
    #secilen kiralık aracı güncelliyoruz
    def kiralıkAracGuncelleBtn(self):
        mysqlConnect.connect()
        kiralikAracGuncelle=mysqlConnect.cursor()
        guncelletc=self.secBtn1.get()
        guncelleyolculuk=self.secBtn7.get()
        kiralikAracGuncelle.execute("UPDATE kiralananaraclar  SET yolculuk=%s where musteriTc=%s", (guncelleyolculuk,guncelletc))
        mysqlConnect.commit()

        #tabloyu sıfırlıyoruz
        self.kiralikAraclar.delete(*self.kiralikAraclar.get_children())
        #sıfırladıgımız tabloya yeni güncel verileri getiriyoruz
        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.kiralananaraclar")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            self.kiralikAraclar.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()
    #secilen kiralık aracı siliyoruz veri tabanından ve tablodan
    def kiralıkAracSilBtn(self):
        saseNoSil=self.secBtn2.get()
        mysqlConnect.connect()
        sil = mysqlConnect.cursor()
        sql = "DELETE FROM kiralananaraclar WHERE aracSasi = %s"
        sil.execute(sql, (saseNoSil,))
        mysqlConnect.commit()
        #tabloyu sıfırlıyoruz
        self.kiralikAraclar.delete(*self.kiralikAraclar.get_children())

        mycursor = mysqlConnect.cursor()
        mycursor.execute("SELECT * FROM arac_kiralama.kiralananaraclar")
        myresult = mycursor.fetchall()
        self.y=0
        for x in myresult:
            print(x)
            # if x ==('TURKLER'):
            #     print(x)
            self.kiralikAraclar.insert('','end',text=self.y,values=(x))
            self.y=self.y+1
        mysqlConnect.close()
    #entrlerdeki değerleri sıfırlamamızı sağlıyor
    def entryTemizle(self):
        self.secBtn1.delete(0, 'end')  
        self.secBtn2.delete(0, 'end')  
        self.secBtn3.delete(0, 'end')  
        self.secBtn4.delete(0, 'end')  
        self.secBtn6.delete(0, 'end')  
        self.secBtn7.delete(0, 'end')  
    #arac teslim edildiyse araclar tablosunda aracın kira durumunu ---hayır kirada değil yazıyor---
    def teslimEdildi(self):
        mysqlConnect.connect()

        teslimDurumuUpdate=mysqlConnect.cursor()
        saseno=int(self.secBtn2.get())
        print(saseno)
        teslimDurumuUpdate.execute ("UPDATE aracbilgi  SET kiradaMi='hayır' where sasiNo=%s" % (saseno))
        mysqlConnect.commit()

        teslimDurumuUpdate=mysqlConnect.cursor()
        val3=int(self.secBtn1.get())
        print(saseno)
        teslimDurumuUpdate.execute ("UPDATE musteriler SET KIRA_DURUM='hayır' WHERE TC=%s" % (val3))
        mysqlConnect.commit()

        mysqlConnect.close()

otomasyon=Otomasyon()
otomasyon.window.mainloop()


