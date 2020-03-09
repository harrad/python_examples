import sys
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QSplitter, QPushButton, QGridLayout, QSizePolicy
from PySide2.QtCore import Qt

class FillPushButton(QPushButton):
    def __init__(self, parent=None):
        """
        QPushButton that fills the parent by default
        :param parent:
        """
        super(FillPushButton, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Splitter Examples")

        layout = QVBoxLayout(self)

        self.add_vertical_splitter(layout)
        self.add_horizontal_splitter(layout)

    def add_vertical_splitter(self, layout):
        splitter = QSplitter()
        layout.addWidget(splitter)

        # ADD LEFT
        left_widget = QWidget(splitter)
        left = QVBoxLayout(left_widget)

        for i in range(3):
            btn =FillPushButton(f'left_{i}')
            left.layout().addWidget(btn)

        # ADD RIGHT
        right_widget = QWidget(splitter)
        right = QGridLayout(right_widget)
        btn = FillPushButton('right')
        right.addWidget(btn)

    def add_horizontal_splitter(self, layout):
        splitter = QSplitter()
        splitter.setOrientation(Qt.Orientation.Vertical)
        layout.addWidget(splitter)

        # ADD TOP
        top_widget = QWidget(splitter)
        top = QVBoxLayout(top_widget)

        for i in range(3):
            btn =FillPushButton(f'top_{i}')
            top.layout().addWidget(btn)

        # ADD BOTTOM
        bottom_widget = QWidget(splitter)
        right = QGridLayout(bottom_widget)
        btn = FillPushButton('bottom')
        right.addWidget(btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QSplitter::handle { background-color: gray }")
    form = Form()
    form.show()

    sys.exit(app.exec_())
