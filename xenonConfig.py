# Initial configuration
import configparser
import shutil
config=configparser.ConfigParser()
config['package.managers'] = {}
pm = config['package.managers']

# Main package manager detecting mechanism
if shutil.which("pacman") != None:
    pm['pacman'] = 'True'
    print("Pacman set to enabled")
else:
    pm['pacman'] = 'False'
    print("Pacman set to disabled")

# AUR package selector mechanism
if shutil.which("paru") and shutil.which("yay") != None:
    aur_helper = input("Multiple AUR Helpers found, please write the one you want to use : ")
    if aur_helper == "paru":
        pm['AUR.helper'] = 'paru'
        print("AUR_Helper enabled and set to paru")
    elif aur_helper == "yay":
        pm['AUR.helper'] = 'yay'
        print("AUR_Helper enabled and set to yay")
elif shutil.which("paru") != None:
    pm['AUR.helper'] = 'paru'
    print("AUR_Helper enabled and set to paru")
elif shutil.which("yay") != None:
    pm['AUR.helper'] = 'yay'
    print("AUR_Helper enabled and set to yay")
else:
    pm['AUR.helper'] = 'None'
    print("AUR_Helper disabled")

# Writes the configuration to a config.ini file
with open('config.ini', 'w') as configfile:
    config.write(configfile)
    print("Config file wrote sucessfully")