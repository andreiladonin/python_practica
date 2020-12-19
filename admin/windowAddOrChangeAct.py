import sqlite3

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox

from admin.windowAddOrChangeActDesigh import Ui_AppendAct

import datetime

d = datetime.date.today()

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

def getIDContract(idContract):
    cursor.execute("SELECT * FROM acts")
    res = cursor.fetchall()
    flag = False
    for i in res:
        if int(idContract) == i[1]:
            flag = True
    return flag

def windowDellOrChangedAct ():
    DellOrChangedAct = QtWidgets.QDialog()
    ui = Ui_AppendAct()
    ui.setupUi(DellOrChangedAct)

    cursor.execute(f"SELECT * FROM contracts ")
    res = cursor.fetchall()

    for i in res:
        ui.IdContract.addItem(str(i[0]))

    ui.dateAct.setDate(QtCore.QDate(int(d.year), int(d.month), int(d.day)))

    def dellOrChangedAct():
        idContract = ui.IdContract.currentText()

        data = ui.dateAct.text()

        summaAct = ui.SumaAct.text().strip()
        try:
            if getIDContract(idContract):
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Акт уже есть с Договором")
                x = msg.exec_()
            elif float(summaAct) < 0 or not summaAct:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Неправильная сумма Акта")
                x = msg.exec_()
            else:
                summaAct = str(int(summaAct))
                cursor.execute(
                    f"INSERT INTO acts (idContract, summaAct, data) VALUES ({int(idContract)}, '{summaAct}', '{data}')")
                db.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"Добавлен акт")
                x = msg.exec_()
                DellOrChangedAct.close()
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Введите сумму Акта")
            x = msg.exec_()

    ui.addAct.clicked.connect(dellOrChangedAct)
    return DellOrChangedAct.exec_()
