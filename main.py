import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.flag = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        rad = randint(1, 250)
        qp.drawEllipse(100, 10, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MyWindow()
    wnd.show()
    sys.exit(app.exec())

