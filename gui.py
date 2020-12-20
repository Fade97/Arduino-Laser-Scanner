from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QScrollArea
from PyQt5.QtGui import QImage, QPixmap, QPainter
from QImageViewer import QImageViewer


class lsApp:
    def __init__(self):
        self.app = QApplication([])
        self.mainWindow = QImageViewer()
        self.mainWindow.setWindowTitle('Arduino Laser Scanner')
        self.mainWindow.show()
        self.app.exec_()
