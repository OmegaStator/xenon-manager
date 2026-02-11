### Detects if the config file exists
import os
if os.path.exists('./config.ini') == False:
    print("Configuration doesn't exist, please run xenonConfig.py before trying to use xenon-manager")
    exit()
del os     # Unloads os module, since it's not needed elsewhere

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

if config['package.managers']['native.pm'] == 'pacman':
    from package_functions import pacman as native
if config['package.managers']['aur.helper'] == 'paru':
    from package_functions import paru as aur
elif config['package.managers']['aur.helper'] == 'yay':
    from package_functions import yay as aur
else:
    aur = None
from argparse import ArgumentParser



### List of arguments
parser=ArgumentParser(
    prog="xenon-manager",
    description="xenon-manager is a CLI tool that wants to be some sort of AIO package manager, although it really just manages the already existing package managers", 
    epilog="Note : Package name must be BEFORE the options or else it won't work")
parser.add_argument("package_manager", help="package managers that you want to apply the options to. You can use the following package managers : all, native, aur")
parser.add_argument("-U", "--update", help="Refresh mirrors (see feature compatibility list in the readme) and do a full update",action="store_true")
parser.add_argument("-I", "--install", dest="install_package", metavar="package", help="Install a program, can be a program name/ local package localisation", type=str)
parser.add_argument("-D", "--db-update", help="Refresh the database",action="store_true")
parser.add_argument("-R", "--remove_package", dest="remove_package", metavar="package", help="Remove a program", type=str)
parser.add_argument("-L", "--list", help="List all installed apps for corresponding package manager", action="store_true" )


### Main argument detection mechanism
args = parser.parse_args()      # Short way to parse the arguments

# Lets you launch operation on all the package managers at the same time
if args.package_manager == "all":
    if args.update == True:
        print("Updating native packages...")
        native.full_upgrade()
        if aur == None:
            print("No AUR helper found, skipping AUR helper")
        else:
            print("Updating AUR packages")
            aur.aur_upgrade()
    elif args.db_update == True:
        print("Updating native database...")
        native.db_update()
    elif args.list == True:
        print("native packages :")
        native.list()
    else:
        print("Option not available")

# Operations on the native package manager
elif args.package_manager == "native" and config['package.managers']['native.pm'] != 'None' :
    if args.update == True:
        native.full_upgrade()
    elif args.db_update == True:
        native.db_update()
    elif args.remove_package != None:
        native.package_remove(args.remove_package)
    elif args.install_package != None:
        if  "/" in args.install_package:    # Detects if the the install command cites a path to automatically pick local install
            native.local_install(args.install_package)
        else:
            native.package_install(args.install_package)
    else:
        print("option not available")


# Operations on AUR packages, most operations are already on Pacman
elif args.package_manager == "aur" and config['package.managers']['aur.helper'] != 'None':
    if args.update == True:
        aur.upgrade()
    elif args.install_package != None:
        aur.install(args.install_package)
    elif args.remove_package != None:
        print("This feature is not implemented since pacman can already do that")
    elif args.db_update == True:
        print("Feature not implemented as it's incompatible with the package manager")
    else:
        print("Option not available")

# If no proper package manager is picked
else:
    print("The package manager", args.package_manager, "does not exist into the program or into your system, please pick a package manager that really exists")