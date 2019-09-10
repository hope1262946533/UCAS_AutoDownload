# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 494)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 231, 23))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.userName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.userName.setObjectName("userName")
        self.horizontalLayout.addWidget(self.userName)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passwd = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.passwd.setObjectName("passwd")
        self.horizontalLayout_2.addWidget(self.passwd)
        self.logInfo = QtWidgets.QTextEdit(Dialog)
        self.logInfo.setGeometry(QtCore.QRect(260, 12, 171, 112))
        self.logInfo.setObjectName("logInfo")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 60, 231, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.certImage = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_3)
        self.certImage.setMaximumSize(QtCore.QSize(150, 32))
        self.certImage.setObjectName("certImage")
        self.horizontalLayout_3.addWidget(self.certImage)
        self.certCode = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.certCode.setMaximumSize(QtCore.QSize(150, 20))
        self.certCode.setText("")
        self.certCode.setObjectName("certCode")
        self.horizontalLayout_3.addWidget(self.certCode)
        self.coursesList = QtWidgets.QListWidget(Dialog)
        self.coursesList.setGeometry(QtCore.QRect(20, 220, 411, 121))
        self.coursesList.setObjectName("coursesList")
        self.hintInfo = QtWidgets.QLabel(Dialog)
        self.hintInfo.setGeometry(QtCore.QRect(170, 200, 121, 16))
        self.hintInfo.setText("")
        self.hintInfo.setObjectName("hintInfo")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 162, 411, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.getCourses = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.getCourses.setObjectName("getCourses")
        self.horizontalLayout_5.addWidget(self.getCourses)
        self.downloadAll = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.downloadAll.setObjectName("downloadAll")
        self.horizontalLayout_5.addWidget(self.downloadAll)
        self.refreshCertCode = QtWidgets.QPushButton(Dialog)
        self.refreshCertCode.setGeometry(QtCore.QRect(95, 100, 91, 31))
        self.refreshCertCode.setObjectName("refreshCertCode")
        self.choosePath = QtWidgets.QPushButton(Dialog)
        self.choosePath.setGeometry(QtCore.QRect(15, 132, 120, 25))
        self.choosePath.setMaximumSize(QtCore.QSize(120, 25))
        self.choosePath.setObjectName("choosePath")
        self.showPath = QtWidgets.QLabel(Dialog)
        self.showPath.setGeometry(QtCore.QRect(140, 126, 291, 41))
        self.showPath.setText("")
        self.showPath.setObjectName("showPath")
        self.remPasswd = QtWidgets.QCheckBox(Dialog)
        self.remPasswd.setGeometry(QtCore.QRect(20, 103, 116, 23))
        self.remPasswd.setObjectName("remPasswd")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(185, 100, 71, 31))
        self.loginButton.setObjectName("loginButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 350, 411, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressInfo = QtWidgets.QTextBrowser(Dialog)
        self.progressInfo.setGeometry(QtCore.QRect(20, 380, 411, 101))
        self.progressInfo.setObjectName("progressInfo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.getCourses.setText(_translate("Dialog", "查询课程"))
        self.downloadAll.setText(_translate("Dialog", "下载并更新"))
        self.refreshCertCode.setText(_translate("Dialog", "刷新验证码"))
        self.choosePath.setText(_translate("Dialog", "选择下载文件夹"))
        self.remPasswd.setText(_translate("Dialog", "记住密码"))
        self.loginButton.setText(_translate("Dialog", "登陆"))
