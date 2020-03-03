import sys
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QPushButton

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("TreeWidget Examples")

        layout = QVBoxLayout(self)
        self.add_tree_no_header(layout)
        self.add_tree_with_header(layout)

    def add_tree_no_header(self, parent):
        tw = QTreeWidget()
        parent.addWidget(tw)
        tw.setHeaderHidden(True)
        tw.setAlternatingRowColors(True)

        i1 = QTreeWidgetItem(tw, ['Mammal'])
        i2 = QTreeWidgetItem(i1, ['Rodent'])
        i3 = QTreeWidgetItem(i2, ['Rat'])
        i3 = QTreeWidgetItem(i2, ['Beaver'])
        i2 = QTreeWidgetItem(i1, ['Primate'])
        i3 = QTreeWidgetItem(i2, ['Baboon'])
        i3 = QTreeWidgetItem(i2, ['Human'])
        i1 = QTreeWidgetItem(tw, ['Reptile'])
        i2 = QTreeWidgetItem(i1, ['Snake'])
        i3 = QTreeWidgetItem(i1, ['Crocodile'])

        self.add_expand_collapse_buttons(parent, tw)

    def add_tree_with_header(self, parent):
        tw = QTreeWidget()
        parent.addWidget(tw)
        tw.setHeaderLabels(['Type', 'Legs', 'Has Hair/Fur'])
        tw.setSortingEnabled(True)
        tw.setAlternatingRowColors(True)
        i1 = QTreeWidgetItem(tw, ['Mammal'])
        i2 = QTreeWidgetItem(i1, ['Rodent'])
        i3 = QTreeWidgetItem(i2, ['Rat', '4', 'True'])
        i3 = QTreeWidgetItem(i2, ['Beaver', '2', 'True'])
        i2 = QTreeWidgetItem(i1, ['Primate'])
        i3 = QTreeWidgetItem(i2, ['Baboon', '2', 'True'])
        i3 = QTreeWidgetItem(i2, ['Human', '2', 'True'])
        i1 = QTreeWidgetItem(tw, ['Reptile'])
        i2 = QTreeWidgetItem(i1, ['Snake', '0', 'False'])
        i3 = QTreeWidgetItem(i1, ['Crocodile', '4', 'False'])

        self.add_expand_collapse_buttons(parent, tw)

    def add_expand_collapse_buttons(self, parent, tw):
        layout = QHBoxLayout()
        parent.addLayout(layout)
        self.add_button(layout, 'Expand All', lambda: tw.expandAll())
        self.add_button(layout, 'Collapse All', lambda: tw.collapseAll())

    def add_button(self, parent, label, action):
        btn = QPushButton(label)
        btn.clicked.connect(action)
        parent.addWidget(btn)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec_())
