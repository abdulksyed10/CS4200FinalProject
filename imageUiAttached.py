'''from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from imageUi import Ui_MainWindow

class imageUiAttached(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

        self.submitBtn.clicked.connect(self.submitBtnClicked)
    
    def submitBtnClicked(self):
        self.outputTxt.setText("Hello, you still got a lot more things to do!!!")
'''