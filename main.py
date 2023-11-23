from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor, QPixmap

from random import randint
import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "круг"))


class MainWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.label.setPixmap(QPixmap(800, 600))
        self.paint = False
        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        qp = QPainter(self.label.pixmap())
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))

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
