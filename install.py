"""
Automated installation script for Thesis Manager
"""

import os
import sys
import subprocess
from pathlib import Path
import platform

class ThesisManagerInstaller:
    def __init__(self):
        self.system = platform.system()
        self.project_root = Path(__file__).parent
        self.venv_path = self.project_root / "venv"
        
    def install(self):
        """Run the complete installation process"""
        print("Starting Thesis Manager installation...")
        
        try:
            self._check_python()
            self._create_venv()
            self._install_requirements()
            self._create_app_bundle()
            self._create_shortcuts()
            self._setup_autostart()
            print("\n✅ Installation completed successfully!")
            self._show_instructions()
        except Exception as e:
            print(f"\n❌ Installation failed: {str(e)}")
            sys.exit(1)

    def _check_python(self):
        """Check Python version and install if needed"""
        print("\n📦 Checking Python installation...")
        min_version = (3, 8)
        
        if sys.version_info < min_version:
            if self.system == "Darwin":  # macOS
                subprocess.run(["brew", "install", "python3"], check=True)
            else:
                raise RuntimeError(f"Python {min_version[0]}.{min_version[1]} or higher is required")

    def _create_venv(self):
        """Create and activate virtual environment"""
        print("\n🔧 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(self.venv_path)], check=True)
        
        # Get path to pip in virtual environment
        if self.system == "Windows":
            self.pip_path = self.venv_path / "Scripts" / "pip"
            self.python_path = self.venv_path / "Scripts" / "python"
        else:
            self.pip_path = self.venv_path / "bin" / "pip"
            self.python_path = self.venv_path / "bin" / "python"

    def _install_requirements(self):
        """Install required packages"""
        print("\n📚 Installing dependencies...")
        subprocess.run([
            str(self.pip_path),
            "install",
            "-r",
            str(self.project_root / "requirements.txt")
        ], check=True)
        
        # Install the package itself
        subprocess.run([
            str(self.pip_path),
            "install",
            "-e",
            "."
        ], check=True)

    def _create_app_bundle(self):
        """Create application bundle"""
        print("\n📱 Creating application bundle...")
        if self.system == "Darwin":  # macOS
            subprocess.run([
                str(self.python_path),
                str(self.project_root / "create_mac_app.py")
            ], check=True)
        elif self.system == "Windows":
            subprocess.run([
                str(self.python_path),
                str(self.project_root / "create_shortcut.py")
            ], check=True)

    def _create_shortcuts(self):
        """Create desktop and menu shortcuts"""
        print("\n🔗 Creating shortcuts...")
        if self.system == "Darwin":  # macOS
            desktop_path = Path.home() / "Desktop" / "Thesis Manager.app"
            if not desktop_path.exists():
                os.symlink(
                    "/Applications/ThesisManager.app",
                    desktop_path
                )
        elif self.system == "Linux":
            # Create .desktop file
            desktop_file = """[Desktop Entry]
Name=Thesis Manager
Exec={python_path} -m thesis_manager
Icon={icon_path}
Type=Application
Categories=Office;Education;
""".format(
                python_path=self.python_path,
                icon_path=self.project_root / "cikgubyfisa/gui/icons/thesis_icon.png"
            )
            
            # Save to applications directory
            desktop_path = Path.home() / ".local/share/applications/thesis-manager.desktop"
            desktop_path.parent.mkdir(parents=True, exist_ok=True)
            desktop_path.write_text(desktop_file)

    def _setup_autostart(self):
        """Configure application to start automatically"""
        print("\n⚙️ Setting up auto-start...")
        if self.system == "Darwin":
            # Create LaunchAgent for macOS
            plist_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.cikgubyfisa.thesismanager</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/ThesisManager.app/Contents/MacOS/ThesisManager</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>"""
            
            launch_agents_dir = Path.home() / "Library/LaunchAgents"
            launch_agents_dir.mkdir(parents=True, exist_ok=True)
            
            plist_path = launch_agents_dir / "com.cikgubyfisa.thesismanager.plist"
            plist_path.write_text(plist_content)

    def _show_instructions(self):
        """Show post-installation instructions"""
        print("\n📝 Installation Complete!")
        print("\nYou can now run Thesis Manager in several ways:")
        
        if self.system == "Darwin":
            print("1. Click the Thesis Manager icon in Applications")
            print("2. Use the desktop shortcut")
            print("3. Use Spotlight (Command + Space, type 'Thesis Manager')")
            print("4. Click the menu bar icon")
        elif self.system == "Windows":
            print("1. Use the desktop shortcut")
            print("2. Find 'Thesis Manager' in the Start menu")
            print("3. Look for the system tray icon")
        else:
            print("1. Use the application menu")
            print("2. Use the desktop shortcut")
            print("3. Look for the system tray icon")
            
        print("\nThe application will start automatically when you log in.")
        print("You can find the system tray icon in the menu bar/system tray.")

if __name__ == "__main__":
    installer = ThesisManagerInstaller()
    installer.install() 