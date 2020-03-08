import sys
from PySide2.QtWidgets import QApplication, QDialog, QHeaderView, QAbstractItemView, QVBoxLayout, QTableWidget, QTableWidgetItem
from PySide2.QtCore import Qt


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Table Example")

        layout = QVBoxLayout(self)

        # ADD TABLE
        self.table = QTableWidget(0, 4)
        layout.addWidget(self.table)

        # ADD COLUMN HEADERS
        self.table.setHorizontalHeaderLabels(["First Name", "Last Name", "Gender", "Age"])

        # ADD DATA
        self.add_row('John', 'Smith', 'Male', '28')
        self.add_row('Jane', 'Doe', 'Female', '32')
        self.add_row('Mary', 'Jane', 'Female', '59')
        self.add_row('John', 'Doe', 'Male', '59')
        self.add_row('Mary', 'Sue', 'Female', '28')

        # TABLE SETTINGS
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSortingEnabled(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_row(self, first, last, gender, age):
        rowId = self.table.rowCount()
        self.table.insertRow(rowId)

        self.add_read_only_cell(rowId,0, first)
        self.add_read_only_cell(rowId, 1, last)
        self.add_read_only_cell(rowId, 2, gender)
        self.add_read_only_cell(rowId, 3, age)


    def add_read_only_cell(self, r, c, value):
        item = QTableWidgetItem(value)
        item.setFlags(Qt.ItemIsSelectable |  Qt.ItemIsEnabled)
        self.table.setItem(r, c, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()

    sys.exit(app.exec_())
