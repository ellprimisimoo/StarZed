import os
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
os.system("pkg upgrade && pkg update && python StarZed.pyc")
