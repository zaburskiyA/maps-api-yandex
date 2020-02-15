import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from mapsUI import MapsMainWindow

class Main(QMainWindow, MapsMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_map)

    def show_map(self):
        ll = ",".join([self.lineEdit.text(), self.lineEdit_2.text()])
        self.pixmap = QPixmap('map.png')
        self.label_4.setPixmap(self.pixmap)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())