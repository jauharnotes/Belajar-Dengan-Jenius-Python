import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        # Add Button / QPushButton
        self.btn1 = QPushButton('Show Dialog', self)
        # Set Button Properties
        # self.btn1.move(20, 20)  # No Layout Mode
        self.btn1.clicked.connect(self.show_input_dialog)

        self.line1 = QLineEdit(self)
        # self.line1.move(130, 22)  # No Layout Mode
        layout.addWidget(self.btn1)
        layout.addWidget(self.line1)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Main Window - QListBox')

    def show_input_dialog(self):
        text, ok = QInputDialog.getText(self, 'input dialog', 'Input Your Name')
        if ok:
            self.line1.setText(str(text))


app = QApplication(sys.argv)
window = Window()
window.show()
# Start the event loop.
sys.exit(app.exec_())  # Zero is considered “successful termination”