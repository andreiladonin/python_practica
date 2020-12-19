import sqlite3

from PyQt5.QtWidgets import QMessageBox
from PySide2 import QtWidgets
from admin.windowAppendContractDesing import Ui_AppendContract

db = sqlite3.connect("Baza.db")

cursor = db.cursor()


def windowAppendContract():
    global addContract
    addContract = QtWidgets.QDialog()
    ui = Ui_AppendContract()
    ui.setupUi(addContract)

    cursor.execute(f"SELECT * FROM firms ")
    res = cursor.fetchall()

    def getIDCompany(nameCompany):
        for i in res:
            if i[1] == nameCompany:
                return  i[0]

    # цикл добавлений компаний в комбобох из бд
    for i in res:
        ui.comboBox.addItem(i[1])
    # добавление контрактов
    def addContractCompany():

        company = ui.comboBox.currentText()
        purposeWork = ui.lineEditPurpose.text().strip()
        summaWork = ui.lineEditSum.text().strip()

        if not purposeWork:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Укажите цель работ")
            x = msg.exec_()
        elif not summaWork:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Укажите сумму договора")
            x = msg.exec_()
        else:
            try:
                idCompany = getIDCompany(company)
                if float(summaWork) > 0:
                    summaWork = int(summaWork)
                    summaWork = str(summaWork)
                    cursor.execute(f"INSERT INTO contracts (idCompany, nameCompany, workCompany, summaContract) VALUES ({idCompany}, '{company}', '{purposeWork}', '{summaWork}' )")
                    db.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle("Успешно")
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Добавлен договор")
                    x = msg.exec_()
                    addContract.close()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введена не правильная сумма договора ")
                    x = msg.exec_()
            except ValueError:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Введена не правильная сумма договора ")
                x = msg.exec_()

    ui.apendContract.clicked.connect(addContractCompany)

    return addContract.exec_()