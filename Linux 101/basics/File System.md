# Filesystem Hierarchy Standard
## Standard hiearchy

### **/** is the root directory
Unlike Windows, which uses seperate drive windows.

In Linux, all drivers are organized under one directory.

**/** is the root directory

The hierachy standard is so important there is a command `man hier`.

### bin
Stores Executable programs and some commands (such as `more` and `less`)

### boot
contains the kernel and all  files to boot the system

### dev
contains all devices (the files inside aren't really files)

### etc
configuration files

### home 
personal directory of users

### lib
libraries for programs to run

### media
mount point for removable sorage devices (USB drives, DVDs)

### mount
mount point for temporary file systems

used before the media directory was instanced

### opt
software installed (not using the distribution package management system)
can be seen by all users, accesible by everyone

### proc
contains information for every running process

### root
home directory of root user

### sbin
Similar to bin, but only executed by the super user root

### tmp
Temporary files, volatile storage space, files in **tmp** can be deleted at anytime

### usr
User directory, contains important sub-directory

#### usr/bin
Important commands

#### usr/local
programs installed in system

### var
contains sub-directories

#### var/log
System log files.

#### var/log/syslog
Main system log files

---
