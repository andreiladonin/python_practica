# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminka.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_panelAdmin(object):
    def setupUi(self, panelAdmin):
        if not panelAdmin.objectName():
            panelAdmin.setObjectName(u"panelAdmin")
        panelAdmin.resize(477, 389)
        panelAdmin.setMinimumSize(QSize(477, 389))
        panelAdmin.setMaximumSize(QSize(477, 389))
        panelAdmin.setStyleSheet(u"background-color:#93c5f5;")
        self.addAccount = QPushButton(panelAdmin)
        self.addAccount.setObjectName(u"addAccount")
        self.addAccount.setGeometry(QRect(350, 340, 121, 41))
        self.addAccount.setStyleSheet(u"background-color: #658aad\n"
"")
        self.label = QLabel(panelAdmin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 159, 121, 31))
        self.label_3 = QLabel(panelAdmin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 20, 301, 91))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.login = QTextEdit(panelAdmin)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(180, 160, 171, 31))
        self.label_2 = QLabel(panelAdmin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 210, 121, 31))
        self.password = QTextEdit(panelAdmin)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(180, 210, 171, 31))
        self.label_4 = QLabel(panelAdmin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 121, 31))
        self.typeAccount = QComboBox(panelAdmin)
        self.typeAccount.addItem("")
        self.typeAccount.addItem("")
        self.typeAccount.setObjectName(u"typeAccount")
        self.typeAccount.setGeometry(QRect(180, 260, 171, 22))
        self.dellAccount = QPushButton(panelAdmin)
        self.dellAccount.setObjectName(u"dellAccount")
        self.dellAccount.setGeometry(QRect(220, 340, 121, 41))
        self.dellAccount.setStyleSheet(u"background-color: #658aad\n"
"")

        self.retranslateUi(panelAdmin)

        QMetaObject.connectSlotsByName(panelAdmin)
    # setupUi

    def retranslateUi(self, panelAdmin):
        panelAdmin.setWindowTitle(QCoreApplication.translate("panelAdmin", u"Админка", None))
        self.addAccount.setText(QCoreApplication.translate("panelAdmin", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("panelAdmin", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("panelAdmin", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u043b\u0438 \u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("panelAdmin", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_4.setText(QCoreApplication.translate("panelAdmin", u"\u0422\u0438\u043f \u0423\u0447\u0435\u0442\u043a\u0438:", None))
        self.typeAccount.setItemText(0, QCoreApplication.translate("panelAdmin", u"\u0410\u0434\u043c\u0438\u043d", None))
        self.typeAccount.setItemText(1, QCoreApplication.translate("panelAdmin", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))

        self.dellAccount.setText(QCoreApplication.translate("panelAdmin", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

