import sqlite3
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
from admin.deleteCompanyDesign import deleteCompany

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

def getIDContract(nameCompany):
    cursor.execute("SELECT * FROM contracts")
    res = cursor.fetchall()
    idContract = 0
    for i in res:
        if i[2] == nameCompany:
            idContract = i[0]
    return idContract
def windowDellCompany ():
    global windowDelleteCompany
    windowDelleteCompany = QtWidgets.QDialog()
    ui = deleteCompany()
    ui.setupUi(windowDelleteCompany)

    cursor.execute(f"SELECT * FROM firms ")
    res = cursor.fetchall()

    # цикл добавлений компаний в комбобох из бд
    for i in res:
        ui.comboBox.addItem(i[1])

    # ф-я удаление из бд
    def btnDeleteCompany():
        nameCompany = ui.comboBox.currentText()

        msg = QMessageBox()
        msg.setWindowTitle("Удаление")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText(f"Вы точно хотите удалить компанию {nameCompany}. Это приведет к удалению актов и договоров")
        x = msg.exec_()

        if x == QMessageBox.Ok:
            idContract = getIDContract(nameCompany)
            cursor.execute(f"DELETE FROM firms WHERE nameCompany = '{nameCompany}' ")
            db.commit()
            cursor.execute(f"DELETE FROM contracts WHERE nameCompany = '{nameCompany}' ")
            db.commit()

            cursor.execute(f"DELETE FROM acts WHERE idContract = {idContract} ")
            db.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"{nameCompany} удалена")
            x = msg.exec_()
            windowDelleteCompany.close()

    ui.pushButton.clicked.connect(btnDeleteCompany)

    return windowDelleteCompany.exec_()