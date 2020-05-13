# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\deneme.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pyperclip
import subprocess

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setWindowIcon(QtGui.QIcon(r"C:\Users\baki\Desktop\youtube\you.png"))
        MainWindow.resize(377, 170)
        MainWindow.setMinimumSize(QtCore.QSize(377, 170))
        MainWindow.setMaximumSize(QtCore.QSize(377, 170
        ))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.direcEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.direcEdit.setObjectName("direcEdit")
        self.gridLayout.addWidget(self.direcEdit, 3, 3, 1, 8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 6, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 15, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 13, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 2)
        self.linkEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.linkEdit.setObjectName("linkEdit")
        self.gridLayout.addWidget(self.linkEdit, 0, 5, 1, 10)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 9, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 2)
        self.pastButton = QtWidgets.QPushButton(self.centralwidget)
        self.pastButton.setObjectName("pastButton")
        self.gridLayout.addWidget(self.pastButton, 1, 11, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 4, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 14, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 3, 12, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 2, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 2, 15, 1, 1)
        self.resul3 = QtWidgets.QRadioButton(self.centralwidget)
        self.resul3.setObjectName("resul3")
        self.gridLayout.addWidget(self.resul3, 2, 6, 1, 1)
        self.resul4 = QtWidgets.QRadioButton(self.centralwidget)
        self.resul4.setObjectName("resul4")
        self.gridLayout.addWidget(self.resul4, 2, 7, 1, 1)
        self.resul10 = QtWidgets.QRadioButton(self.centralwidget)
        self.resul10.setObjectName("resul10")
        self.gridLayout.addWidget(self.resul10, 2, 11, 1, 1)
        self.resul7 = QtWidgets.QRadioButton(self.centralwidget)
        self.resul7.setObjectName("resul7")
        self.gridLayout.addWidget(self.resul7, 2, 9, 1, 1)
        self.direcButton = QtWidgets.QPushButton(self.centralwidget)
        self.direcButton.setObjectName("direcButton")
        self.gridLayout.addWidget(self.direcButton, 3, 2, 1, 1)
        self.durum = QtWidgets.QLabel(self.centralwidget)
        self.durum.setMaximumSize(QtCore.QSize(64, 56))
        self.durum.setFont(font)
        self.durum.setText("")
        self.durum.setScaledContents(True)
        self.durum.setObjectName("durum")
        self.gridLayout.addWidget(self.durum, 1, 2, 2, 1)
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 3, 11, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.link = ''
        self.youtube = r"C:\Users\baki\Desktop\youtube\youtube-dl\youtube-dl.exe"
        self.reparam = '-F'
        self.title = '%(title)s.%(ext)s'
        self.path = r'C:\Users\baki\Videos'

        self.resul3.toggled.connect(self.res3)
        self.resul4.toggled.connect(self.res4)
        self.resul7.toggled.connect(self.res7)
        self.resul10.toggled.connect(self.res10)
        self.pastButton.clicked.connect(self.yapistir)
        self.clearButton.clicked.connect(self.clearLink)
        self.direcButton.clicked.connect(self.selectF)
        self.downButton.clicked.connect(self.down)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.linkEdit, self.pastButton)
        MainWindow.setTabOrder(self.pastButton, self.resul3)
        MainWindow.setTabOrder(self.resul3, self.resul4)
        MainWindow.setTabOrder(self.resul4, self.resul7)
        MainWindow.setTabOrder(self.resul7, self.resul10)
        MainWindow.setTabOrder(self.resul10, self.direcButton)
        MainWindow.setTabOrder(self.direcButton, self.direcEdit)
        MainWindow.setTabOrder(self.direcEdit, self.downButton)
        MainWindow.setTabOrder(self.downButton, self.clearButton)

    def yapistir(self):
        self.link = pyperclip.paste()
        self.clearLink()
        if isinstance(self.link,str):
            self.linkEdit.insert(self.link)
    
    def clearLink(self):
        self.linkEdit.clear()

    def res3(self):
        self.reparam = '-f 18'

    def res4(self):
        self.reparam = '-f 135+140'

    def res7(self):
        self.reparam = '-f 22'

    def res10(self):
        self.reparam = '-f 137+140'

    def selectF(self):
        foldr = QtWidgets.QFileDialog.getExistingDirectory(self,"Open f",self.path)
        if foldr:
            self.direcEdit.insert(foldr)
            self.path = foldr + "\\" + self.title

    def down(self):
        self.durum.setObjectName("Indiriliyor")
        subprocess.run([self.youtube,self.reparam,self.linkEdit.text(),'-o',self.path],shell=True,text=True)
        if subprocess.CompletedProcess.check_returncode:
            self.durum.setPixmap(QtGui.QPixmap(r"C:\Users\baki\Desktop\youtube\ok.png"))
        else:
            self.durum.setPixmap(QtGui.QPixmap(r"C:\Users\baki\Desktop\youtube\error.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.clearButton.setText(_translate("MainWindow", "Temizle"))
        self.label.setText(_translate("MainWindow", "Youtube Link:"))
        self.pastButton.setText(_translate("MainWindow", "Yapıştır"))
        self.resul3.setText(_translate("MainWindow", "360p"))
        self.resul4.setText(_translate("MainWindow", "480p"))
        self.resul10.setText(_translate("MainWindow", "1080p"))
        self.resul7.setText(_translate("MainWindow", "720p"))
        self.direcButton.setText(_translate("MainWindow", "Klasor"))
        self.downButton.setText(_translate("MainWindow", "İndir"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())