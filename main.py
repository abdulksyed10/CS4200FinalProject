import sys
from PyQt5 import QtWidgets
import imageUiAttached

#needed to run the program
app = QtWidgets.QApplication(sys.argv)
imageUI_win = QtWidgets.QMainWindow()
imageUI_ui = imageUiAttached.imageUiAttached(imageUI_win)
app.exec_()