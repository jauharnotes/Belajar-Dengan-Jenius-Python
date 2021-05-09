# Form implementation generated from reading ui file '9.DesignerQTableWidget.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, \
    QTableWidget, QMessageBox, QApplication


class window(QWidget):  # TEST
    def __init__(self):
        super().__init__()
        self.verticalLayout_2 = QVBoxLayout(windowQWidget)
        self.verticalLayout = QVBoxLayout()
        self.tableWidget1 = QTableWidget(windowQWidget)
        self.pushButton1 = QPushButton(windowQWidget)
        self.inputDialog1 = QInputDialog()
        self.mbox1 = QMessageBox()

        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 3, item)

        self.verticalLayout.addWidget(self.tableWidget1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout_2.addWidget(self.pushButton1)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(473, 487)
        self.re_translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def re_translate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Password Manager - QTableWidget"))
        item = self.tableWidget1.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Account"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Username"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Description"))
        __sortingEnabled = self.tableWidget1.isSortingEnabled()
        self.tableWidget1.setSortingEnabled(False)
        item = self.tableWidget1.item(0, 0)
        item.setText(_translate("Form", "Coinmarketcap"))
        item = self.tableWidget1.item(0, 1)
        item.setText(_translate("Form", "febrianza@gmail.com"))
        item = self.tableWidget1.item(0, 2)
        item.setText(_translate("Form", "***************"))
        item = self.tableWidget1.item(0, 3)
        item.setText(_translate("Form", "For API Development Purpose"))

        self.tableWidget1.setSortingEnabled(__sortingEnabled)
        self.pushButton1.setText(_translate("Form", "Add Password"))

        self.pushButton1.clicked.connect(self.get_item)

    def count_row(self):
        self.mbox1.setWindowTitle("Message Box")
        self.mbox1.setText("Total Rows : " + str(self.tableWidget1.rowCount()))
        self.mbox1.exec()

    def get_item(self):
        text, ok = self.inputDialog1.getText(self, 'input dialog', 'Input Your Name')
        if ok:
            print(text)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    windowQWidget = QWidget()
    gui = window()
    gui.setup_ui(windowQWidget)
    windowQWidget.show()
    sys.exit(app.exec())
