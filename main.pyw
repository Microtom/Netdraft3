import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import (QAction, QActionGroup, QApplication, QMainWindow)

class MainWindow(QMainWindow):
	
	def __init__(self, parent=None):
	
		super(MainWindow, self).__init__(parent)
		self.setWindowTitle("Netdraft 3")
		
		self.initUI()
		
	def initUI(self):
	
		menu = self.menuBar()
		fileMenu = menu.addMenu("&File")

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
