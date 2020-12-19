# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuUser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MenuAdnin(object):
    def setupUi(self, MenuAdnin):
        if not MenuAdnin.objectName():
            MenuAdnin.setObjectName(u"MenuAdnin")
        MenuAdnin.resize(1100, 596)
        MenuAdnin.setMaximumSize(QSize(1100, 850))
        icon = QIcon()
        icon.addFile(u"iconxd.png", QSize(), QIcon.Normal, QIcon.Off)
        MenuAdnin.setWindowIcon(icon)
        MenuAdnin.setStyleSheet(u"background-color:#93c5f5;")
        self.tabWidget = QTabWidget(MenuAdnin)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1091, 551))
        self.tabWidget.setMaximumSize(QSize(1091, 781))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color:#93c5f5;\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableDirectory = QTableWidget(self.tab)
        if (self.tableDirectory.columnCount() < 4):
            self.tableDirectory.setColumnCount(4)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableDirectory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableDirectory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableDirectory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableDirectory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableDirectory.setObjectName(u"tableDirectory")
        self.tableDirectory.setGeometry(QRect(0, 0, 1091, 781))
        self.tableDirectory.setMinimumSize(QSize(1091, 781))
        self.tableDirectory.setMaximumSize(QSize(1091, 781))
        self.tableDirectory.setRowCount(0)
        self.tableDirectory.horizontalHeader().setMinimumSectionSize(250)
        self.tableDirectory.horizontalHeader().setDefaultSectionSize(250)
        self.tableDirectory.horizontalHeader().setHighlightSections(True)
        self.tableDirectory.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableDirectory.horizontalHeader().setStretchLastSection(True)
        self.changeDirectory = QPushButton(self.tab)
        self.changeDirectory.setObjectName(u"changeDirectory")
        self.changeDirectory.setGeometry(QRect(140, 490, 121, 21))
        self.addDirectory = QPushButton(self.tab)
        self.addDirectory.setObjectName(u"addDirectory")
        self.addDirectory.setGeometry(QRect(10, 490, 121, 21))
        self.importSpravochnik = QToolButton(self.tab)
        self.importSpravochnik.setObjectName(u"importSpravochnik")
        self.importSpravochnik.setGeometry(QRect(270, 490, 121, 21))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableContact = QTableWidget(self.tab_2)
        if (self.tableContact.columnCount() < 5):
            self.tableContact.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableContact.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableContact.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableContact.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tableContact.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tableContact.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tableContact.setObjectName(u"tableContact")
        self.tableContact.setGeometry(QRect(0, 0, 1091, 531))
        self.tableContact.setMaximumSize(QSize(1091, 781))
        self.tableContact.setRowCount(0)
        self.tableContact.horizontalHeader().setMinimumSectionSize(200)
        self.tableContact.horizontalHeader().setDefaultSectionSize(200)
        self.tableContact.horizontalHeader().setHighlightSections(True)
        self.tableContact.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableContact.horizontalHeader().setStretchLastSection(True)
        self.addContact = QToolButton(self.tab_2)
        self.addContact.setObjectName(u"addContact")
        self.addContact.setGeometry(QRect(10, 490, 121, 21))
        self.changeContact = QToolButton(self.tab_2)
        self.changeContact.setObjectName(u"changeContact")
        self.changeContact.setGeometry(QRect(140, 490, 121, 21))
        self.importContract = QToolButton(self.tab_2)
        self.importContract.setObjectName(u"importContract")
        self.importContract.setGeometry(QRect(270, 490, 121, 21))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableAct = QTableWidget(self.tab_3)
        if (self.tableAct.columnCount() < 4):
            self.tableAct.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tableAct.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tableAct.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tableAct.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tableAct.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.tableAct.setObjectName(u"tableAct")
        self.tableAct.setGeometry(QRect(-5, 1, 1091, 781))
        self.tableAct.setMinimumSize(QSize(1091, 781))
        self.tableAct.setMaximumSize(QSize(1091, 781))
        self.tableAct.setRowCount(0)
        self.tableAct.horizontalHeader().setMinimumSectionSize(200)
        self.tableAct.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableAct.horizontalHeader().setStretchLastSection(True)
        self.addAct = QToolButton(self.tab_3)
        self.addAct.setObjectName(u"addAct")
        self.addAct.setGeometry(QRect(10, 490, 121, 21))
        self.changeAct = QToolButton(self.tab_3)
        self.changeAct.setObjectName(u"changeAct")
        self.changeAct.setGeometry(QRect(140, 490, 121, 21))
        self.importAct = QToolButton(self.tab_3)
        self.importAct.setObjectName(u"importAct")
        self.importAct.setGeometry(QRect(270, 490, 121, 21))
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(MenuAdnin)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MenuAdnin)
    # setupUi

    def retranslateUi(self, MenuAdnin):
        MenuAdnin.setWindowTitle(QCoreApplication.translate("MenuAdnin", u"\u041c\u0435\u043d\u044e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        ___qtablewidgetitem = self.tableDirectory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MenuAdnin", u"ID \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None));
        ___qtablewidgetitem1 = self.tableDirectory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MenuAdnin", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableDirectory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u041d\u041d", None));
        ___qtablewidgetitem3 = self.tableDirectory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MenuAdnin", u"\u0410\u0434\u0440\u0435\u0441", None));
        self.changeDirectory.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.addDirectory.setText(QCoreApplication.translate("MenuAdnin", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.importSpravochnik.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0432 EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MenuAdnin", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u043e\u0432", None))
        ___qtablewidgetitem4 = self.tableContact.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MenuAdnin", u"ID \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem5 = self.tableContact.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MenuAdnin", u"ID \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None));
        ___qtablewidgetitem6 = self.tableContact.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MenuAdnin", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None));
        ___qtablewidgetitem7 = self.tableContact.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MenuAdnin", u"\u0426\u0435\u043b\u044c \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem8 = self.tableContact.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MenuAdnin", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0443", None));
        self.addContact.setText(QCoreApplication.translate("MenuAdnin", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.changeContact.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.importContract.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0432 EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MenuAdnin", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0443", None))
        ___qtablewidgetitem9 = self.tableAct.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MenuAdnin", u"\u2116 \u0430\u043a\u0442\u0430", None));
        ___qtablewidgetitem10 = self.tableAct.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MenuAdnin", u"\u2116 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem11 = self.tableAct.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MenuAdnin", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u043e \u0430\u043a\u0442\u0443", None));
        ___qtablewidgetitem12 = self.tableAct.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MenuAdnin", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d\u0438\u044f", None));
        self.addAct.setText(QCoreApplication.translate("MenuAdnin", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c ", None))
        self.changeAct.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.importAct.setText(QCoreApplication.translate("MenuAdnin", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0432 EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MenuAdnin", u"\u0410\u043a\u0442\u044b \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442", None))
    # retranslateUi

