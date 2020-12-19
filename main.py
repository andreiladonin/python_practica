import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
from vhod import Ui_Dialog
from modules import *
from user.mainUser import usersMenu
from admin.mainAdmin import adminMenu
#Create app
app = QtWidgets.QApplication(sys.argv)

#init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
db = sqlite3.connect('Baza.db')
sql = db.cursor()

db.commit()
#logika
ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

# аунтификация
def authentication ():
    login = ui.login.text()
    pasword = ui.password.text()

    # проверка
    admin = chek("admins", login, pasword)
    user = chek("users", login, pasword)

    if admin:
        # загрузка окна админа
        adminMenu()
        Dialog.close()
    elif user:
        # загрузка окна юзера
        usersMenu()
        Dialog.close()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        msg.setText("Вы в системе не зарегистрированы")
        x = msg.exec_()

ui.pushButton.clicked.connect(authentication)

#main loop
sys.exit(app.exec_())


