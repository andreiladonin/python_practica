# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vhod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(225, 225)
        Dialog.setMinimumSize(QSize(225, 225))
        Dialog.setMaximumSize(QSize(225, 225))
        icon = QIcon()
        icon.addFile(u"iconxd.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color:#93c5f5;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 51, 21))
        font = QFont()
        font.setFamily(u"Calibri")
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 41, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 15, 121, 41))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 182, 101, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 14pt \"Calibri\";\n"
"background-color: #658aad\n"
"};")
        self.login = QLineEdit(Dialog)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(80, 90, 113, 20))
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(80, 140, 113, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

