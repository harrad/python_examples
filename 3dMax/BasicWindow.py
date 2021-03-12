from MaxPlus import GetQMaxMainWindow
from PySide2 import QtWidgets


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Basic Window")
        self.resize(500, 200)

        self.setLayout(QtWidgets.QVBoxLayout())

        self.btn_1 = QtWidgets.QPushButton("Button 1")
        self.layout().addWidget(self.btn_1)

        self.btn_2 = QtWidgets.QPushButton("button 2")
        self.layout().addWidget(self.btn_2)

        self.layout().addStretch(1)


if __name__ == "__main__":
    window = MainWindow(GetQMaxMainWindow())
    window.show()
