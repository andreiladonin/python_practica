# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actdelete.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_actDelete(object):
    def setupUi(self, actDelete):
        if not actDelete.objectName():
            actDelete.setObjectName(u"actDelete")
        actDelete.resize(403, 242)
        icon = QIcon()
        icon.addFile(u"C:/Users/User/Desktop/praktika blin/iconxd.png", QSize(), QIcon.Normal, QIcon.Off)
        actDelete.setWindowIcon(icon)
        actDelete.setStyleSheet(u"background-color:#93c5f5;")
        self.dellact = QPushButton(actDelete)
        self.dellact.setObjectName(u"dellact")
        self.dellact.setGeometry(QRect(280, 200, 121, 41))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(12)
        self.dellact.setFont(font)
        self.dellact.setStyleSheet(u"background-color: #658aad\n"
"")
        self.act = QComboBox(actDelete)
        self.act.setObjectName(u"act")
        self.act.setGeometry(QRect(210, 90, 181, 31))
        self.label = QLabel(actDelete)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 161, 51))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.retranslateUi(actDelete)

        QMetaObject.connectSlotsByName(actDelete)
    # setupUi

    def retranslateUi(self, actDelete):
        actDelete.setWindowTitle(QCoreApplication.translate("actDelete", u"Dialog", None))
        self.dellact.setText(QCoreApplication.translate("actDelete", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("actDelete", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430:", None))
    # retranslateUi

