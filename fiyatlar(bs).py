import requests
from bs4 import BeautifulSoup
import mysql.connector
#MYSQL
baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="fiyatlar")
isaretci=baglanti.cursor()

#BİLGİSAYAR LİNKİ
URL = 'https://www.gittigidiyor.com/dizustu-laptop-notebook-bilgisayar/msi-gl75-9sd-050tr_spp_763039?id=588952901'
#kullanıcı bilgileri
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

#def bilgisayar():
sayfa = requests.get(URL, headers=headers)
soup = BeautifulSoup(sayfa.content,'html.parser')


#Fiyat verisini çekme
fiyat = soup.find(id="sp-price-highPrice").get_text()

#0. index(TL'yi silme)
a=(fiyat.split()[0])

#virgülü noktaya çevirme
b=a.replace(',','.')

#noktayı silme
c=int(b.replace('.',''))
print(c)


if(c<3000000):
    def gonder():
        isaretci.execute('''INSERT INTO fiyat(fiyat) VALUES("%s")'''%(c))
        baglanti.commit()
        baglanti.close
    gonder()

#TELEFON
URL2 ='https://www.trendyol.com/apple/iphone-11-64gb-beyaz-apple-turkiye-garantili-p-32055428'
#kullanıcı bilgileri
headers2 = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
sayfa2 = requests.get(URL2, headers=headers2)
soup2 = BeautifulSoup(sayfa2.content,'html.parser')

#TELEFON İD
fiyat2 =soup2.find(class_='prc-slg').get_text()

#0. index(TL'yi silme)
d=(fiyat2.split()[0])

#virgülü noktaya çevirme
e=d.replace(',','.')

#noktayı silme
f=int(e.replace('.',''))
print(f)
if(f<100000):
    def gonder2():
        isaretci.execute('''INSERT INTO tel(telefon) VALUES("%s")'''%(f))
        baglanti.commit()
        baglanti.close
    gonder2()

#PANTOLON

URL3='https://www.boyner.com.tr/aeropostale-denim-pantolon-843013-200109'
#kullanıcı bilgileri
headers3 = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
sayfa3 = requests.get(URL3, headers=headers3)
soup3 = BeautifulSoup(sayfa3.content,'html.parser')

#pantolon id

fiyat3 = soup3.find(class_="price-payable").get_text()
#0. index(TL'yi silme)
g=(fiyat3.split()[0])

#virgülü noktaya çevirme
h=g.replace(',','.')

#noktayı silme
i=int(h.replace('.',''))
print(i)


if(i<19000):
    def gonder3():
        isaretci.execute('''INSERT INTO jean(pantolon) VALUES("%s")'''%(i))
        baglanti.commit()
        baglanti.close
    gonder3()
