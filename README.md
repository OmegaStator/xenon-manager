# xenon-manager
Because why have 50 different package managers when you can manage all of them with one tool

# What is xenon-manager
xenon-manager is an interpreter for multiple package managers, who never dreamt of updating every package in your system with only one command

## Requirements

- python3
- At least one compatible package manager

## Package managers that are compatible as of now


## Package managers that have experimental/partial support
- pacman (archlinux)
- paru (archlinux)

## Package managers that doesn't have support but that will have in the future
- yay (archlinux)
- flatpak (generic)
- apt (Debian)
- pkg (termux)


## Features supported by xenon-manager for each package manager
|__Features__                   |pacman                              |paru|
|-------------------------------|------------------------------------|------------------------------------|
|Package install                |✅                                  |✅ (AUR only)                       |
|Package install (local package)|✅                                  |❌ (Already implemented in pacman)  |
|Package remove                 |✅                                  |❌ (Already implemented in pacman)  |
|Full update                    |✅                                  |✅ (Aur only)                       |
|Database update                |✅                                  |❌ (No database system in the AUR)  |
|List packages (by name)        |✅                                  |❌ (Already implemented in pacman)  |
|List packages (by size)        |❌ (no support from package manager)|❌ (no support from package manager)|
|List packages (by install date)|❌ (no support from package manager)|❌ (no support from package manager)|



## Issues as-of now
_wow, so empty_
