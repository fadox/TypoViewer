# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../windows/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 801)
        font = QtGui.QFont()
        font.setPointSize(72)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelectFiles = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectFiles.setIcon(icon1)
        self.actionSelectFiles.setObjectName("actionSelectFiles")
        self.actionClearList = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearList.setIcon(icon2)
        self.actionClearList.setObjectName("actionClearList")
        self.actionDeleteItems = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/file_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteItems.setIcon(icon3)
        self.actionDeleteItems.setObjectName("actionDeleteItems")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon4)
        self.actionSettings.setObjectName("actionSettings")
        self.toolBar.addAction(self.actionSelectFiles)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDeleteItems)
        self.toolBar.addAction(self.actionClearList)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSelectFiles.setText(_translate("MainWindow", "Select Files"))
        self.actionSelectFiles.setToolTip(_translate("MainWindow", "Select Files"))
        self.actionClearList.setText(_translate("MainWindow", "Clear List"))
        self.actionClearList.setToolTip(_translate("MainWindow", "Clear List"))
        self.actionDeleteItems.setText(_translate("MainWindow", "Delete Items"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

import TypoViewer.resources.icons_db
import TypoViewer.resources.samples
