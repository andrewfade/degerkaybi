from PyQt5 import QtWidgets
import sys
from mainwindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.hesapla.clicked.connect(self.dkhesapla)
        self.ui.verileritemizle.clicked.connect(self.cbverileritemizle)

    def cbverileritemizle(self):
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                cb.setChecked(False)

    def dkhesapla(self):
        try:
            piyasa = int(self.ui.lE_piyasa.text())
            kilometre = int(self.ui.lE_kilometre.text())
            hasar = int(self.ui.lE_hasar.text())
            sbm = self.ui.comboBox.currentIndex()
            ticari = self.ui.cb_ticari.isChecked()
            print(piyasa, kilometre, hasar,type(sbm),ticari)
            items = self.ui.gb_aracturu.findChildren(QtWidgets.QRadioButton)
            for rb in items:
                if rb.isChecked():
                    arac = rb.text()
            if arac ==  "Araba / Taksi" or arac == "Motosiklet":
                if piyasa <= 49999:
                    R = 0.65
                elif 99999 >= piyasa > 49999: 
                    R = 0.7
                elif 199999 >= piyasa >= 100000:
                    R = 0.75
                elif 299999 >= piyasa >= 200000:
                    R = 0.8
                elif 399999 >= piyasa >= 300000:
                    R = 0.85
                elif 499999 >= piyasa >= 400000:
                    R = 0.9
                elif 749999 >= piyasa >= 500000:
                    R = 0.95
                else:
                    R = 1.0
            else:
                if piyasa <= 249999:
                    R = 0.65
                elif 349999 >= piyasa > 249999: 
                    R = 0.7
                elif 499999 >= piyasa >= 350000:
                    R = 0.75
                elif 749999 >= piyasa >= 500000:
                    R = 0.8
                elif 999999 >= piyasa >= 750000:
                    R = 0.85
                elif 1249999 >= piyasa >= 1000000:
                    R = 0.9
                elif 1499999 >= piyasa >= 1250000:
                    R = 0.95
                else:
                    R = 1.0
            if arac ==  "Araba / Taksi" or arac == "Motosiklet":
                if kilometre <= 19999:
                    K = 1
                elif 49999 >= kilometre > 19999: 
                    K = 0.95
                elif 99999 >= kilometre >= 50000:
                    K = 0.9
                elif 149999 >= kilometre >= 100000:
                    K = 0.85
                elif 199999 >= kilometre >= 150000:
                    K = 0.8
                elif 299999 >= kilometre >= 200000:
                    K = 0.75
                else:
                    K = 0.7
            elif arac == "İş Makinesi/ Traktör/Tarım Makinesi":
                calisma = int(self.ui.lE_calisma.text())
                if calisma <= 500:
                    K = 1
                elif 1000 >= calisma > 500: 
                    K = 0.95
                elif 2000 >= calisma >= 1001:
                    K = 0.9
                elif 3000 >= calisma >= 2001:
                    K = 0.85
                elif 4000 >= calisma >= 3001:
                    K = 0.8
                elif 5000 >= calisma >= 4001:
                    K = 0.75
                else:
                    K = 0.7
            else:
                if kilometre <= 49999:
                    K = 1
                elif 149999 >= kilometre > 49999: 
                    K = 0.95
                elif 299999 >= kilometre >= 150000:
                    K = 0.9
                elif 499999 >= kilometre >= 300000:
                    K = 0.85
                elif 749999 >= kilometre >= 500000:
                    K = 0.8
                elif 999999 >= kilometre >= 750000:
                    K = 0.75
                else:
                    K = 0.7
            if arac == "Araba / Taksi":
                HK = 0
                items = self.ui.gb_araba.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())
            elif arac == "Minibüs/ Otobüs":
                HK = 0
                items = self.ui.gb_minibus.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())
            elif arac == "Kamyonet/ Kamyon/ Çekici":
                HK = 0
                items = self.ui.gb_kamyon.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())
            elif arac == "İş Makinesi/ Traktör/Tarım Makinesi":
                HK = 0
                items = self.ui.gb_ismakinesi.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())
            elif arac == "Romörk":
                HK = 0
                items = self.ui.gb_romork.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())
            elif arac == "Motosiklet":
                HK = 0
                items = self.ui.gb_motosiklet.findChildren(QtWidgets.QCheckBox)
                for cb in items:
                    if cb.isChecked():
                        HK += float(cb.text())

            T = (hasar / piyasa) * 10
            H = (HK + T) / 100

            G = 0
            G1 = 0
            if self.ui.cb_ticari.isChecked():
                G1 = -0.05
            G2 = self.ui.comboBox.currentIndex() * (-0.03)
            G3 = 0
            if arac ==  "Araba / Taksi" or arac == "Motosiklet":
                if kilometre <= 1000:
                    G3 =0.05
                elif 21000 >= kilometre > 19999: 
                    G3 =0.05
                elif 51000 >= kilometre >= 50000:
                    G3 =0.05
                elif 101000 >= kilometre >= 100000:
                    G3 =0.05
                elif 151000 >= kilometre >= 150000:
                    G3 =0.05
                elif 201000 >= kilometre >= 200000:
                    G3 =0.05
                elif 301000 >= kilometre >= 300000:
                    G3 =0.05
            elif arac != "İş Makinesi/ Traktör/Tarım Makinesi":
                if kilometre <= 1000:
                    G3 = 0.05
                elif 51000 >= kilometre > 49999: 
                    G3 = 0.05
                elif 151000 >= kilometre >= 150000:
                    G3 = 0.05
                elif 301000 >= kilometre >= 300000:
                    G3 = 0.05
                elif 501000 >= kilometre >= 500000:
                    G3 = 0.05
                elif 751000 >= kilometre >= 750000:
                    G3 = 0.05
                elif 1001000 >= kilometre >= 1000000:
                    G3 = 0.05
            G = 1 + G1 + G2 + G3

            DK = piyasa * R * K * H * G
            
            if arac == "Motosiklet":
                DK *= 2.5
            print(R,K,HK, piyasa, H, G, DK)

            result = f"Hesaplanan Değer Kaybı:\n{int(DK)} TL'dir"   
            self.ui.SONUC.setText(result)
        except:
            result = f"Lütfen girmiş olduğunuz verileri kontrol edin"   
            self.ui.SONUC.setText(result)


      
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()