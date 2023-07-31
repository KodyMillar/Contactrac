# -*- coding: utf-8 -*-
# rpcontacts/model.py

"""Manages the contacts table"""
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        """Create and set up the model"""
        contactsTableModel = QSqlTableModel()
        contactsTableModel.setTable("contacts")
        contactsTableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        contactsTableModel.select()
        headerNames = ["ID", "Name", "Job", "Email"]
        for column, header in enumerate(headerNames):
            contactsTableModel.setHeaderData(column, Qt.Horizontal, header)
        return contactsTableModel


