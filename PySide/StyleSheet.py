import os
import sys
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QSplitter, QPushButton, QGridLayout, \
    QSizePolicy, QCheckBox, QStatusBar, QMainWindow, QRadioButton, QLineEdit, QTabWidget, QTabBar, QGroupBox
from PySide2.QtCore import Qt

class FillPushButton(QPushButton):
    def __init__(self, parent=None):
        """
        QPushButton that fills the parent by default
        :param parent:
        """
        super(FillPushButton, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Style Sheet Example")

        self.add_status_bar()

        # ADD TAB BAR
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_tab_1()
        self.tabs.addTab(QWidget(), 'Tab No.2')
        self.tabs.addTab(QWidget(), 'Tab No.3')

        # DISABLED
        self.tabs.addTab(QWidget(), 'Tab Disabled')
        self.tabs.setTabEnabled(3,False)


    def add_tab_1(self):
        t1 = QWidget()
        layout = QVBoxLayout(t1)

        self.tabs.addTab(t1, "Tab No.1")

        self.add_vertical_splitter(layout)
        self.add_horizontal_splitter(layout)

    def add_status_bar(self):
        self.myStatus = QStatusBar()
        self.myStatus.showMessage("This is a status bar message...")
        self.setStatusBar(self.myStatus)

    def add_vertical_splitter(self, layout):
        splitter = QSplitter()
        layout.addWidget(splitter)

        # ADD LEFT
        left_widget = QWidget(splitter)
        left = QVBoxLayout(left_widget)

        # NORMAL
        let = QLineEdit('Line Edit With Text')
        left.layout().addWidget(let)

        #PLACEHOLDER
        let = QLineEdit()
        let.setPlaceholderText('This is placeholder text...')
        left.layout().addWidget(let)

        # DISABLED
        let = QLineEdit('Line Edit Disabled')
        let.setEnabled(False)
        left.layout().addWidget(let)



        # ADD RIGHT
        right_widget = QWidget(splitter)
        right = QGridLayout(right_widget)

        # GROUP BOX
        grp = QGroupBox("Group Box")
        right.layout().addWidget(grp)

        grp_layout = QGridLayout(grp)


        btn = QPushButton('Set Style')
        btn.pressed.connect(self.set_style)
        grp_layout.addWidget(btn)







    def add_horizontal_splitter(self, layout):
        splitter = QSplitter()
        splitter.setOrientation(Qt.Orientation.Vertical)
        layout.addWidget(splitter)

        # ADD TOP
        top_widget = QWidget(splitter)
        top = QVBoxLayout(top_widget)

        # NORMAL
        btn =FillPushButton('Push Button')
        top.layout().addWidget(btn)

        #DISABLED
        btn = FillPushButton('Push Button Disabled')
        btn.setEnabled(False)
        top.layout().addWidget(btn)

        # ADD BOTTOM
        bottom_widget = QWidget(splitter)
        right = QGridLayout(bottom_widget)

        # NORMAL
        cbx = QCheckBox('Check Box')
        right.addWidget(cbx)

        #DISABLED
        cbx = QCheckBox('Check Box Disabled')
        cbx.setEnabled(False)
        right.addWidget(cbx)

        rob = QRadioButton('Radio Button')
        right.addWidget(rob)

        rob = QRadioButton('Radio Button Disabled')
        rob.setEnabled(False)
        right.addWidget(rob)

    def set_style(self):
        stylesheet_path = os.path.join(os.path.dirname(__file__), 'style_dark.qss')
        with open(stylesheet_path, 'r') as f:
            self.setStyleSheet(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()
    #form.resize(400,600)

    form.set_style()

    sys.exit(app.exec_())


