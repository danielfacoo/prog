from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector
from PyQt5.QtGui import *
#MYSQL BAĞLANTI
baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="fiyatlar")
#Telefon cursor
telefon=baglanti.cursor()
#Pantolon Cursor
pantolon = baglanti.cursor()
#Pc Cursor
pc = baglanti.cursor()
class fiyatHesaplama (QDialog):
    
    #Pantolon işlemler
    def pantolon(self):
        pantolon.execute("SELECT pantolon FROM jean")
        pantolonsorgu = pantolon.fetchone()
        print(pantolonsorgu)
        
        #Telefon İşlemler
    def telefon(self):
        telefon.execute("SELECT telefon FROM tel")
        telsorgu = telefon.fetchone()
        print(telsorgu)
        
        #Bilgisayar İşlemler
    def bilgisayar(self):
        pc.execute("SELECT fiyat from fiyat")
        pcsorgu = pc.fetchone()
        print(pcsorgu)
        
    
        #Layout
    def __init__(self,parent=None):                     
        super(fiyatHesaplama,self).__init__(parent)
        grid=QGridLayout()                                  
        
        
      
        
        #Bilgisayar Fiyatı
        grid.addWidget(QLabel("Bilgisayar Fiyatı:"),1,0)
        self.bbilgisayar=QLabel (self.bilgisayar())
        grid.addWidget(self.bbilgisayar,1,1)
        
        #Telefon Fiyatı
        grid.addWidget(QLabel("Telefon Fiyatı:"),2,0)
        self.ttelefon=QLabel(self.telefon())
        grid.addWidget(self.ttelefon,2,1)
        
        #Pantolon Fiyatı 
        grid.addWidget(QLabel("Pantolon Fiyatı:"),3,0)
        self.ppantolon=QLabel(self.pantolon())
        grid.addWidget(self.ppantolon,3,1)
        
        #Pantolon button
        hesaplabuton=QPushButton("Pantolon")
        grid.addWidget(hesaplabuton,4,0)
        hesaplabuton.clicked.connect(self.pantolon)
        
        #Telefon Button
        hesaplabuton2=QPushButton("Telefon")
        grid.addWidget(hesaplabuton2,4,1)
        hesaplabuton2.clicked.connect(self.telefon)
        
        #Bilgisayar Button
        hesaplabuton3=QPushButton("Bilgisayar")
        grid.addWidget(hesaplabuton3,4,2)
        hesaplabuton3.clicked.connect(self.bilgisayar)
        
                       
        self.setLayout(grid)
        #Başlık
        self.setWindowTitle("Fiyatını Takip Ettiğim Ürünler")
        

              
uygulama=QApplication([])
pencere=fiyatHesaplama()
pencere.show()
uygulama.exec_()
