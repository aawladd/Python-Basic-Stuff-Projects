from dis import dis
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("Window")
        self.resize(600, 400)



app = QApplication(sys.argv)

display = Window()
display.show()

sys.exit(app.exec_())


