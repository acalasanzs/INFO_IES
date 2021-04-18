import PyInstaller.__main__

PyInstaller.__main__.run([
    'Definitive/7-8/7-8.py',
    '--onefile',
    '--icon=C:/Users/07cal/Downloads/pp.ico 7-8.py',
    '--manifest=Definitive/7-8/manifest.xml',
    '--hidden-import=Module'
    ])