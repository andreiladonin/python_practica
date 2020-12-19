import sqlite3

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox

from admin.windowChangedDesigh import Ui_ChangedAct

import datetime

d = datetime.date.today()


db = sqlite3.connect("Baza.db")

cursor = db.cursor()

def windowChangedAct():
    w = QtWidgets.QDialog()
    ui = Ui_ChangedAct()
    ui.setupUi(w)
    cursor.execute(f"SELECT * FROM acts ")
    res = cursor.fetchall()
    ui.label_2.setText("№ акта")
    for i in res:
        ui.IdAct.addItem(str(i[0]))
    #выбор акта
    def choiseAct ():

        cursor.execute(f"SELECT * FROM acts ")
        res = cursor.fetchall()
        act = ui.IdAct.currentText()

        sumAndData = []

        for i in res:
            if int(act) == i[0]:
                sumAndData.append(i[2])
                sumAndData.append(i[3])
        ui.SumaAct.setText(str(sumAndData[0]))
        ui.dateAct.setDate(QtCore.QDate(int(sumAndData[1][6:]), int(sumAndData[1][3:5]), int(sumAndData[1][:2])))

    # изменение акта
    def changeAct():
        act = ui.IdAct.currentText()
        sumAct = ui.SumaAct.text().strip()
        data = ui.dateAct.text()

        if not sumAct:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Введите сумму Акта ")
            x = msg.exec_()
        if (sumAct.isnumeric() == False) or (int(sumAct) < 0):
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Неккорретная сумма акта")
            x = msg.exec_()
        else:
            cursor.execute(f"UPDATE acts SET summaAct = '{sumAct}' WHERE id = {int(act)}")
            db.commit()

            cursor.execute(f"UPDATE acts SET data = '{data}' WHERE id = {int(act)}")
            db.commit()
            w.close()


    ui.choiseAct.clicked.connect(choiseAct)
    ui.addAct.clicked.connect(changeAct)
    return w.exec_()