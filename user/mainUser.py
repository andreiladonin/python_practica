import csv

from PySide2 import QtWidgets
from PySide2.QtWidgets import QTableWidgetItem

from user.menuUser import Ui_MenuAdnin
from admin.appendCompany import *
from admin.windowAppendContract import windowAppendContract
from admin.windowAddOrChangeAct import windowDellOrChangedAct
from admin.windowChangedAct import windowChangedAct

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

# Проверка ИНН
def chekInn(inn):
    return bool(re.match(r"^([0-9]{4}-[0-9]{4}-[0-9]{2})$", inn))

def chekCompany(company):
    cursor.execute(f"SELECT * FROM firms")
    res = cursor.fetchall()
    listCompany = []
    for i in res:
        listCompany.append(i[1])
    if company in listCompany:
        return True
    else:
        return False

# ф-ия проверки суммы
def SummaChek(summa):
    flag = False
    if summa.isnumeric():
        if float(summa) > 0:
            flag = True
    return flag

def usersMenu():
    global UserMenu
    UserMenu = QtWidgets.QDialog()

    def updateTableFirms():

        cursor.execute("SELECT * FROM firms")
        res = cursor.fetchall()
        ui.tableDirectory.setRowCount(0)

        for row_number, row_data in enumerate(res):
            ui.tableDirectory.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.tableDirectory.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def updateTableContracts ():
        cursor.execute("SELECT * FROM contracts")
        res = cursor.fetchall()
        ui.tableContact.setRowCount(0)

        for row_number, row_data in enumerate(res):
            ui.tableContact.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.tableContact.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def updateTableAct ():
        cursor.execute("SELECT * FROM acts")
        res = cursor.fetchall()
        ui.tableAct.setRowCount(0)

        for row_number, row_data in enumerate(res):
            ui.tableAct.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui.tableAct.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    ui = Ui_MenuAdnin()
    ui.setupUi(UserMenu)

    def appendCompany():
        x = windowAppendCompany()
        if x == 0:
            updateTableFirms()
    # ф-я на изменения в таблице компаний
    def changedTblCompany():

        tbl = []
        # получение таблицы в массив
        for i in range(ui.tableDirectory.rowCount()):
            row = []
            flag = True
            for j in range(ui.tableDirectory.columnCount()):

                nameCompany = ui.tableDirectory.item(i, 1).text().title().strip()
                adressCompany = ui.tableDirectory.item(i, 3).text().title().strip()
                # проверка на пустоту ячеек
                if not nameCompany:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f"Заполните имя компаннии где id {ui.tableDirectory.item(i, 0).text()}")
                    x = msg.exec_()
                    tbl = []
                    flag = False
                    break
                if not adressCompany:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f"Заполните адресс компаннии {ui.tableDirectory.item(i, 1).text()}")
                    x = msg.exec_()
                    tbl = []
                    flag = False
                    break
                # если все правильно то добавляется в масив
                elif chekInn(ui.tableDirectory.item(i, 2).text()):
                    row.append(ui.tableDirectory.item(i, j).text())
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f"Некорректный ИНН в Компании {ui.tableDirectory.item(i, 1).text()}")
                    x = msg.exec_()
                    tbl = []
                    flag = False
                    break
            if flag == False:
                break
            else:
                tbl.append(row)
        # если массив не пустой то  добавляем изменение в бд
        if bool(tbl):
            cursor.execute(f"DELETE FROM firms")
            db.commit()
            for i in tbl:
                for j in i:
                    cursor.execute(f"INSERT or IGNORE INTO firms (nameCompany, innCompany, adressCompany) VALUES ('{i[1]}', '{i[2]}','{i[3]}')")
                    db.commit()
                    cursor.execute(f"UPDATE contracts SET nameCompany = '{i[1]}' WHERE idCompany = {int(i[0])}")
                    db.commit()
            updateTableFirms()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Изменения сохранены")
            x = msg.exec_()
            updateTableContracts()
    def loadWindowAppendContract():
            x = windowAppendContract()
            if x == 0:
                updateTableContracts()

        # ф-ия для  изменение таблицы договоров

    def changedTableContracts():
            tbl = []
            # получение таблицы в массив
            for i in range(ui.tableContact.rowCount()):
                row = []
                flag = True
                for j in range(ui.tableContact.columnCount()):

                    nameCompany = ui.tableContact.item(i, 2).text().strip()
                    workCompany = ui.tableContact.item(i, 3).text().strip()
                    sumWork = ui.tableContact.item(i, 4).text().strip()
                    # проверка на пустоту ячеек
                    if chekCompany(nameCompany)== False:
                        msg = QMessageBox()
                        msg.setWindowTitle("Ошибка")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(
                            f"Заполните имя компании из вкладки заказчиков компаннии где № договора {ui.tableContact.item(i, 0).text()}")
                        x = msg.exec_()
                        tbl = []
                        flag = False
                        break
                    if not workCompany:
                        msg = QMessageBox()
                        msg.setWindowTitle("Ошибка")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(f"Заполните цель {ui.tableContact.item(i, 2).text()}")
                        x = msg.exec_()
                        tbl = []
                        flag = False
                        break
                    if SummaChek(sumWork) == False:
                        msg = QMessageBox()
                        msg.setWindowTitle("Ошибка")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(f"Заполните сумму договора №  {ui.tableContact.item(i, 0).text()}")
                        x = msg.exec_()
                        tbl = []
                        flag = False
                        break
                    else:
                        row.append(ui.tableContact.item(i, j).text().strip())
                if flag == False:
                    break
                else:
                    tbl.append(row)

            if bool(tbl):
                # замена id  в массиве на тот который привязан данной компании
                cursor.execute(f"SELECT * FROM firms")
                res = cursor.fetchall()
                for i in res:
                    for j in tbl:
                        if i[1] == j[2]:
                            j[1] = i[0]
                # print(tbl)
                cursor.execute(f"DELETE FROM contracts")
                db.commit()
                for i in tbl:
                    cursor.execute(
                        f"INSERT or IGNORE INTO contracts (idCompany, nameCompany, workCompany, summaContract) VALUES ({int(i[1])}, '{i[2]}','{i[3]}', '{i[4]}')")
                    db.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"Изменения сохранены")
                x = msg.exec_()
                updateTableContracts()

    def loadWindowAct():
        x = windowDellOrChangedAct()
        if x == 0:
            updateTableAct()

    def loadWindowChangedAct():
        x = windowChangedAct()
        if x == 0:
            updateTableAct()

    updateTableAct()
    updateTableFirms()
    updateTableContracts()

    def ecsportCSVCompany():
        cursor.execute(f"SELECT * FROM firms ")
        res = cursor.fetchall()
        file = open("firms.csv", "w")

        test = [["Имя Компании", "Инн", "Адрес"]]


        for i in res:
            ar = [str(i[1]), i[2], i[3]]
            test.append(ar)

        with file:
            write = csv.writer(file, delimiter=";")
            write.writerows(test)
        msg = QMessageBox()
        msg.setWindowTitle("Успешно")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Файл сохранен")
        x = msg.exec_()


    def ecsportCSVContracts():
        cursor.execute(f"SELECT * FROM contracts ")
        res = cursor.fetchall()
        file = open("contracts.csv", "w")

        test = [["ID Договора","ID Компании", "Цель Договора", "Сумма по Договору"]]


        for i in res:
            ar = [i[0],str(i[1]), i[2], i[3]]
            test.append(ar)

        with file:
            write = csv.writer(file, delimiter=";")
            write.writerows(test)
        msg = QMessageBox()
        msg.setWindowTitle("Успешно")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Файл сохранен")
        x = msg.exec_()

    def ecsportCSVActs():
        cursor.execute(f"SELECT * FROM acts ")
        res = cursor.fetchall()
        file = open("acts.csv", "w")

        test = [["№ акта", "№ договора", "Сумма по акту", "Дата подписания"]]

        for i in res:
            ar = [i[0], str(i[1]), i[2], i[3]]
            test.append(ar)

        with file:
            write = csv.writer(file, delimiter=";")
            write.writerows(test)
        msg = QMessageBox()
        msg.setWindowTitle("Успешно")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Файл сохранен")
        x = msg.exec_()

    ui.addDirectory.clicked.connect(appendCompany)
    ui.changeDirectory.clicked.connect(changedTblCompany)
    ui.importSpravochnik.clicked.connect(ecsportCSVCompany)

    ui.addContact.clicked.connect(loadWindowAppendContract)
    ui.changeContact.clicked.connect(changedTableContracts)
    ui.importContract.clicked.connect(ecsportCSVContracts)

    ui.addAct.clicked.connect(loadWindowAct)
    ui.changeAct.clicked.connect(loadWindowChangedAct)
    ui.importAct.clicked.connect(ecsportCSVActs)
    UserMenu.show()

