import subprocess

def db_update():
    subprocess.call(['sudo', 'pacman', '-Sy'])

def full_upgrade():
    subprocess.call(['sudo', 'pacman', '-Syu'])

def package_remove(package):
    subprocess.call(['sudo', 'pacman', '-R', package])

def package_install(package):
    subprocess.call(['sudo', 'pacman', '-Sy', package])