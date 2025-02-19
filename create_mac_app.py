"""
Create macOS application bundle
"""
import os
import sys
from pathlib import Path

def create_mac_app():
    # Create app bundle structure
    app_path = Path("/Applications/ThesisManager.app")
    contents_path = app_path / "Contents"
    macos_path = contents_path / "MacOS"
    resources_path = contents_path / "Resources"
    
    # Create directories
    for path in [app_path, contents_path, macos_path, resources_path]:
        path.mkdir(exist_ok=True)
    
    # Create Info.plist
    info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>ThesisManager</string>
    <key>CFBundleIconFile</key>
    <string>thesis_icon.icns</string>
    <key>CFBundleIdentifier</key>
    <string>com.cikgubyfisa.thesismanager</string>
    <key>CFBundleName</key>
    <string>Thesis Manager</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.10</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>
"""
    (contents_path / "Info.plist").write_text(info_plist)
    
    # Create launcher script
    launcher = """#!/bin/bash
cd "$(dirname "$0")"
/usr/local/bin/python3 -m thesis_manager
"""
    launcher_path = macos_path / "ThesisManager"
    launcher_path.write_text(launcher)
    launcher_path.chmod(0o755)
    
    print(f"Created application bundle at {app_path}")

if __name__ == "__main__":
    create_mac_app() 