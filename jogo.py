# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jogo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Jokenpo(object):
    def setupUi(self, Jokenpo):
        Jokenpo.setObjectName("Jokenpo")
        Jokenpo.resize(545, 374)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Jokenpo.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Jokenpo)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 10, 91, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelFichas = QtWidgets.QLabel(self.frame)
        self.labelFichas.setGeometry(QtCore.QRect(0, 0, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelFichas.setFont(font)
        self.labelFichas.setText("")
        self.labelFichas.setObjectName("labelFichas")
        self.btnPedra = QtWidgets.QPushButton(self.centralwidget)
        self.btnPedra.setGeometry(QtCore.QRect(20, 100, 101, 51))
        self.btnPedra.setObjectName("btnPedra")
        self.btnPapel = QtWidgets.QPushButton(self.centralwidget)
        self.btnPapel.setGeometry(QtCore.QRect(20, 150, 101, 51))
        self.btnPapel.setObjectName("btnPapel")
        self.btnTesoura = QtWidgets.QPushButton(self.centralwidget)
        self.btnTesoura.setGeometry(QtCore.QRect(20, 200, 101, 51))
        self.btnTesoura.setObjectName("btnTesoura")
        self.inputValor = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValor.setGeometry(QtCore.QRect(20, 60, 231, 41))
        self.inputValor.setObjectName("inputValor")
        self.inputDepositar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputDepositar.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.inputDepositar.setObjectName("inputDepositar")
        self.labelDepositar = QtWidgets.QLabel(self.centralwidget)
        self.labelDepositar.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.labelDepositar.setObjectName("labelDepositar")
        self.btnDepositar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDepositar.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.btnDepositar.setObjectName("btnDepositar")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(129, 109, 391, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelJogo = QtWidgets.QLabel(self.frame_2)
        self.labelJogo.setGeometry(QtCore.QRect(10, 10, 371, 231))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelJogo.setFont(font)
        self.labelJogo.setStyleSheet("color:red")
        self.labelJogo.setText("")
        self.labelJogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJogo.setObjectName("labelJogo")
        Jokenpo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jokenpo)
        QtCore.QMetaObject.connectSlotsByName(Jokenpo)

    def retranslateUi(self, Jokenpo):
        _translate = QtCore.QCoreApplication.translate
        Jokenpo.setWindowTitle(_translate("Jokenpo", "Jokenpo"))
        self.btnPedra.setText(_translate("Jokenpo", "PEDRA"))
        self.btnPapel.setText(_translate("Jokenpo", "PAPEL"))
        self.btnTesoura.setText(_translate("Jokenpo", "TESOURA"))
        self.labelDepositar.setText(_translate("Jokenpo", "DEPOSITAR:"))
        self.btnDepositar.setText(_translate("Jokenpo", "Depositar"))