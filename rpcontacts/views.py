# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table"""

from PyQt5.Qt import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

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
