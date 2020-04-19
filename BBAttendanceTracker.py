from PyQt5 import QtWidgets
from PyQt5 import QtNetwork
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QFontDialog
from PyQt5.QtCore import QSettings

from attendance import Ui_MainWindow
# from dialog import Ui_Dialog

import loginDialog

from datetime import datetime
from datetime import timedelta
import sys
import os


class mywindow(QtWidgets.QMainWindow):

    bb_address = ""
    late_threshold = 0
    font = QtGui.QFont()
    app_key = ""
    secret = ""
    app_id = ""
    dialog = ""

    auth_path = "/learn/api/public/v1/oauth2/token"
    dsk_path = "/learn/api/public/v1/dataSources"
    term_path = "/learn/api/public/v1/terms"
    course_path = "/learn/api/public/v1/courses"
    user_path = "/learn/api/public/v1/users"

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
        self.ui.actionEditFontSize.triggered.connect(self.Edit_Font_Size)

        with open("offline", "r") as f:
            d = {}
            a = []
            for line in f.readlines()[:7]:
                a = line.strip().split(":")
                d[a[0]] = a[1]
        self.bb_address = d['bb_address']
        self.late_threshold = int(d["late_threshold"])
        self.font = QtGui.QFont(d["font"])
        self.font.setPointSize(int(d["font_size"]))
        self.Set_Font(self.font)
        self.app_key = d["app_key"]
        self.app_id = d["app_id"]
        self.secret = d["secret"]
        self.ui.actionEditAddress.setText(self.bb_address)
        self.ui.actionEditLate.setText(str(self.late_threshold) + " minutes")
        self.ui.actionEditFontSize.setText("Change Font")
        self.ui.txtLateTime.setText(
            self.update_time_display(self.late_threshold))
        self.ui.txtEndTime.setText(self.update_time_display(80))

    def closeEvent(self, event):
        with open("offline", "w") as f:
            f.write(f"bb_address:{self.bb_address}\n") 
            f.write(f"late_threshold:{self.late_threshold}\n")
            f.write(f"font:{self.font.toString()}\n")
            f.write(f"font_size:{self.font.pointSize()}\n")
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

    def Edit_Font_Size(self):
        font, ok = QFontDialog.getFont(self.font)
        self.font = font
        self.Set_Font(font)

    def Set_Font(self, font):
        self.ui.btnLogin.setFont(font)
        self.ui.lblStartTime.setFont(font)
        self.ui.txtStartTime.setFont(font)
        self.ui.lblLateTime.setFont(font)
        self.ui.txtLateTime.setFont(font)
        self.ui.lblEndTime.setFont(font)
        self.ui.txtEndTime.setFont(font)
        self.ui.btnSubmit.setFont(font)
        self.ui.btnLogout.setFont(font)
        self.ui.tableWidget.setFont(font)
        font.setPointSize(font.pointSize() - 1)
        self.ui.comboClasses.setFont(font)
        font.setPointSize(font.pointSize() + 1)

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
        with open("offline", "w") as f:
            f.write(f"bb_address:{self.bb_address}\n")
            f.write(f"late_threshold:{self.late_threshold}\n")
            f.write(f"font:{self.font.toString()}\n")
            f.write(f"font_size:{self.font.pointSize()}\n")            
            f.write(f"app_key:{self.app_key}\n")
            f.write(f"app_id:{self.app_id}\n")
            f.write(f"secret:{self.secret}\n")
        sys.exit()

    def onBtnLogin(self, event):
        self.dialog = QDialog(self)
        self.dialog.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)
        self.dialog.buttonBox.setGeometry(QtCore.QRect(0, 100, 340, 32))
        self.dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialog.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.dialog.buttonBox.setObjectName("buttonBox")
        self.txtUsername = QtWidgets.QLineEdit(self.dialog)
        self.txtUsername.setGeometry(QtCore.QRect(30, 20, 271, 21))
        self.txtUsername.setFont(self.font)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.setPlaceholderText("User Name")
        self.txtPassword = QtWidgets.QLineEdit(self.dialog)
        self.txtPassword.setGeometry(QtCore.QRect(30, 50, 271, 21))
        self.txtPassword.setFont(self.font)
        self.txtPassword.setInputMethodHints(
            QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|
            QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setPlaceholderText("Password")
        self.dialog.buttonBox.accepted.connect(self.processLogin)
        self.dialog.buttonBox.rejected.connect(self.PassReject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()


    def processLogin(self):
        # loginurl = "https://" + self.bb_address + self.auth_path
        # print(loginurl)
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        # self.ui.txtUsername.clear()
        # self.ui.txtPassword.clear()
        print(username, password)
        self.dialog.done(0)

    def PassReject(self):
        self.dialog.done(1)

    def selectClass(self, event):
        print(self.ui.comboClasses.currentText())

        # get list of students from selected class and populate TableView

    def uploadAttendance(self, event):
        print("uploading")

        # repackage tableview data and update BB

    def logout(self, event):
        print("logging out")

        # return token?


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
