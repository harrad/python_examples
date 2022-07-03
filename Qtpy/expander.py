import sys
from Qt import QtWidgets, QtCore, Qt


class Expander(QtWidgets.QWidget):
    def __init__(self, text, is_expanded=False, parent=None):
        super(Expander, self).__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.btn_header = self._make_header(text)
        self._content_widget = self._make_content()

        self.set_expanded(is_expanded)

    def _make_header(self, text):
        widget = QtWidgets.QToolButton(toggled=self.on_toggled, parent=self)
        self.layout().addWidget(widget)

        widget.setCheckable(True)
        widget.setToolButtonStyle(Qt.QtCore.Qt.ToolButtonTextBesideIcon)
        widget.setText(text)
        widget.setArrowType(QtCore.Qt.RightArrow)
        widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)

        return widget

    def _make_content(self):
        widget = QtWidgets.QFrame(objectName="expander", parent=self)
        self.layout().addWidget(widget)
        widget.setLayout(QtWidgets.QVBoxLayout())

        qss = "QFrame#expander { border: 1px solid #abacad; border-top:0px; margin-left:1; margin-right:1; }"
        widget.setStyleSheet(qss)

        return widget

    def content_layout(self):
        return self._content_widget.layout()

    def on_toggled(self, arg):
        self.set_expanded(arg)

    def set_expanded(self, value):
        self.btn_header.setChecked(value)
        self._content_widget.setVisible(value)
        if value:
            self.btn_header.setArrowType(QtCore.Qt.DownArrow)
        else:
            self.btn_header.setArrowType(QtCore.Qt.RightArrow)


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Basic Window")
        self.resize(500, 200)

        self.setLayout(QtWidgets.QVBoxLayout())

        exp = Expander("Expander 1 - Collapsed", parent=self)
        self.layout().addWidget(exp)
        self.add_content(exp)

        exp = Expander("Expander 2 - Expanded", is_expanded=True, parent=self)
        self.layout().addWidget(exp)
        self.add_content(exp)

        exp = Expander("Expander 3 - Collapsed & Disabled", parent=self)
        self.layout().addWidget(exp)
        self.add_content(exp)
        exp.setEnabled(False)

        exp = Expander("Expander 4 - Expanded & Disabled", is_expanded=True, parent=self)
        self.layout().addWidget(exp)
        self.add_content(exp)
        exp.setEnabled(False)

        self.layout().addStretch(1)

    def add_content(self, expander):
        for i in range(3):
            btn = QtWidgets.QPushButton(f"Expander Button {i + 1}", parent=expander)
            expander.content_layout().addWidget(btn)

        expander.content_layout().addStretch(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
