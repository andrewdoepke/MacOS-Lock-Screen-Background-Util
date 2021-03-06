"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['app.py', 'restrt.sh', 'lockscreengb.sh']
OPTIONS = {'argv_emulation': False, 'includes':['PyQt5', 'os', 'sys'], 'packages':['PyQt5'], 'iconfile':'images/icon.icns'}

setup(
    app=APP,
    name="Desktop Background Util",
    version="1.1",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
