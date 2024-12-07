# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:18:08 2022

@author: ricar
"""

# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>aa", parent=window)
helloMsg.move(60, 15)

print("app")
# 4. Show your application's GUI
window.show()

print("1")
# 5. Run your application's event loop
sys.exit(app.exec())

