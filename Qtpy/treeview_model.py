import sys
from Qt import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Treeview Example")
        self.resize(500, 400)
        self.setLayout(QtWidgets.QVBoxLayout())

        self.basic_tree = self.get_basic_tree()
        self.complex_tree = self.get_complex_tree()

    def add_basic_item(self, parent, text):
        item = QtGui.QStandardItem(text)
        parent.setChild(parent.rowCount(), item)
        return item

    def get_basic_tree(self):
        treeview = QtWidgets.QTreeView()
        self.layout().addWidget(treeview)
        treeview.setHeaderHidden(True)
        treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        model = QtGui.QStandardItemModel(0, 1, self)
        treeview.setModel(model)

        parent = model.invisibleRootItem()
        i1 = self.add_basic_item(parent, "item 1")
        self.add_basic_item(i1, "item 1a")
        self.add_basic_item(i1, "item 1b")

        i2 = self.add_basic_item(parent, "item 2")
        self.add_basic_item(i2, "item 2a")
        self.add_basic_item(i2, "item 2b")

        return treeview

    def add_complex_item(self, parent, values):
        row = parent.rowCount()
        for i, v in enumerate(values):
            item = QtGui.QStandardItem(v)
            parent.setChild(row, i, item)
        return parent.child(row, 0)

    def get_complex_tree(self):
        treeview = QtWidgets.QTreeView()
        self.layout().addWidget(treeview)
        treeview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        model = QtGui.QStandardItemModel(0, 3, self)
        treeview.setModel(model)

        treeview.header().setStretchLastSection(False)
        treeview.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        headers = ["Type", "Legs", "Has Fur"]
        for i, v in enumerate(headers):
            model.setHeaderData(i, QtCore.Qt.Horizontal, v)

        parent = model.invisibleRootItem()
        i1 = self.add_complex_item(parent, ["Mammal"])
        self.add_complex_item(i1, ["Human", "2", "False"])
        self.add_complex_item(i1, ["Rat", "4", "True"])

        i2 = self.add_complex_item(parent, ["Reptile"])
        self.add_complex_item(i2, ["Snake", "0", "False"])
        self.add_complex_item(i2, ["Crocodile", "4", "False"])

        return treeview


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
