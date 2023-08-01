# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table"""

from PyQt5.Qt import Qt
from PyQt5.Qt import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QLineEdit,
    QMessageBox
)

from .model import ContactsModel

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI"""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create Buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)


class AddDialog(QDialog):
    """Adds the contact dialog to add a contact"""
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

    def setupUI(self):
        """Setup the contact dialog's UI"""
        # Create the line edits for the contact's information
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        # Add the form layout to hold all the line edits
        addContactLayout = QFormLayout()
        addContactLayout.addRow("Name", self.nameField)
        addContactLayout.addRow("Job", self.jobField)
        addContactLayout.addRow("Email", self.emailField)
        # Create the buttons for the dialog
        self.buttonsBox = QDialogButtonBox()
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok, QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted(self.accept)
        self.buttonsBox.rejected(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Validate and accept the data from the user"""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}"
                )
                # Reset the data
                self.data = None
                return

            self.data.append(field.text())
        super().accept()


