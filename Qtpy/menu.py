import sys

from Qt import QtWidgets, QtGui


class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Menus")
        self.resize(250, 200)
        self.setLayout(QtWidgets.QFormLayout())

        static_menu = self.menu_static()

        # BUTTON WITH A SET MENU
        btn_menu = QtWidgets.QPushButton("Static Menu - Button Menu")
        self.layout().addWidget(btn_menu)
        btn_menu.setMenu(static_menu)

        # BUTTON WHICH SPAWNS A STATIC MENU ON CLICK UNDER THE CURSOR
        btn_menu = QtWidgets.QPushButton("Static Menu - Under Cursor")
        self.layout().addWidget(btn_menu)
        btn_menu.clicked.connect(lambda x: static_menu.exec_(QtGui.QCursor().pos()))

        # BUTTON WHICH GENERATES A DYNAMIC MENU ON CLICK UNDER THE CURSOR
        btn_menu = QtWidgets.QPushButton("Dynamic Menu - Under Cursor")
        self.layout().addWidget(btn_menu)
        btn_menu.clicked.connect(self.menu_dynamic)

        self.setFixedHeight(self.sizeHint().height())

    def menu_static(self):
        menu = QtWidgets.QMenu()

        # SUBMENU EXAMPLE
        submenu = menu.addMenu("Submenu")
        for i in ["Submenu Item 01", "Submenu Item 02", "Submenu Item 03"]:
            submenu.addAction(i)

        # SEPARATOR EXAMPLE
        menu.addSeparator()

        # ACTION WITH CONNECTION EXAMPLE
        action = menu.addAction("Connected action")
        action.triggered.connect(self.action)

        # USING ADD ACTION ARGS EXAMPLE
        menu.addAction("Action in args", self.action)

        # USING LAMBDA EXPRESSION EXAMPLE
        action = menu.addAction("Lambda action")
        action.triggered.connect(lambda x: self.action())

        return menu

    def menu_dynamic(self):
        menu = QtWidgets.QMenu()

        for item in ["Dynamic Menu Item 01", "Dynamic Menu Item 02", "Dynamic Menu Item 03"]:
            menu.addAction(item, self.action)

        menu.exec_(QtGui.QCursor().pos())

    def action(self):
        sender = self.sender()
        print("Menu Item Clicked - " + sender.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
