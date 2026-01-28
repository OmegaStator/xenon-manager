import subprocess

def aur_upgrade():
    subprocess.call(['paru', '-Sua'])

def aur_install(package):
    subprocess.call(['paru', '-Sa', package])