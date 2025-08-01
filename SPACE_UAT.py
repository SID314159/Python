from uat import uat_auto
from json_to_xl import document
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def main():
    def uat():
        obj1=uat_auto()
        obj1.pass_inputs()
    def xl():   
        obj2=document()
        obj2.xlwrite()
    # Create the application
    app = QApplication(sys.argv)
    # Create the main window
    window = QWidget()
    window.setWindowTitle('SELECT')
    window.setGeometry(100, 100, 300, 150)
    # Create Button 1
    button1 = QPushButton('UAT', window)
    button1.move(50, 50)
    button1.clicked.connect(uat)
    # Create Button 2
    button2 = QPushButton('JSON_to_XL', window)
    button2.move(150, 50)
    button2.clicked.connect(xl)
    # Show the window
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
