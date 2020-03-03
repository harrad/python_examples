import sys
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QWidget, QListWidgetItem, QLabel


class CustomItemWidget(QWidget):
    """
    Custom item for ListViewWidget
    """
    def __init__(self, text1, text2, parent = None):
        super(CustomItemWidget, self).__init__(parent)

        layout = QVBoxLayout(self)

        self.label_1 = QLabel(text1)
        layout.addWidget(self.label_1)

        self.label_2 = QLabel(text2)
        layout.addWidget(self.label_2)


class Form(QDialog):
    """
    Main window form
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("ListWidget Examples")

        layout = QVBoxLayout(self)

        self.add_default_list(layout)
        self.add_custom_list(layout)

    def add_custom_list(self, layout):
        qtList = QListWidget()
        layout.addWidget(qtList)
        qtList.setAlternatingRowColors(True)
        for i in range(1, 6):
            widget = CustomItemWidget('Input Text 1', 'Input Text 2')
            item = QListWidgetItem()

            item.setSizeHint(widget.sizeHint())

            qtList.addItem(item)
            qtList.setItemWidget(item, widget)

    def add_default_list(self, layout):
        qtList = QListWidget()
        layout.addWidget(qtList)
        for i in range(1, 6):
            qtList.addItem(str(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())
