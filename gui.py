import sys
import os

from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)
from PyQt5.QtGui import QIcon, QPixmap

from subprocess import call


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel('M1', self)
        self.lbl2 = QLabel('Highlighted : ',self)
        combo = QComboBox(self)
        File_object = open("mosfet_tobe_highlighted.txt","w")
        File_object.write('M1')
        File_object.close()
        call(["python", "mosfets.py"])
        self.label = QLabel(self)
        self.pixmap = QPixmap('schematic.jpg')
        self.label.setPixmap(self.pixmap)   
        
        for i in range(1,7):
             combo.addItem('M'+str(i))   

        combo.move(180, 25)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.lbl.move(210,50)
        self.lbl2.move(140,50)
        self.label.move(20,150)
        self.setWindowTitle('Highlite Mosfet')
        self.show()

    def onActivated(self, text):
        File_object = open("mosfet_tobe_highlighted.txt","w")
        File_object.write(text)
        File_object.close()
        call(["python", "mosfets.py"])
        self.lbl.setText(text)
        self.pixmap = QPixmap('schematic.jpg')
        self.label.setPixmap(self.pixmap)   
        
        self.lbl.adjustSize()


def main():

    app = QApplication(sys.argv)
    ex = Window()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
