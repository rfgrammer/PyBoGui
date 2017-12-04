from PySide.QtCore import *
from PySide.QtGui import *
import time
import sys

__appname__ = "Eight Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close..")

        # self.connect(openButton, SIGNAL("clicked()"), self.open())

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):
        dir = "."
        fileObj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=dir, filter="text files (*.txt)")
        print fileObj
        print type(fileObj)

    def save(self):
        pass

    def dir(self):
        pass

    def close(self):
        pass


def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
