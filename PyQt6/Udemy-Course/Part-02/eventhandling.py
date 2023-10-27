from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Event Handling")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_Widget()
    

    def create_Widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        btn.clicked.connect(self.click_btn)
        self.label = QLabel("Default Text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def click_btn(self):
        self.label.setText("Anoter Text")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet('color:red')

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())