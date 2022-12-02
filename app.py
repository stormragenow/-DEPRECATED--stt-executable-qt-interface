from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Form(object):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1059, 582)
        Form.setMinimumSize(QtCore.QSize(1059, 582))
        Form.setMaximumSize(QtCore.QSize(1059, 582))
        self.LoadFileButton = QtWidgets.QPushButton(self)
        self.LoadFileButton.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.LoadFileButton.setObjectName("LoadFileButton")
        self.StartButton = QtWidgets.QPushButton(self)        
        self.StartButton.setGeometry(QtCore.QRect(140, 0, 141, 31))
        self.StartButton.setObjectName("StartButton")
        self.ResultTextEditBox = QtWidgets.QPlainTextEdit(Form)
        self.ResultTextEditBox.setGeometry(QtCore.QRect(10, 30, 571, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultTextEditBox.sizePolicy().hasHeightForWidth())
        self.ResultTextEditBox.setSizePolicy(sizePolicy)
        self.ResultTextEditBox.setAcceptDrops(True)
        self.ResultTextEditBox.setObjectName("ResultTextEditBox")
        self.LogTextBrowser = QtWidgets.QTextBrowser(self)
        self.LogTextBrowser.setGeometry(QtCore.QRect(585, 31, 471, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.LogTextBrowser.sizePolicy().hasHeightForWidth())
        self.LogTextBrowser.setSizePolicy(sizePolicy)
        self.LogTextBrowser.setObjectName("LogTextBrowser")
        self.LabelInform = QtWidgets.QLabel(self)
        self.LabelInform.setEnabled(True)
        self.LabelInform.setGeometry(QtCore.QRect(590, 10, 67, 13))
        self.LabelInform.setObjectName("LabelInform")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LoadFileButton.setText(_translate("Form", "Выбрать файл"))
        self.StartButton.setText(_translate("Form", "Преобразовать"))
        self.LabelInform.setText(_translate("Form", "Информация:"))    