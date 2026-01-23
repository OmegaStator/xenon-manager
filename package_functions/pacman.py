import subprocess

def db_update():
    subprocess.call(['sudo', 'pacman', '-Sy'])

def full_upgrade():
    subprocess.call(['sudo', 'pacman', '-Syu'])

def safe_upgrade():         # If you have a better name for this variable, i'm not against it
    subprocess.call(['sudo', 'pacman', '-Syyu'])

def package_remove(package):
    subprocess.call(['sudo', 'pacman', '-R', package])

def package_install(package):
    status = subprocess.run(['sudo', 'pacman', '-S', package], capture_output=True)
    if status.returncode == 1:
        print("Package was not found in local database. Searching in online database")
        status = subprocess.run(['sudo', 'pacman', '-Sy', package])
        if status.returncode == 1:
            print("The package you requested does not exit in your active repositories")