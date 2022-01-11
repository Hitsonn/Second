from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)

    def run(self, qp):
        if self.draw:
            x = random.randint(20, 250)
            y = random.randint(30, 250)
            r = random.randint(20, 100)
            qp.setBrush(QColor(200, 200, 0))
            qp.drawEllipse(x, y, r, r)
            self.draw = False
            qp.end()

    def circle(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())