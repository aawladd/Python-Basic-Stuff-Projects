from PyQt5.QtWidgets import *
import sys 

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hello Program")
        

        layout = QGridLayout()
        self.setLayout(layout)


        label = QLabel(" Hello World ")
        layout.addWidget(label, 0, 0)



app = QApplication(sys.argv)

display = Window()
display.show()

sys.exit(app.exec_())