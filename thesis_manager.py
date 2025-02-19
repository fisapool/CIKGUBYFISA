#!/usr/bin/env python3
"""
Desktop launcher for thesis template manager
"""

import sys
from PyQt6.QtWidgets import QApplication
from cikgubyfisa.gui.system_tray import ThesisSystemTray

def main():
    # Create application
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    # Create system tray
    tray = ThesisSystemTray()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 