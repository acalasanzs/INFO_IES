@RD /S /Q "C:\Users\07cal\Documents\Python\acs\IES\Definitive\7-8\dist"
@RD /S /Q "C:\Users\07cal\Documents\Python\acs\IES\Definitive\7-8\build"
@RD /S /Q "C:\Users\07cal\Documents\Python\acs\IES\Definitive\7-8\__pycache__"
start /b "" "pyinstaller" "--onefile" "--icon=pp.ico" "--name=Apartats 7 i 8 by Albert CS" "7-8.py"