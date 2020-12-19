from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox

from admin.appendCompanyDesing import Ui_appendCompany
import sqlite3

import re

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

# проверка нету ли в бд таких компаний
def chek(table, nameCompany, innCompany, adressCompany ):

    cursor.execute(f"SELECT * FROM {table} ")

    res = cursor.fetchall()

    flag = False
    for i in res:
        if i[1] == nameCompany or i[2] == innCompany or i[2] == adressCompany:
            flag = True
    return flag


# Проверка ИНН
def chekInn(inn):
    return bool(re.match(r"^([0-9]{4}-[0-9]{4}-[0-9]{2})$", inn))


def windowAppendCompany ():
    global windowAppendCompany
    windowAppendCompany= QtWidgets.QDialog()
    ui = Ui_appendCompany()
    ui.setupUi(windowAppendCompany)
    # функция регистрации компаниий
    def addCompany():
        nameCompany = ui.lineEditNameCompany.text().strip()
        innCompany = ui.lineEditInn.text()
        adressCompany = f"г. {ui.lineEditCity.text().strip()} ул. {ui.lineEditNameStreet.text().strip()} д. {ui.lineEditNameHouse.text().strip()}"
        #проверка на пустые строки
        if not ui.lineEditCity.text().strip():
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Введите город")
            x = msg.exec_()
        elif not ui.lineEditNameStreet.text().strip():
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Введите улицу")
            x = msg.exec_()
        elif not ui.lineEditNameHouse.text().strip():
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Введите дом")
            x = msg.exec_()
        elif (ui.lineEditNameHouse.text().strip().isnumeric() == False) or (int(ui.lineEditNameHouse.text().strip()) < 0) :
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некорректный номер дома")
            x = msg.exec_()
        elif not nameCompany:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Введите имя компании")
            x = msg.exec_()
        else:
            try:
                if chek("firms", nameCompany, innCompany, adressCompany):
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Компания уже зарегистрирована")
                    x = msg.exec_()
                else:
                    if chekInn(innCompany):
                        # добавление
                        cursor.execute(f"INSERT INTO firms (nameCompany, innCompany, adressCompany) VALUES ('{nameCompany}', '{innCompany}','{adressCompany}')")
                        db.commit()

                        msg = QMessageBox()
                        msg.setWindowTitle("Добавлено")
                        msg.setIcon(QMessageBox.Information)
                        msg.setText(f"{nameCompany} зарегистрирована")
                        x = msg.exec_()
                        windowAppendCompany.close()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Ошибка")
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Некорректный ИНН")
                        x = msg.exec_()
            except sqlite3.IntegrityError:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Компания уже зарегистрирована")
                x = msg.exec_()
    ui.addCompany.clicked.connect(addCompany)

    windowAppendCompany.show()

    return windowAppendCompany.exec_()
