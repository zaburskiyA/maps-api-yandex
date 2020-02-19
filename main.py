import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from mapsUI import MapsMainWindow
from request_by_coords import request


class Main(QMainWindow, MapsMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_map)

    def show_map(self):
        size = 0.5
        map_file = request([self.lineEdit.text(), self.lineEdit_2.text()], size)
        self.pixmap = QPixmap(map_file)
        self.label_4.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
