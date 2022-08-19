from PySide2 import QtWidgets
import qtmax

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.setWindowTitle("Combo Box")
        self.resize(200, 200)

        self.setLayout(QtWidgets.QVBoxLayout())
        
        self.cbx_1 = QtWidgets.QComboBox()
        self.layout().addWidget(self.cbx_1)
        self.cbx_1.addItems(["Banana", "Apple", "Grape"])
        self.cbx_1.currentIndexChanged.connect(self.on_combox_changed)
        
        self.btn_2 = QtWidgets.QPushButton("Press Me!")
        self.layout().addWidget(self.btn_2)        
        self.btn_2.pressed.connect(self.on_button_pressed)

        self.layout().addStretch(1)
        
    def on_button_pressed(self):
        item = self.cbx_1.currentText()
        print(f"The current selection is {item}")
        
    def on_combox_changed(self, ):
        item = self.cbx_1.currentText()
        print(f"Item changed to {item}")


if __name__ == "__main__":
    window = MainWindow(qtmax.GetQMaxMainWindow())
    window.show()
