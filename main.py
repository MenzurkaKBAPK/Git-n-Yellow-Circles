from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5 import uic

from random import randint
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)
        self.label.setPixmap(QPixmap(800, 600))
        self.paint = False
        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        qp = QPainter(self.label.pixmap())
        qp.setBrush(QColor(255, 255, 0))

        R = randint(1, 50)
        x, y = randint(0, 800 - R), randint(0, 600 - R)
        qp.drawEllipse(x, y, R, R)

        qp.end()
        self.update()


def main() -> None:
    sys.excepthook = except_hook

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()