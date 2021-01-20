import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a, b = randint(0, 300), randint(0, 460)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(a, a, b, b)
        a, b = randint(0, 300), randint(0, 460)
        qp.drawEllipse(a, a, b, b)
        a, b = randint(0, 300), randint(0, 460)
        qp.drawEllipse(a, a, b, b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


