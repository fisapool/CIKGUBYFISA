import os
import sys
import winshell
from win32com.client import Dispatch

def create_shortcut():
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Thesis Manager.lnk")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = sys.executable
    shortcut.Arguments = "-m thesis_manager"
    shortcut.IconLocation = os.path.join(os.path.dirname(__file__), 
                                       "cikgubyfisa", "gui", "icons", "thesis_icon.png")
    shortcut.save()

if __name__ == "__main__":
    create_shortcut() 