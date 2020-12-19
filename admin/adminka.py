from PySide2 import QtWidgets
from admin.desingAdminka import Ui_panelAdmin
import sqlite3
from PySide2.QtWidgets import QMessageBox

# adminka

db = sqlite3.connect("Baza.db")

cursor = db.cursor()

def chek(table, log ):

    cursor.execute(f"SELECT * FROM {table} ")

    res = cursor.fetchall()

    flag = False
    for i in res:
        if i[1] == log :
            flag = True

    return flag



def adminka():
    global admin
    admin = QtWidgets.QDialog()
    ui = Ui_panelAdmin()
    ui.setupUi(admin)

    #добавление аккаунта
    def addAccount():
        login = ui.login.toPlainText().strip()
        password = ui.password.toPlainText().strip()
        typeAccount = ui.typeAccount.currentText()

        if (not login):
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Проверьте введеность данных")
            x = msg.exec_()
        elif (not password):
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Проверьте введеность данных")
            x = msg.exec_()
        else:
            if chek("admins", login) or chek("users", login):
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Имя уже зарегистрировано")
                x = msg.exec_()
            else:
                if typeAccount == "Админ":
                    cursor.execute(f"INSERT INTO admins (login, password) VALUES ('{login}', '{password}')")
                    db.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle("Успешно")
                    msg.setText(f"{typeAccount} добавлен")
                    x = msg.exec_()
                else:
                    cursor.execute(f"INSERT INTO users (login, password) VALUES ('{login}', '{password}')")
                    db.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle("Успешно")
                    msg.setText(f"{typeAccount} добавлен")
                    x = msg.exec_()

    # удаление аккаунта
    def dellAccount():
        login = ui.login.toPlainText()

        if chek("admins", login):
            msg = QMessageBox()
            msg.setWindowTitle("Удаление")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText(f"Вы точно хотите удалить пользователя {login}")
            x = msg.exec_()

            if x == QMessageBox.Ok:
                cursor.execute(f"DELETE FROM admins WHERE login = '{login}'")
                db.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setText(f"{login} удален")
                x = msg.exec_()

        elif chek("users", login):
            msg = QMessageBox()
            msg.setWindowTitle("Удаление")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText(f"Вы точно хотите удалить пользователя {login}")
            x = msg.exec_()

            if x == QMessageBox.Ok:
                cursor.execute(f"DELETE FROM users WHERE login = '{login}'")
                db.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setText(f"{login} удален")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Пользователь {login} не найден")
            x = msg.exec_()

    ui.addAccount.clicked.connect(addAccount)

    ui.dellAccount.clicked.connect(dellAccount)
    admin.show()
