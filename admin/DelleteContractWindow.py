import sqlite3

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox

from admin.DesingDelleteContractWindow import Ui_DeleteContracts

db = sqlite3.connect("Baza.db")

cursor = db.cursor()



def DelleteContractWindow ():

    windowDellContract = QtWidgets.QDialog()
    ui = Ui_DeleteContracts()
    ui.setupUi(windowDellContract)

    cursor.execute(f"SELECT * FROM contracts ")
    res = cursor.fetchall()
    ui.label.setText("Выбрать № догвора")
    # цикл добавлений компаний в комбобох из бд
    for i in res:
        ui.comboBoxCompany.addItem(str(i[0]))

    def btnDelleteContract ():
        company = ui.comboBoxCompany.currentText()
        msg = QMessageBox()
        msg.setWindowTitle("Удаление")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(f"Вы точно хотите удалить договор с {company} это приведет к удалению и акта")
        x = msg.exec_()
        if x == QMessageBox.Ok:
            cursor.execute(f"DELETE FROM contracts WHERE id = {int(company)} ")
            db.commit()
            cursor.execute(f"DELETE FROM acts WHERE idContract = {int(company)} ")
            db.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Договор удален и акт удален")
            x = msg.exec_()
            windowDellContract.close()

    ui.btnDelleteContract.clicked.connect(btnDelleteContract)
    return windowDellContract.exec_()