import sys
from Qt import QtWidgets

class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Tab Example")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addWidget(QtWidgets.QPushButton("Btn Outside Of Tabs"))

        self.tab_widget = QtWidgets.QTabWidget()
        self.layout().addWidget(self.tab_widget)

        # MAKE TABS
        tab_a = self.new_tab()
        tab_a.layout().addWidget(QtWidgets.QPushButton("Btn On Tab A"))

        tab_b = self.new_tab()
        tab_b.layout().addWidget(QtWidgets.QPushButton("Btn On Tab B"))

        # ADD TABS
        self.tab_widget.addTab(tab_a, "Tab A")
        self.tab_widget.addTab(tab_b, "Tab B")

    def new_tab(self):
        widget = QtWidgets.QWidget()
        widget.setLayout(QtWidgets.QVBoxLayout())
        return widget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
