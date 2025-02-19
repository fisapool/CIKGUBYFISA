from setuptools import setup, find_packages

setup(
    name="cikgubyfisa",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pylatex>=1.4.1",
        "bibtexparser>=1.4.0",
        "PyPDF2>=2.0.0",
        "PyQt6>=6.4.0",
        "pystray>=0.19.4",
        "pillow>=9.0.0",
    ],
    entry_points={
        "console_scripts": [
            "thesis-manager=thesis_manager:main",
        ],
    },
    package_data={
        "cikgubyfisa": ["gui/icons/*.png"],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A thesis management system for Malaysian universities",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cikgubyfisa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LaTeX Project Public License",
        "Operating System :: OS Independent",
    ],
) 