from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from UI import Ui_mainWindow


class Test(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw = False
        self.pushButton.clicked.connect(self.circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)

    def run(self, qp):
        if self.draw:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            x = random.randint(20, 250)
            y = random.randint(30, 250)
            h = random.randint(20, 100)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(x, y, h, h)
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