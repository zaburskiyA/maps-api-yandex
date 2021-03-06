import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from mapsUI import SearchWindow, MapWindow
from request_by_coords import request, get_coord


class Main(QMainWindow, SearchWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_map)
        self.pushButton_2.clicked.connect(self.show_map)
        self.radioButton.clicked.connect(self.change_map_type)
        self.radioButton_2.clicked.connect(self.change_map_type)
        self.radioButton_3.clicked.connect(self.change_map_type)
        self.maps = []
        self.map_types = {'схема': 'map', 'спутник': 'sat', 'гибрид': 'sat,skl'}

    def show_map(self):
        sender = self.sender()
        map = Map()
        self.map_type = map.map_type
        self.maps.append(map)
        if sender is not None and sender.text() == 'Найти':
            map.coords = (self.lineEdit_2.text(), self.lineEdit.text())
        elif sender is not None and sender.text() == 'Поиск по адресу':
            map.coords = get_coord(self.lineEdit_3.text())
        map.show_map()
        map.show()

    def change_map_type(self):
        text = self.sender().text()
        self.map_type = self.map_types[text]
        print(self.map_type)


class Map(QMainWindow, MapWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.size = 0.5
        self.coords = (0, 0)
        self.map_type = 'map'
        self.first = True

    def show_map(self):
        map_file = request(self.coords, self.size, self.map_type, self.first)
        self.pixmap = QPixmap(map_file)
        self.label.setPixmap(self.pixmap)
        self.update()
        print(map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown and self.size <= 90 / 1.1:
            self.size *= 1.1
            self.show_map()
        elif event.key() == Qt.Key_PageUp and self.size >= 0.001:
            self.size *= 0.91
            self.show_map()
        elif event.key() == Qt.Key_Up:
            l1, l2 = self.coords
            self.coords = (float(l1), (float(l2) + self.size + 90) % 180 - 90)
            self.first = False
            self.show_map()
        elif event.key() == Qt.Key_Down:
            l1, l2 = self.coords
            self.coords = (float(l1), (float(l2) - self.size + 90) % 180 - 90)
            self.first = False
            self.show_map()
        elif event.key() == Qt.Key_Right:
            l1, l2 = self.coords
            self.coords = ((float(l1) + self.size + 180) % 360 - 180, float(l2))
            self.first = False
            self.show_map()
        elif event.key() == Qt.Key_Left:
            l1, l2 = self.coords
            self.coords = ((float(l1) - self.size + 180) % 360 - 180, float(l2))
            self.first = False
            self.show_map()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
