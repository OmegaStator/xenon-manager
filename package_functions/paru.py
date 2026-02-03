import subprocess

def upgrade():
    subprocess.call(['paru', '-Sua'])

def install(package):
    subprocess.call(['paru', '-Sa', package])