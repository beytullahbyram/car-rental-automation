#TABLE İNFO

# create table
# cursorObject = mysqlConnect.cursor()
aracKiralamaTablosu = """CREATE TABLE musteriler (
TC INT NOT NULL,
AD_SOYAD VARCHAR(20) NOT NULL,
TELEFON INT NOT NULL,
DOGUM_TARIH VARCHAR(10) NOT NULL,
MAIL VARCHAR(20),
MESLEK VARCHAR(20),
EHLIYET VARCHAR(20) NOT NULL,
MEDENI_DURUMU VARCHAR(20),
EGITIM_DURUMU VARCHAR(20),
KIRA_DURUM VARCHAR(10)
)"""
# cursorObject.execute(aracKiralamaTablosu)


# cursorObject2 = mysqlConnect.cursor()
aracBilgiTablo = """CREATE TABLE aracBilgi (
aracTur VARCHAR(10) NOT NULL,
marka VARCHAR(10) NOT NULL,
model VARCHAR(10) NOT NULL,
yıl VARCHAR(10) NOT NULL,
uretimModeli VARCHAR(10) NOT NULL,
yakıt VARCHAR(15) NOT NULL,
vites VARCHAR(15) NOT NULL,
motorGucu INT NOT NULL,
motorHacmi INT NOT NULL,
motorNo INT NOT NULL,
kasaTip VARCHAR(20) NOT NULL,
cekis VARCHAR(20) NOT NULL,
kapi INT NOT NULL,
renk VARCHAR(15) NOT NULL,
sasiNo INT NOT NULL,
gunlukFiyat INT NOT NULL,
kiradaMi VARCHAR(10) NOT NULL,
kullanimDisiMi VARCHAR(10) NOT NULL
)"""
# cursorObject2.execute(aracBilgiTablo)
#


#3.tablomuzu olusturduk
# cursorObject3 = mysqlConnect.cursor()
kiralananAraclarTablosu = """CREATE TABLE kiralananAraclar (
musteriTC VARCHAR(11) NOT NULL,
aracSasi INT(10) NOT NULL,
kiralamaTarihi DATE NOT NULL,
teslimTarihi DATE NOT NULL,
ucret INT NOT NULL,
yolculuk VARCHAR(15) NOT NULL
)"""
# cursorObject3.execute(kiralananAraclarTablosu)
# mysqlConnect.close()
