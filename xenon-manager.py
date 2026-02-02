from package_functions import pacman
from package_functions import paru
from argparse import ArgumentParser

### List of arguments
parser=ArgumentParser(
    prog="xenon-manager",
    description="xenon-manager is a CLI tool that wants to be some sort of AIO package manager, although it really just manages the already existing package managers", 
    epilog="Note : Package name must be BEFORE the options or else it won't work")
parser.add_argument("package_manager", help="package managers that you want to apply the options to. You can take the following package managers : all, pacman, paru")
parser.add_argument("-U", "--update", help="Refresh mirrors (see feature compatibility list in the readme) and do a full update",action="store_true")
parser.add_argument("-I", "--install", dest="install_package", metavar="package", help="Install a program, can be a program name/ local package localisation", type=str)
parser.add_argument("-D", "--db-update", help="Refresh the database",action="store_true")
parser.add_argument("-R", "--remove_package", dest="remove_package", metavar="package", help="Remove a program", type=str)
parser.add_argument("-L", "--list", help="List all installed apps for corresponding package manager", action="store_true" )


### Main argument detection mechanism
args = parser.parse_args()                  # Short way to parse the arguments


if args.package_manager == "all":           # Lets you launch operation on all the package managers at the same time
    if args.update == True:
        print("Updating pacman packages...")
        pacman.full_upgrade()
        print("Updating AUR packages")
        paru.aur_upgrade()
    elif args.db_update == True:
        print("Updating pacman database...")
        pacman.db_update()
    elif args.list == True:
        print("Pacman packages :")
        pacman.list()
    else:
        print("Option not available")

elif args.package_manager == "pacman":      # Operations on Pacman
    if args.update == True:
        pacman.full_upgrade()
    elif args.db_update == True:
        pacman.db_update()
    elif args.remove_package != None:
        pacman.package_remove(args.remove_package)
    elif args.install_package != None:
        if  "/" in args.install_package:    # Detects if the the install command cites a path to automatically pick local install
            pacman.local_install(args.install_package)
        else:
            pacman.package_install(args.install_package)
    else:
        print("option not available")

elif args.package_manager == "paru":        # Operations on Paru, most operations are already on Pacman
    if args.update == True:
        paru.aur_upgrade()
    elif args.install_package != None:
        paru.aur_install(args.install_package)
    elif args.remove_package != None:
        print("This feature is not implemented since pacman can already do that")
    elif args.db_update == True:
        print("Feature not implemented as it's incompatible with the package manager")
    else:
        print("Option not available")

else:                                       # If no proper package manager is picked
    print("The package manager", args.package_manager, "does not exist into the program, please pick a package manager that really exists")