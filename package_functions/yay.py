import subprocess

def upgrade():
    subprocess.call(['yay', '-Sua'])

def install(package):
    subprocess.call(['yay', '-Sa', package])