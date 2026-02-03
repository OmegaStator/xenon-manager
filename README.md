# xenon-manager
Because why have 50 different package managers when you can manage all of them with one tool

# What is xenon-manager
xenon-manager is an interpreter for multiple package managers, who never dreamt of updating every package in your system with only one command

## Requirements

- python3
- sudo
- At least one compatible package manager

## How to use
You will need to run `xenonConfig` at least one time before being able to use `xenon-manager`, it will generate a config.ini file.

```
positional arguments:
  package_manager       package managers that you want to apply the options
                        to. You can use the following package managers :
                        all, pacman, aur

options:
  -U, --update          Refresh mirrors (see feature compatibility list in
                        the readme) and do a full update

  -I, --install <<package>>
                        Install a program, can be a program name/ local
                        package localisation

  -D, --db-update       Refresh the database

  -R, --remove_package <<package>>
                        Remove a program

  -L, --list            List all installed apps for corresponding package
                        manager
```

## Package managers that are compatible as of now
- pacman (archlinux)
- paru (archlinux)
- yay (archlinux)

## Package managers that have experimental/partial support

## Package managers that doesn't have support but that will have in the future
- flatpak (generic)
- apt (Debian)
- pkg (termux)


## Features supported by xenon-manager for each package manager
|__Features__                   |pacman                              |paru                                |yay                                 |
|-------------------------------|------------------------------------|------------------------------------|------------------------------------|
|Package install                |✅                                  |✅ (AUR only)                       |✅ (AUR only)                       |
|Package install (local package)|✅                                  |❌ (Already implemented in pacman)  |❌ (Already implemented in pacman)  |
|Package remove                 |✅                                  |❌ (Already implemented in pacman)  |❌ (Already implemented in pacman)  |
|Full update                    |✅                                  |✅ (Aur only)                       |✅ (Aur only)                       |
|Database update                |✅                                  |❌ (No database system in the AUR)  |❌ (No database system in the AUR)  |
|List packages (by name)        |✅                                  |❌ (Already implemented in pacman)  |❌ (Already implemented in pacman)  |
|List packages (by size)        |❌ (no support from package manager)|❌ (no support from package manager)|❌ (no support from package manager)|
|List packages (by install date)|❌ (no support from package manager)|❌ (no support from package manager)|❌ (no support from package manager)|



## Issues as-of now
_wow, so empty_
