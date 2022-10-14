import os
import time

test = "gsettings set org.gnome.desktop.background picture-uri file:///home/duch3201/Projects/fedoraPostInstallScript/walp/PurpleLeft.svg"

os.chdir("walp")
print(test)
os.system(test)