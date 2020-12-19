# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowChangedAct.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChangedAct(object):
    def setupUi(self, ChangedAct):
        if not ChangedAct.objectName():
            ChangedAct.setObjectName(u"ChangedAct")
        ChangedAct.resize(667, 280)
        ChangedAct.setStyleSheet(u"background: #93c5f5;\n"
"font: 14pt \"Calibri\";")
        self.label_2 = QLabel(ChangedAct)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 131, 41))
        self.IdAct = QComboBox(ChangedAct)
        self.IdAct.setObjectName(u"IdAct")
        self.IdAct.setGeometry(QRect(170, 40, 201, 22))
        self.label_3 = QLabel(ChangedAct)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 131, 41))
        self.SumaAct = QLineEdit(ChangedAct)
        self.SumaAct.setObjectName(u"SumaAct")
        self.SumaAct.setGeometry(QRect(170, 100, 121, 20))
        self.label_4 = QLabel(ChangedAct)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 131, 41))
        self.dateAct = QDateEdit(ChangedAct)
        self.dateAct.setObjectName(u"dateAct")
        self.dateAct.setGeometry(QRect(170, 150, 110, 22))
        self.addAct = QPushButton(ChangedAct)
        self.addAct.setObjectName(u"addAct")
        self.addAct.setGeometry(QRect(250, 190, 221, 41))
        self.choiseAct = QPushButton(ChangedAct)
        self.choiseAct.setObjectName(u"choiseAct")
        self.choiseAct.setGeometry(QRect(380, 30, 121, 41))

        self.retranslateUi(ChangedAct)

        QMetaObject.connectSlotsByName(ChangedAct)
    # setupUi

    def retranslateUi(self, ChangedAct):
        ChangedAct.setWindowTitle(QCoreApplication.translate("ChangedAct", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("ChangedAct", u"ID \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("ChangedAct", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u043e \u0410\u043a\u0442\u0443", None))
        self.label_4.setText(QCoreApplication.translate("ChangedAct", u"\u0414\u0430\u0442\u0430 \u041f\u043e\u0434\u043f\u0438\u0441\u0438", None))
        self.addAct.setText(QCoreApplication.translate("ChangedAct", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.choiseAct.setText(QCoreApplication.translate("ChangedAct", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

