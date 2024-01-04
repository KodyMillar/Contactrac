# -*- coding: utf-8 -*-
# rpcontacts/database.py

"""This module connects the application to a database"""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createContactsTable():
    """Create the contacts table in the database"""
    contactsTableQuery = QSqlQuery()
    return contactsTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL,
            company_id INTEGER,
            city_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES company(id),
            FOREIGN KEY (city_id) REFERENCES city(id)
        )
        """
    )

def _createCompanyTable():
    companyTableQuery = QSqlQuery()
    return companyTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            company VARCHAR(40) NOT NULL,
            industry VARCHAR(40)
        )
        """
    )

def _createCountryTable():
    """Create the country table in the database"""
    countryTableQuery = QSqlQuery()
    return countryTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS country (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            country_name VARCHAR(40) NOT NULL,
        )
        """
    )

def _createCityTable():
    """Create the city table in the database"""
    cityTableQuery = QSqlQuery()
    return cityTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS city (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            city_name VARCHAR(40) NOT NULL,
            country_id INTEGER,
            FOREIGN KEY country_id REFERENCES country(id)
        )
        """
    )

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}"
        )
        return False
    _createContactsTable()
    _createCompanyTable()
    _createCityTable()
    _createCountryTable()
    return True

