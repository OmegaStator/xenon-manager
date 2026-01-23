from package_functions import pacman
from argparse import ArgumentParser

parser=ArgumentParser(
    prog="xenon-manager",
    description="xenon-manager is a CLI tool that wants to be some sort of AIO package manager, although it really just manages the already existing package managers")
parser.add_argument("package_manager", help="package managers that you want to apply the options to. You can take the following package managers : all, pacman")
parser.add_argument("-U", "--update", help="Refresh mirrors and do a full update", nargs=0 )
parser.add_argument("-I", "--install", dest="argument", metavar="package", help="Install a program")

args = parser.parse_args()
print(args.update)