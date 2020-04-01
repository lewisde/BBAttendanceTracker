# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 1067)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.leftSide = QtWidgets.QVBoxLayout()
        self.leftSide.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.leftSide.setSpacing(20)
        self.leftSide.setObjectName("leftSide")
        self.upperLayout = QtWidgets.QVBoxLayout()
        self.upperLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.upperLayout.setSpacing(10)
        self.upperLayout.setObjectName("upperLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.upperLayout.addItem(spacerItem)
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.upperLayout.addWidget(self.txtUsername)
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtPassword.setFont(font)
        self.txtPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.upperLayout.addWidget(self.txtPassword)
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.upperLayout.addWidget(self.btnLogin)
        self.leftSide.addLayout(self.upperLayout)
        self.middleLayout = QtWidgets.QVBoxLayout()
        self.middleLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.middleLayout.setSpacing(5)
        self.middleLayout.setObjectName("middleLayout")
        self.comboClasses = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboClasses.setFont(font)
        self.comboClasses.setObjectName("comboClasses")
        self.middleLayout.addWidget(self.comboClasses)
        self.startLayout = QtWidgets.QHBoxLayout()
        self.startLayout.setObjectName("startLayout")
        self.lblStartTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStartTime.sizePolicy().hasHeightForWidth())
        self.lblStartTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblStartTime.setFont(font)
        self.lblStartTime.setObjectName("lblStartTime")
        self.startLayout.addWidget(self.lblStartTime)
        self.txtStartTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtStartTime.sizePolicy().hasHeightForWidth())
        self.txtStartTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtStartTime.setFont(font)
        self.txtStartTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtStartTime.setObjectName("txtStartTime")
        self.startLayout.addWidget(self.txtStartTime)
        self.middleLayout.addLayout(self.startLayout)
        self.lateLayout = QtWidgets.QHBoxLayout()
        self.lateLayout.setObjectName("lateLayout")
        self.lblLateTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLateTime.sizePolicy().hasHeightForWidth())
        self.lblLateTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblLateTime.setFont(font)
        self.lblLateTime.setObjectName("lblLateTime")
        self.lateLayout.addWidget(self.lblLateTime)
        self.txtLateTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtLateTime.sizePolicy().hasHeightForWidth())
        self.txtLateTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtLateTime.setFont(font)
        self.txtLateTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtLateTime.setObjectName("txtLateTime")
        self.lateLayout.addWidget(self.txtLateTime)
        self.middleLayout.addLayout(self.lateLayout)
        self.endLayout = QtWidgets.QHBoxLayout()
        self.endLayout.setObjectName("endLayout")
        self.lblEndTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblEndTime.sizePolicy().hasHeightForWidth())
        self.lblEndTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblEndTime.setFont(font)
        self.lblEndTime.setObjectName("lblEndTime")
        self.endLayout.addWidget(self.lblEndTime)
        self.txtEndTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtEndTime.sizePolicy().hasHeightForWidth())
        self.txtEndTime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtEndTime.setFont(font)
        self.txtEndTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtEndTime.setObjectName("txtEndTime")
        self.endLayout.addWidget(self.txtEndTime)
        self.middleLayout.addLayout(self.endLayout)
        self.leftSide.addLayout(self.middleLayout)
        self.bottomLayout = QtWidgets.QVBoxLayout()
        self.bottomLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.bottomLayout.setContentsMargins(-1, -1, -1, 0)
        self.bottomLayout.setSpacing(25)
        self.bottomLayout.setObjectName("bottomLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bottomLayout.addItem(spacerItem1)
        self.btnSubmit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")
        self.bottomLayout.addWidget(self.btnSubmit)
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogout.sizePolicy().hasHeightForWidth())
        self.btnLogout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnLogout.setFont(font)
        self.btnLogout.setObjectName("btnLogout")
        self.bottomLayout.addWidget(self.btnLogout)
        self.leftSide.addLayout(self.bottomLayout)
        self.gridLayout.addLayout(self.leftSide, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 22))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.menuBBAttendanceTracker = QtWidgets.QMenu(self.menubar)
        self.menuBBAttendanceTracker.setObjectName("menuBBAttendanceTracker")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit_BB_Address = QtWidgets.QAction(MainWindow)
        self.actionEdit_BB_Address.setObjectName("actionEdit_BB_Address")
        self.menuBBAttendanceTracker.addAction(self.actionEdit_BB_Address)
        self.menubar.addAction(self.menuBBAttendanceTracker.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtUsername.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.txtPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "Login to Blackboard"))
        self.lblStartTime.setText(_translate("MainWindow", "Class Start Time"))
        self.txtStartTime.setText(_translate("MainWindow", "12:20 PM"))
        self.lblLateTime.setText(_translate("MainWindow", "Class Late Time"))
        self.txtLateTime.setText(_translate("MainWindow", "12:30 PM"))
        self.lblEndTime.setText(_translate("MainWindow", "Class End Time"))
        self.txtEndTime.setText(_translate("MainWindow", "1:40 PM"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit Attendance"))
        self.btnLogout.setText(_translate("MainWindow", "Logout of Blackboard"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Present"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Late"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Absent"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "53363"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "David"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Lewis"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "12:40 PM"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "12:50 PM"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "53314"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Susanne"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Lewis"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "1:50 PM"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "2:00 PM"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "X"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menuBBAttendanceTracker.setTitle(_translate("MainWindow", "BBAttendanceTracker"))
        self.actionEdit_BB_Address.setText(_translate("MainWindow", "Blackboard Address"))
