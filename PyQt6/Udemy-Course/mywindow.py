from PyQt6.QtWidgets import QApplication, QWidget 
import sys 

app = QApplication(sys.argv)

window = QWidget()
# window.statusBar().showMessage("Welcome to PyQt6")

window.show()

sys.exit(app.exec())