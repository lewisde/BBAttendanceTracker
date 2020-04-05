from PyQt5 import QtWidgets
from PyQt5 import QtNetwork
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog

from attendance import Ui_MainWindow
# from dialog import Ui_Dialog

from datetime import datetime
from datetime import timedelta
import sys
import os


class mywindow(QtWidgets.QMainWindow):

    bb_address = ""
    late_threshold = 0
    app_key = ""
    secret = ""
    app_id = ""

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.ui.btnLogin.clicked.connect(self.onBtnLogin)
        self.ui.comboClasses.currentTextChanged.connect(self.selectClass)
        self.ui.btnSubmit.clicked.connect(self.uploadAttendance)
        self.ui.btnLogout.clicked.connect(self.logout)
        self.ui.actionEditAddress.triggered.connect(self.Edit_BB_Address)
        self.ui.actionEditLate.triggered.connect(self.Edit_Late_Threshold)
        self.ui.actionQuit.triggered.connect(self.quit)

        with open("offline", "r") as f:
            d = {}
            a = []
            for line in f.readlines():
                a = line.strip().split(":")
                d[a[0]] = a[1]
        self.bb_address = d['bb_address']
        self.late_threshold = int(d["late_threshold"])
        self.app_key = d["app_key"]
        self.app_id = d["app_id"]
        self.secret = d["secret"]
        self.ui.actionEditAddress.setText(self.bb_address)
        self.ui.actionEditLate.setText(str(self.late_threshold) + " minutes")
        self.ui.txtLateTime.setText(
            self.update_time_display(self.late_threshold))
        self.ui.txtEndTime.setText(self.update_time_display(80))

    def closeEvent(self, event):
        with open("offline", "w") as f:
            f.write(f"bb_address:{self.bb_address}\n")
            f.write(f"late_threshold:{self.late_threshold}\n")
            f.write(f"app_key:{self.app_key}\n")
            f.write(f"app_id:{self.app_id}\n")
            f.write(f"secret:{self.secret}\n")

    def update_time_display(self, difference):
        start_time = self.ui.txtStartTime.text().split(":")
        now = datetime.now()
        start_hour = int(start_time[0])
        start_minute = int(start_time[1].split(" ")[0])
        now = datetime
        ampm = start_time[1].split(" ")[1]
        length = self.late_threshold
        latehour = start_hour + (difference // 60)
        lateminute = start_minute + (difference % 60)
        latehour += lateminute // 60
        if latehour > 11:
            ampm = "PM"
        else:
            ampm = "AM"
        lateminute = lateminute % 60
        latehour = latehour % 24
        if latehour < 1:
            latehour = 1
            ampm = "AM"

        time = f"{latehour}:{lateminute:02} {ampm}"
        return(time)

    def Edit_BB_Address(self):
        self.dialog = QDialog(self)
        self.dialog.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)
        self.dialog.buttonBox.setGeometry(QtCore.QRect(0, 50, 340, 32))
        self.dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialog.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.dialog.buttonBox.setObjectName("buttonBox")
        self.dialog.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.dialog.lineEdit.setGeometry(QtCore.QRect(30, 20, 271, 21))
        self.dialog.lineEdit.setObjectName("lineEdit")
        self.dialog.lineEdit.setText(self.bb_address)
        self.dialog.buttonBox.accepted.connect(self.BBaccept)
        self.dialog.buttonBox.rejected.connect(self.BBreject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.exec_()

    def BBaccept(self):
        self.bb_address = self.dialog.lineEdit.text()
        self.ui.actionEditAddress.setText(self.bb_address)
        self.dialog.done(0)

    def BBreject(self):
        self.dialog.done(0)

    def Edit_Late_Threshold(self):
        self.dialog = QDialog(self)
        self.dialog.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)
        self.dialog.buttonBox.setGeometry(QtCore.QRect(0, 50, 340, 32))
        self.dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialog.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.dialog.buttonBox.setObjectName("buttonBox")
        self.dialog.lineEdit = QtWidgets.QLineEdit(self.dialog)
        self.dialog.lineEdit.setGeometry(QtCore.QRect(30, 20, 271, 21))
        self.dialog.lineEdit.setObjectName("lineEdit")
        self.dialog.lineEdit.setText(str(self.late_threshold))
        self.dialog.buttonBox.accepted.connect(self.late_accept)
        self.dialog.buttonBox.rejected.connect(self.late_reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.exec_()

    def late_accept(self):
        self.late_threshold = int(self.dialog.lineEdit.text())
        self.ui.txtLateTime.setText(self.update_time_display(self.late_threshold))
        self.ui.actionEditLate.setText(str(self.late_threshold) + " minutes")
        self.dialog.done(0)

    def late_reject(self):
        self.dialog.done(0)

    def quit(self):
        sys.exit()

    def onBtnLogin(self, event):
        loginurl = "https://" + self.bb_address + "/learn/api/public/v1/oauth2/token"
        print(loginurl)
        username = self.ui.txtUsername.text()
        password = self.ui.txtPassword.text()
        self.ui.txtUsername.clear()
        self.ui.txtPassword.clear()
        print(username, password)

    def selectClass(self, event):
        print(self.ui.comboClasses.currentText())

    def uploadAttendance(self, event):
        print("uploading")

    def logout(self, event):
        print("logging out")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
