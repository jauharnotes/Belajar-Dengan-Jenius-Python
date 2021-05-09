# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '7.DesignerQListBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class myWindow(object):
    def __init__(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.mbox1 = QMessageBox()

    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(400, 300)

        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.listWidget.insertItem(0, "Maudy")
        self.listWidget.insertItem(1, "Ayunda")
        self.listWidget.insertItem(2, "Gun Gun")
        self.listWidget.insertItem(3, "Febrianza")
        self.listWidget.clicked.connect(self.event_listbox1_clicked)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Main Window - QListBox"))

    def event_listbox1_clicked(self):
        item = self.listWidget.currentItem()
        print(item.text())
        self.display_message("MessageBox", "Item : " + item.text())

    def display_message(self, title, text):
        self.mbox1.setWindowTitle(title)
        self.mbox1.setText(text)
        self.mbox1.setDetailedText("Place for more details information.")
        self.mbox1.exec()
        # QMessageBox.information(self, title, text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = myWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
