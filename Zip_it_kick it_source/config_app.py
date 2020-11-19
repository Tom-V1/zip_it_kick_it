import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
import json
from PyQt5 import QtGui

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui\gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        self.browse_2.clicked.connect(self.browsefiles_2)
        self.confirm_2.clicked.connect(self.confirm)
        self.spinBox.valueChanged.connect(self.valuechange)

        app.setWindowIcon(QtGui.QIcon('gui/test-tube.png'))

        app.setApplicationName("Zip It, Kick It")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


    def browsefiles(self):
        fname=QFileDialog.getExistingDirectory(self, 'Select Directory', '')
        self.filename.setText(fname)
        print(fname)

    def browsefiles_2(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select Directory','D:\codefirst.io\PyQt5 tutorials\Browse Files')
        self.filename_2.setText(fname)
        print(fname)

    def valuechange(self):
        print("changed")

    def confirm(self):
        print(self.filename.text())
        print(self.filename_2.text())
        print((self.spinBox.value()))
        with open("data/config_data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            data["archive_location"] = self.filename.text()
            data["target_location"] = self.filename_2.text()
            data["days"] = self.spinBox.value()
        with open("data/config_data.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Config file updated")
        msgBox.setWindowTitle("Zip It, Kick It")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            sys.exit(app.exec_())

    def msgButtonClick(i):
        print("Button clicked is:", i.text())

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())
