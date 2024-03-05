## Linux Package Management
Like an "app store"!
Dependecy manager.

DEB debian distro, RPM redhat distro

## Debian System
### DEB `dpkg` | `apt`
**dpkg** can **not** automatically download packages from repository.

`apt update` Checks for avaialble package updates.

`apt list --upgradeable` See list of upgradable packages.

`apt upgrade` Upgrades the availble packages.

Ugrades to operating system and programs are done this way.

### Using `apt` to find, check, install, delete and purge packages
`which` checks if this package is available for download
`which pdftk` pdftk is a program that does not come distributed.

`apt which pdftk` This will show available packages to download.

`apt show pdftk` gives a description about the program. Very usefull.

`apt install pdftk` to install program from the repositiory. Requires root priviledge.

`which pdftk` to check for program successfull installation.

`apt remove pdftk` to remove software. Requires root priviledge.

`apt purge pdftk`
Some packages use config files that are not cleaned after uninstall. 
`apt autoremove`

## RedHat Systems
### RedHat `rpm` `yum` 
`yum` is simmillar to `apt` in Debian.

`sudo yum check-update` Checks for avaialble package updates.

This is not completely necessary as the software auto updates.

`yum` is like update and upgrade in `apt`

### Using `yum` to find, check, install and delete packages
`yum search qpdf` qpdf is a program that does not come distributed.

`yum info qpdf`  This will show available packages to download.

`sudo yum install qpdf` To install.

`which qpdf` to check for succesfull installation.

`sudo yum remove qpdf` to remove the program. Unlike `apt` there is no command to purge.

## Manually Installing Software | Example downloading git
Download the source code for a program and self compile

### **1.** Install packages needed to build the software. 

example:

`apt install build-essential checkinstall libz-dev libssl-dev libcurl4-gnutls-dev libexpatl-dev gettext cmake gcc curl`

### **2.** Use wget to download git

`which git` Check if git is available.

`cd Downloads` change directory to Downloads

`wget https://link/to/package.tar.gz` Use wget to get the git archive (.tar.gz  a.k.a  tar ball) 

`tar xfz package.tar.gz` Unzip and decompress the tar ball

`cd package` enter the directory

Configure build environment and determine where files will be stored.

`./configure` This creates a `Makefile`

`make` To compile the code.

### **3.** Install the compiled software

`sudo make install` Install the software 

`git --version`

___
