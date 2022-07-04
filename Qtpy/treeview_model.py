import sys
from Qt import QtWidgets, QtGui


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Treeview Example")
        self.resize(500, 200)
        self.setLayout(QtWidgets.QVBoxLayout())

        self.treeview = QtWidgets.QTreeView()
        self.layout().addWidget(self.treeview)
        self.treeview.setHeaderHidden(True)
        self.treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.model = QtGui.QStandardItemModel(0, 1, self)
        self.treeview.setModel(self.model)

        parent = self.model.invisibleRootItem()
        i1 = self.add_item(parent, "item 1")
        self.add_item(i1, "item 1a")
        self.add_item(i1, "item 1b")

        i2 = self.add_item(parent, "item 2")
        self.add_item(i2, "item 2a")
        self.add_item(i2, "item 2b")

    def add_item(self, parent, text):
        item = QtGui.QStandardItem(text)
        parent.setChild(parent.rowCount(), item)
        return item


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
