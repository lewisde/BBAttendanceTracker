from PyQt5 import QtWidgets
from PyQt5 import QtNetwork
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog

from attendance import Ui_MainWindow
from dialog import Ui_Dialog

from datetime import datetime
from datetime import timedelta
import sys
import os


class mywindow(QtWidgets.QMainWindow):

	bb_address = "https://blackboard.olivetcollege.edu"
	late_threshold = 10

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
		self.ui.actionEditAddress.triggered.connect(self.Edit_BB_Address)
		self.ui.actionEditLate.triggered.connect(self.Edit_Late_Threshold)
		self.ui.actionQuit.triggered.connect(self.quit)

	def Edit_BB_Address(self):
		self.dialog = QDialog(self)
		self.dialog.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)
		self.dialog.buttonBox.setGeometry(QtCore.QRect(0, 50, 340, 32))
		self.dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.dialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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

	def BBreject(self): self.dialog.done(0)

	def Edit_Late_Threshold(self):
		self.dialog = QDialog(self)
		self.dialog.buttonBox = QtWidgets.QDialogButtonBox(self.dialog)
		self.dialog.buttonBox.setGeometry(QtCore.QRect(0, 50, 340, 32))
		self.dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.dialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
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
		start_time = self.ui.txtStartTime.text().split(":")
		minutes = start_time[1].split()
		self.ui.txtLateTime.setText(str(start_time[0] + ":" + str(int(minutes[0]) + self.late_threshold)) + " " + minutes[1])
		self.ui.actionEditLate.setText(str(self.late_threshold) + " minutes")
		self.dialog.done(0)

	def late_reject(self): self.dialog.done(0)

	def quit(self): sys.exit()

	def onBtnLogin(self, event):
		loginurl = self.bb_address + "/learn/api/public/v1/oauth2/token"
		username = self.ui.txtUsername.text()
		password = self.ui.txtPassword.text()
		self.ui.txtUsername.clear()
		self.ui.txtPassword.clear()
		print(username,password)


if __name__ == "__main__":
	# secrets = {}
	# with open("offline", "r") as f:
	# 	keys = f.readline().strip().split(",")
	# 	values = f.readline().strip().split(",")
	# 	secrets = dict(zip(keys, values))

	app = QtWidgets.QApplication([])
	application = mywindow()
	application.show()
	sys.exit(app.exec())