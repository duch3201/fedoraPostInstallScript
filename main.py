import os
import time

def number_of_keys(dict):
 
    count = 0
 
    for key,value in dict.items():
 
        count += 1
 
    return count

test = "gsettings set org.gnome.desktop.background picture-uri file:///home/duch3201/Projects/fedoraPostInstallScript/walp/PurpleLeft.svg"
fdf = "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'"

flatpaks = {
    "0":"com.bitwarden.desktop",
    "1":"com.discordapp.Discord",
    "2":"com.spotify.Client",
    "3":"com.visualstudio.code",
    "4":"org.videolan.VLC",
    "5":"com.makemkv.MakeMKV",
    "6":"com.raggesilver.BlackBox",
    "7":"org.gnome.Extensions"

}

flatpakinst = "flatpak install "

print("setting wallpaper")
os.chdir("walp")
os.system(test)

print("installing flatpaks")
print(flatpaks["0"])
print(flatpaks["1"])
print(flatpaks["2"])
print(flatpaks["3"])
print(flatpaks["4"])
print(flatpaks["5"])
print(flatpaks["6"])
print(flatpaks["7"])

keynum = number_of_keys(flatpaks)
i = 0

print(keynum)
input("")
while i < keynum:
    print("fdf")
    #os.system(flatpakinst+flatpaks[i])
    i += 1

os.system(fdf)

print("done!")