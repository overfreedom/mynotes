# encoding=utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox,\
    QApplication
from PyQt5.Qt import QObject

##It is not possible to define a new Python class that sub-classes from more than one Qt class.
class A(QMainWindow):      ##一个类不能继承多个Qt组件窗体
    pass    
    

class Example(QWidget,A):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setGeometry(300,300,400,200)

        vbox = QVBoxLayout()

        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")

        btn1.clicked.connect(self.btnclick)
        btn2.clicked.connect(self.btnclick)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)
        self.show()

    def btnclick(self):
         sender = self.sender()
         msg = QMessageBox().question(self, "message", "you have push the "+sender.text(), QMessageBox.Yes,QMessageBox.Yes)

         
if __name__ == "__main__":         
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())