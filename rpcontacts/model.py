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
        headerNames = ["ID", "Name", "Job", "Email", "Company", "Country"]
        for column, header in enumerate(headerNames):
            contactsTableModel.setHeaderData(column, Qt.Horizontal, header)
        return contactsTableModel

    def addContact(self, data):
        """Adds a contact to the database"""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()

    def deleteContact(self, row):
        """Delete a contact from the database"""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()


class CompanyModel:

    def __init__(self):
        self.model = self._createModel()
    
    def _createModel(self):
        companyTableModel = QSqlTableModel()
        companyTableModel.setTable("country")
        companyTableModel.setEditStrategy(QSqlTableModel.onFieldChange)
        companyTableModel.select()
        companyHeaders = ["ID", "Company", "Industry"]
        for column, header in enumerate(companyHeaders):
            companyTableModel.setHeaderData(column, Qt.Horizontal, header)
        return companyTableModel