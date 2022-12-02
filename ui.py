from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
        QInputDialog,QFileDialog,QMessageBox)
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QMutex, QObject, QThread, pyqtSignal
from pathlib import Path
import sys
from stt import STT
import threading


# def thread(my_func):
#     def wrapper(*args, **kwargs):
#         my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
#         my_thread.start()
#     return wrapper


# @thread
# def stt_thread():
#      global stt
#      global unlock
#      unlock=False
#      stt=STT()     
#      unlock=True    

class app_ui(QWidget):
    
    def __init__(self):
        super().__init__()
        self.LoadFileButton = QPushButton(self)
        self.LoadFileButton.setEnabled(False)      
        self.LoadFileButton.setGeometry(QtCore.QRect(10, 0, 121, 31))
        self.LoadFileButton.setObjectName("LoadFileButton")
        self.LoadFileButton.setCheckable(True)
        self.LoadFileButton.clicked.connect(self.SelectFileDialog)
        
        
        self.StartButton = QtWidgets.QPushButton(self)        
        self.StartButton.setGeometry(QtCore.QRect(140, 0, 141, 31))
        self.StartButton.setObjectName("StartButton")
        self.ResultTextEditBox = QtWidgets.QPlainTextEdit(self)
        self.ResultTextEditBox.setGeometry(QtCore.QRect(10, 30, 571, 551))

        self.LabelInform = QtWidgets.QLabel(self)
        self.LabelInform.setGeometry(QtCore.QRect(590, 10, 90, 15))
        self.LabelInform.setObjectName("LabelInform")

        self.LogTextBrowser = QtWidgets.QTextBrowser(self)
        self.LogTextBrowser.setGeometry(QtCore.QRect(585, 31, 471, 551))

        self.initUI()
        self.threads = [] 

    def initUI(self):      
        self.setGeometry(300, 300, 1060, 600)
        self.setWindowTitle('stt-executable')
        qtRectangle = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        self.SetTextUi()
        self.show()


    def SetTextUi(self):
        _SetText = QtCore.QCoreApplication.translate
        self.setWindowTitle(_SetText("stt-executable", "stt-executable"))
        self.LoadFileButton.setText(_SetText("select", "Выбрать файл"))
        self.StartButton.setText(_SetText("tranform", "Преобразовать"))
        self.LabelInform.setText(_SetText("info", "Информация:"))   
     
    def createThread(self, audio_file):
        thread = QThread()
        global stt
        stt= STT()
        stt.moveToThread(thread)    
        return thread


    def SelectFileDialog(self):         
        home_dir = str(Path.home())
        file_name = QFileDialog.getOpenFileName(self, 'Open file', home_dir,"Sound files (*.ogg *.wav *.mp3 *.mp4 *.avi)")
        global stt
        global unlock        
        print(unlock)
        if file_name[0]:
            if unlock==True:          
                l=(stt.audio_to_text(file_name[0]))
                f = open(str(file_name[0])+"-stt-executable.txt", 'w',encoding="utf-8")      
                for index in l:
                    f.write(index)
                f.close()
                f = open(str(file_name[0])+"-stt-executable.txt",encoding="utf-8")                
                ReadyText = f.read()                
                #self.ResultTextEditBox.clear()
                self.ResultTextEditBox.appendPlainText(file_name[0]+"\n"+ReadyText+" \n ")
                f.close()                          
    
          