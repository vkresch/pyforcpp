from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    # Init the app class
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Set the window geometry
    win.setGeometry(0, 0, 800, 600)
    win.setWindowTitle("Title")

    # Define a label
    label = QtWidgets.QLabel("This is a label", win)
    label.setText("This is a updated label juhuu!")
    label.move(50, 50)

    # Show the window
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()