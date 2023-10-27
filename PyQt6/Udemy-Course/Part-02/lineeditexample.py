from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Python QLineEdit")
        self.setWindowIcon(QIcon('images/python.png'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Sanserif', 16))
        # line_edit.setText("Default Text")
        # line_edit.setPlaceholderText("Please Enter you username")
        # line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())