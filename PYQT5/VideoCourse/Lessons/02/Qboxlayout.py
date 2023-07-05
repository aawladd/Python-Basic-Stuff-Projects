from copyreg import dispatch_table
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QBoxLayOut Window")
        self.resize(600, 400)


        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        label = QLabel("First Label")
        layout.addWidget(label, 0)

        label = QLabel("Second Label")
        layout.addWidget(label, 0)


        secondLayout = QBoxLayout(QBoxLayout.TopToBottom)

        layout.addLayout(secondLayout)

        label = QLabel("Third Label")
        secondLayout.addWidget(label)

        label = QLabel("Fourth Label")
        secondLayout.addWidget(label)


app = QApplication(sys.argv)

display = Window()


display.show()

sys.exit(app.exec_())
