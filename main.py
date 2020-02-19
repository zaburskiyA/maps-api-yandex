import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from mapsUI import MapsMainWindow
from request_by_coords import request, get_coord


class Main(QMainWindow, MapsMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_map)
        self.pushButton_2.clicked.connect(self.show_map)
        #self.map.clicked.connect(self.change_l)
        #self.sat.clicked.connect(self.change_l)
        #self.gibrid.clicked.connect(self.change_l)
        self.size = 0.5
        self.coords = (0, 0)
        self.l = "map"

    def show_map(self):
        sender = self.sender()
        if sender is not None and sender.text() == 'Найти':
            self.coords = (self.lineEdit_2.text(), self.lineEdit.text())
        elif sender is not None and sender.text() == 'Поиск по адресу':
            self.coords = get_coord(self.lineEdit_3.text())
        map_file = request(self.coords, self.size, self.l)
        self.pixmap = QPixmap(map_file)
        self.label_4.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            self.size *= 1.1
            self.show_map()
        if event.key() == Qt.Key_PageUp:
            self.size *= 0.91
            self.show_map()

    def change_l(self):
        sender = self.sender().text()
        if sender == "схема":
            self.l = "map"
        elif sender == "спутник":
            self.l = "sat"
        elif sender == "гибрид":
            self.l = "sat,skl"
        self.show_map()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
