# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appendCompany.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_appendCompany(object):
    def setupUi(self, appendCompany):
        if not appendCompany.objectName():
            appendCompany.setObjectName(u"appendCompany")
        appendCompany.resize(477, 389)
        appendCompany.setMinimumSize(QSize(477, 389))
        appendCompany.setMaximumSize(QSize(477, 389))
        appendCompany.setStyleSheet(u"background-color:#93c5f5;")
        self.addCompany = QPushButton(appendCompany)
        self.addCompany.setObjectName(u"addCompany")
        self.addCompany.setGeometry(QRect(350, 340, 121, 41))
        self.addCompany.setStyleSheet(u"background-color: #658aad\n"
"")
        self.label = QLabel(appendCompany)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 160, 151, 21))
        self.label_3 = QLabel(appendCompany)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 20, 301, 91))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_2 = QLabel(appendCompany)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 210, 51, 21))
        self.label_4 = QLabel(appendCompany)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 260, 151, 31))
        self.lineEditNameCompany = QLineEdit(appendCompany)
        self.lineEditNameCompany.setObjectName(u"lineEditNameCompany")
        self.lineEditNameCompany.setGeometry(QRect(170, 160, 241, 20))
        self.lineEditCity = QLineEdit(appendCompany)
        self.lineEditCity.setObjectName(u"lineEditCity")
        self.lineEditCity.setGeometry(QRect(90, 210, 101, 20))
        self.label_5 = QLabel(appendCompany)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 210, 21, 21))
        self.label_6 = QLabel(appendCompany)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 210, 16, 21))
        self.lineEditNameStreet = QLineEdit(appendCompany)
        self.lineEditNameStreet.setObjectName(u"lineEditNameStreet")
        self.lineEditNameStreet.setGeometry(QRect(240, 210, 101, 20))
        self.label_7 = QLabel(appendCompany)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 210, 16, 21))
        self.lineEditNameHouse = QLineEdit(appendCompany)
        self.lineEditNameHouse.setObjectName(u"lineEditNameHouse")
        self.lineEditNameHouse.setGeometry(QRect(370, 210, 61, 20))
        self.lineEditInn = QLineEdit(appendCompany)
        self.lineEditInn.setObjectName(u"lineEditInn")
        self.lineEditInn.setGeometry(QRect(190, 260, 211, 20))

        self.retranslateUi(appendCompany)

        QMetaObject.connectSlotsByName(appendCompany)
    # setupUi

    def retranslateUi(self, appendCompany):
        appendCompany.setWindowTitle(QCoreApplication.translate("appendCompany", u"Dialog", None))
        self.addCompany.setText(QCoreApplication.translate("appendCompany", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("appendCompany", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("appendCompany", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_2.setText(QCoreApplication.translate("appendCompany", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.label_4.setText(QCoreApplication.translate("appendCompany", u"\u0418\u041d\u041d:                                     \u2116", None))
        self.label_5.setText(QCoreApplication.translate("appendCompany", u"\u0433.", None))
        self.label_6.setText(QCoreApplication.translate("appendCompany", u"\u0443\u043b.", None))
        self.label_7.setText(QCoreApplication.translate("appendCompany", u"\u0434.", None))
    # retranslateUi

