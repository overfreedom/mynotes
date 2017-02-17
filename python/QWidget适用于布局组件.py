# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication,QPushButton,QBoxLayout,QMainWindow, QHBoxLayout,\
    QVBoxLayout,QWidget
import sys

class Example(QWidget):   #如果这里继承QMainWindow 则布局组件会失效
    def __init__(self):
        super().__init__()
        try:
            self.initWindow()
        except Exception as e:
            print(e)
            
    def initWindow(self):
                
        self.okButton = QPushButton("OK")
        self.okButton.resize(self.okButton.sizeHint())
        self.cancelButton = QPushButton("cancel")
         
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.okButton)
        self.hbox.addWidget(self.cancelButton)
         
        self.vbox =QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
          
        self.setLayout(self.vbox)
        self.setGeometry(300,300,500,200)
        self.show()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())        