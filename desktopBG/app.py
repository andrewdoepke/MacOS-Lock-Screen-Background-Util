import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class appski(QWidget):
    file = None

    def restart(self):
        print(self)
        os.system("sh restrt.sh")

    def b2press(self):
        src = self.sender()

        os.system("sh lockscreengb.sh " + self.file)
        src.hide()

        layout = src.parentWidget().layout()

        layout.itemAt(0).widget().hide()
        layout.itemAt(1).widget().hide()
        layout.itemAt(2).widget().hide()
        layout.itemAt(3).widget().hide()

        layout.addWidget(QLabel("The deed is done! Restart your pc."))

        restartbtn = QPushButton("Push to restart your PC if ya want to now")
        restartbtn.clicked.connect(self.restart)
        layout.addWidget(restartbtn)

        exitbtn = QPushButton("Click to exit")
        exitbtn.clicked.connect(self.close)
        layout.addWidget(exitbtn)


    def buttonpress(self):
        src = self.sender()

        # noinspection PyArgumentList
        fname, _ = QFileDialog.getOpenFileName(filter='Image Files(*.png *.jpg *.bmp *.jpeg)')
        self.file = fname

        if fname == '': #if no file is chosen
            return

        src.hide()

        img = QPixmap(self.file)
        pic = QLabel()
        pic.setPixmap(img)
        pic.setMaximumWidth(400)
        pic.setMaximumHeight(200)
        pic.setScaledContents(True)

        layout = src.parentWidget().layout()

        layout.addWidget(QLabel("Your image:"))
        layout.addWidget(pic)

        submit = QPushButton()
        submit.setText("Click here to change background!")
        submit.clicked.connect(self.b2press)

        layout.addWidget(submit)

    # noinspection PyArgumentList
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle('Desktop Background Changer')

        vbox = QVBoxLayout()

        txt = QLabel()
        txt.setText("Add a file to change your desktop background!")

        choosefile = QPushButton(self)
        choosefile.setText("Click here to choose your image file")
        choosefile.clicked.connect(self.buttonpress)

        vbox.addWidget(txt)
        vbox.addWidget(choosefile)

        self.setLayout(vbox)

        self.show()

def buildmainapp():
    appa = QApplication(sys.argv)
    appy = appski()

    print(appy)
    sys.exit(appa.exec_()) #execute the desired app


def app():
    buildmainapp()
