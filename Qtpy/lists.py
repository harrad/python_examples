import sys
from Qt import QtWidgets

class CustomItemWidget(QtWidgets.QWidget):
    """
    Custom item for ListViewWidget
    """
    def __init__(self, text1, text2, parent = None):
        super(CustomItemWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout(self)

        self.label_1 = QtWidgets.QLabel(text1)
        layout.addWidget(self.label_1)

        self.label_2 = QtWidgets.QLabel(text2)
        layout.addWidget(self.label_2)


class Form(QtWidgets.QDialog):
    """
    Main window form
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("ListWidget Examples")

        layout = QtWidgets.QVBoxLayout(self)

        self.add_default_list(layout)
        self.add_custom_list(layout)

    def add_custom_list(self, layout):
        qtList = QtWidgets.QListWidget()
        layout.addWidget(qtList)
        qtList.setAlternatingRowColors(True)
        for i in range(1, 6):
            self.add_item(qtList)

    def add_item(self, list_widget):
        widget = CustomItemWidget('Input Text 1', 'Input Text 2')
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        list_widget.addItem(item)
        list_widget.setItemWidget(item, widget)

    def add_default_list(self, layout):
        qtList = QtWidgets.QListWidget()
        layout.addWidget(qtList)
        for i in range(1, 6):
            qtList.addItem(str(i))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())
