import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Snake(QWidget):
    score = 0
    x = 15
    y = 15

    def __init__(self):
        super(Snake, self).__init__()
        self.initUI()

    # Not default method. Just to make the constructor bit tidier.
    # It contains everything related to the window, and it's calling the NewGame method GOTO line ...
    def initUI(self):
        # setMouseTracking(True) will get the location of the curses when it hovers on the windows. When it is not
        # used you must press the left click and move the curser on the window for the system to detect it.
        self.setMouseTracking(True)
        self.highscore = 0
        self.newGame()
        self.setStyleSheet("QWidget { background: #FFFFFF }")
        self.setFixedSize(800, 800)
        self.setWindowTitle('Snake')
        self.show()

    # Default method name
    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        # ---- Place shapes you want to draw ---
        self.drawShape(qp)
        # ---- Do not place bellow ----
        qp.end()

    # Two option for window interaction, either use the mouse or the key input
    # Default method name.
    # Used to detect any external interaction
    def keyPressEvent(self, e):
        ...
        # # Key detection code
        # if e.key() == QtCore.Qt.Key_Up:
        #     self.y -=1
        # elif e.key() == QtCore.Qt.Key_Down:
        #     self.y += 1
        # elif e.key() == QtCore.Qt.Key_Left:
        #     self.x -= 1
        # elif e.key() == QtCore.Qt.Key_Right:
        #     self.x += 1

        # print(f"X={self.x} Y={self.y}")

    # Default method name.
    # Used to detect any external interaction
    def mouseMoveEvent(self, e):
        ...
        # self.y = e.y()
        # self.x = e.x()
        #
        # text = f'x: {self.y},  y: {self.x}'
        # print(text)

    # Not default method.
    def newGame(self):
        self.timer = QtCore.QBasicTimer()
        # This is the refresh speed of the frame super important GOTO line 79 ...
        # The greater the speed value is the lower the frame refresh rate is.
        self.speed = 1

        self.start()

    # Not default method.
    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

    # Not default method.
    def start(self):
        self.isPaused = False
        # ... This timer dictates the refresh speed of the frames
        self.timer.start(self.speed, self)
        self.update()

    # Not default method.
    # Could be used for auto move objects
    def update(self, ):
        ...
        # The code bellow is just to show how it is adding numbers
        #     self.score +=1
        #     print(self.score)

    # Not default method.
    def drawShape(self, qp):
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(QtGui.QColor(255, 80, 0, 255))
        qp.drawRect(self.x, self.y, 12, 12)

    # Default method name
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            # The code bellow is used to constantly call the update method
            self.update()
            # The paints the scene over and over
            self.repaint()
        else:
            QtGui.QFrame.timerEvent(self, event)


def main():
    app = QApplication(sys.argv)
    ex = Snake()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
