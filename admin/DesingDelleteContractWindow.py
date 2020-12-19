# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DesingDelleteContractWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_DeleteContracts(object):
    def setupUi(self, DeleteContracts):
        if not DeleteContracts.objectName():
            DeleteContracts.setObjectName(u"DeleteContracts")
        DeleteContracts.resize(366, 190)
        DeleteContracts.setStyleSheet(u"background:#93c5f5;;\n"
"font: 14pt \"Calibri\";")
        self.comboBoxCompany = QComboBox(DeleteContracts)
        self.comboBoxCompany.setObjectName(u"comboBoxCompany")
        self.comboBoxCompany.setGeometry(QRect(20, 80, 321, 22))
        self.label = QLabel(DeleteContracts)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 221, 41))
        self.btnDelleteContract = QPushButton(DeleteContracts)
        self.btnDelleteContract.setObjectName(u"btnDelleteContract")
        self.btnDelleteContract.setGeometry(QRect(290, 150, 75, 31))

        self.retranslateUi(DeleteContracts)

        QMetaObject.connectSlotsByName(DeleteContracts)
    # setupUi

    def retranslateUi(self, DeleteContracts):
        DeleteContracts.setWindowTitle(QCoreApplication.translate("DeleteContracts", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("DeleteContracts", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.btnDelleteContract.setText(QCoreApplication.translate("DeleteContracts", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

