import sqlite3

from PySide2.QtWidgets import QMessageBox
from PySide2 import QtWidgets

from admin.actDeleteDes import Ui_actDelete

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

def windowDellAct():
    dellAct = QtWidgets.QDialog()
    ui = Ui_actDelete()
    ui.setupUi(dellAct)
    cursor.execute(f"SELECT * FROM acts ")

    res = cursor.fetchall()

    for i in res:
        ui.act.addItem(str(i[0]))

    def delleteAct ():
        act = ui.act.currentText()
        msg = QMessageBox()
        msg.setWindowTitle("Удаление")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(f"Вы точно хотите удалить акт № {act}")
        x = msg.exec_()
        if x == QMessageBox.Ok:
            cursor.execute(f"DELETE FROM acts WHERE id = {int(act)} ")
            db.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Акт удален")
            x = msg.exec_()
            dellAct.close()

    ui.dellact.clicked.connect(delleteAct)

    return dellAct.exec_()