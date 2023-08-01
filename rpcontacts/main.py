# -*- coding: utf-8 -*-

"""This module provides the RP Contacts Application"""

import sys

from PyQt5.Qt import QApplication

from .database import createConnection
from .views import Window

def main():
    """RP Contacts main function"""
    # Create the app
    app = QApplication([])
    # Connect to database before creating window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())