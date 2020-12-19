# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowAppendContract.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AppendContract(object):
    def setupUi(self, Append):
        if not Append.objectName():
            Append.setObjectName(u"Append")
        Append.resize(568, 277)
        Append.setStyleSheet(u"background-color:#93c5f5;\n"
"font: 14pt \"Calibri\";")
        self.label = QLabel(Append)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 191, 31))
        self.label.setStyleSheet(u"font: 14pt \"Calibri\";")
        self.label_2 = QLabel(Append)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 111, 21))
        self.comboBox = QComboBox(Append)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 80, 221, 22))
        self.label_3 = QLabel(Append)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(39, 140, 131, 21))
        self.label_4 = QLabel(Append)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 190, 151, 21))
        self.lineEditPurpose = QLineEdit(Append)
        self.lineEditPurpose.setObjectName(u"lineEditPurpose")
        self.lineEditPurpose.setGeometry(QRect(190, 140, 251, 20))
        self.lineEditSum = QLineEdit(Append)
        self.lineEditSum.setObjectName(u"lineEditSum")
        self.lineEditSum.setGeometry(QRect(190, 190, 111, 20))
        self.apendContract = QPushButton(Append)
        self.apendContract.setObjectName(u"apendContract")
        self.apendContract.setGeometry(QRect(410, 230, 141, 23))

        self.retranslateUi(Append)

        QMetaObject.connectSlotsByName(Append)
    # setupUi

    def retranslateUi(self, Append):
        Append.setWindowTitle(QCoreApplication.translate("Append", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("Append", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0414\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("Append", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.label_3.setText(QCoreApplication.translate("Append", u"\u0426\u0435\u043b\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Append", u"\u0421\u0443\u043c\u043c\u0430 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.apendContract.setText(QCoreApplication.translate("Append", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

