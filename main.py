from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import QtWidgets
from stt import STT
from ui import *
from app import *


if __name__ == "__main__":   
    import sys      
    app = QtWidgets.QApplication(sys.argv [1:])    
    ui = app_ui()
    ui.show()
    
    
    sys.exit(app.exec())
   

