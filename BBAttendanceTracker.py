from PyQt5 import QtWidgets
from PyQt5 import QtNetwork

# from attendance import Ui_Dialog
from untitled2 import Ui_MainWindow
import json
import sys
import os

class mywindow(QtWidgets.QMainWindow):

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

	def onBtnLogin(self, event):
		loginurl = "https://blackboard.olivetcollege.edu/learn/api/public/v1/oauth2/token"
		username = self.ui.txtUsername.text()
		password = self.ui.txtPassword.text()
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