# CIKGUBYFISA - Malaysian University Thesis Manager

A comprehensive thesis template and management system for Malaysian universities, supporting both public and private institutions.

## Features

- 🎓 Supports multiple Malaysian universities:
  - Public Universities:
    - Universiti Malaya (UM)
    - Universiti Sains Malaysia (USM)
    - Universiti Kebangsaan Malaysia (UKM)
    - Universiti Putra Malaysia (UPM)
    - Universiti Teknologi Malaysia (UTM)
  - Private Universities:
    - Taylor's University
    - Sunway University
    - MMU
    - UTP
    - IIUM

- 📝 Thesis Management:
  - Automatic formatting according to university guidelines
  - Bibliography management with multiple citation styles
  - Chapter organization and structuring
  - Reference management

- 🎨 Features:
  - User-friendly GUI interface
  - System tray integration
  - Automatic updates
  - Cross-platform support (macOS, Windows, Linux)

## Installation

### macOS

```bash
# Clone the repository
git clone https://github.com/yourusername/cikgubyfisa.git
cd cikgubyfisa

# Run the installer
python3 install.py
```

The installer will:
1. Check and install required dependencies
2. Create application bundle
3. Add desktop shortcut
4. Configure auto-start

### Windows

```batch
# Clone the repository
git clone https://github.com/yourusername/cikgubyfisa.git
cd cikgubyfisa

# Run the installer
python install.py
```

### Linux

```bash
# Clone the repository
git clone https://github.com/yourusername/cikgubyfisa.git
cd cikgubyfisa

# Run the installer
python3 install.py
```

## Usage

1. Launch the application:
   - macOS: Use Spotlight (Cmd + Space) and type "Thesis Manager"
   - Windows: Use desktop shortcut or Start menu
   - Linux: Use application menu or desktop shortcut

2. Select your university and faculty

3. Enter thesis information:
   - Title
   - Author details
   - Supervisor information
   - Abstract

4. Add content:
   - Write or import chapters
   - Add references
   - Insert figures and tables

5. Generate thesis:
   - Choose output format (PDF/LaTeX)
   - Select citation style
   - Generate final document

## Requirements

- Python 3.8 or higher
- LaTeX distribution (e.g., MacTeX, MiKTeX)
- Required Python packages (automatically installed):
  - pylatex>=1.4.1
  - bibtexparser>=1.4.0
  - PyPDF2>=2.0.0
  - PyQt6>=6.4.0
  - pystray>=0.19.4
  - pillow>=9.0.0

## Development

### Setup Development Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Unix
.\venv\Scripts\activate   # Windows

# Install development dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
pytest tests/
```

### Building Documentation

```bash
cd docs
make html
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

Copyright (c) 2024 FISA Trading

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

See the [LICENSE](LICENSE) file for the full license text.

## Acknowledgments

- Thanks to all Malaysian universities for their thesis guidelines
- PyLaTeX team for the excellent LaTeX library
- Qt team for the GUI framework
- FISA Trading team for project maintenance and support

## Support

For support, please:
1. Check the [documentation](docs/)
2. Open an issue on GitHub
3. Contact FISA Trading:
   - GitHub: [@fisapool](https://github.com/fisapool)
   - Shopee: [FISA Trading](https://shopee.com.my/fisatrading)

## Roadmap

- [ ] Add more university templates
- [ ] Implement real-time preview
- [ ] Add collaboration features
- [ ] Create web version
- [ ] Add AI-powered writing assistance

## Authors

- FISA Trading - Initial work - [fisapool](https://github.com/fisapool)
  - Shopee: [FISA Trading](https://shopee.com.my/fisatrading)
  - Contact: [Insert preferred contact method]

## Project Status

Active development - Contributions welcome!
