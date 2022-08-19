import sys
from Qt import QtWidgets

class BreadcrumbWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

    def set_items(self, items):
        path = "<span> &#10097; </span>".join([i for i in items])
        self.setText(path)


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Breadcrumb")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.breadcrumbs = BreadcrumbWidget(self)
        self.layout().addWidget(self.breadcrumbs)
        self.breadcrumbs.set_items(["C:/", "Folder", "SubFolder", "Item"])

        self.layout().addStretch()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
