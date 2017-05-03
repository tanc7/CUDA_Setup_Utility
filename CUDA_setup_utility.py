#!/usr/bin/env python
# coding=UTF-8
import os
import socket
import operator
import sys
from termcolor import colored
import time

# purpose to automate (for the most part ) the installation of proper NVidia drivers in a interactive menu
# Know that it requires Python termcolors module
print colored('NVidia Driver and CUDA Setup Utility\nBy Chang Tan Lister\nwww.github.com/tanc7','cyan',attrs=['bold'])

def first_reboot_cycle(): #apt-get update and dist-upgrade
    continue_question = str(raw_input("Type CONTINUE to proceed with updating Linux: "))
    if continue_question == "CONTINUE":
        print colored('[*] Updating APT Repo','yellow',attrs=['bold'])
        os.system('sudo apt-get update')
        print colored('[*] Performing Distribution Upgrade, please do not interrupt!','yellow',attrs=['bold'])
        os.system('sudo apt-get dist-upgrade -y')
        print colored('[+] Distro Update and Upgrade Completed, please reboot your machine','green',attrs=['bold'])
    elif continue_question == "0":
        main()
    else:
        print colored('[-] Type CONTINUE to proceed! Or type "0" to return to Main Menu','red',attrs=['bold'])
        first_reboot_cycle()
    return

def second_reboot_cycle(): #blacklist Nouveau Kernel Modules, update initramfs, and then reboot
    print colored('[!] Warning! After this reboot, your display will NOT WORK and you will have to rely on running this from the TTY terminals (CTRL + ALT + 1 to 6)','red',attrs=['bold'])
    continue_question = str(raw_input("Type CONTINUE to proceed with blacklisting Nouveau and modifying Kernel: "))
    if continue_question == "CONTINUE":
        print colored('[*] Searching for modules that loaded the Nouveau driver','yellow',attrs=['bold'])
        os.system('lsmod | grep -i nouveau')
        print colored('[*] Modifying Kernel, blacklisting Nouveau driver','yellow',attrs=['bold'])
        os.system('echo -e "blacklist nouveau\noptions nouveau modeset=0\nalias nouveau off" > /etc/modprobe.d/blacklist-nouveau.conf')
        print colored('[+] Rebooting System','green',attrs=['bold'])
        os.system('update-initramfs -u && reboot')
    elif continue_question == "0":
        main()
    else:
        print colored('[-] Type CONTINUE to proceed! Or type "0" to return to Main Menu','red',attrs=['bold'])
        second_reboot_cycle()
    return

def third_reboot_cycle(): # Install NVidia Drivers, OCL libraries, and CUDA Toolkits
    print colored('[*] Grepping for any modules running that says nouveau','yellow',attrs=['bold'])
    os.system('lsmod | grep -i nouveau')
    print colored('[!] Do you see anything that says Nouveau? If you do, then first kill those processes before proceeding','red',attrs=['bold'])
    continue_question = str(raw_input("Type CONTINUE to proceed with installing NVidia Drivers and required toolkits (check that no Nouveau related mods are loaded): "))
    if continue_question == "CONTINUE":
        print colored('[*] Updating APT Repo Again','yellow',attrs=['bold'])
        os.system('sudo apt-get update')
        print colored('[*] Installing NVidia Drivers, OpenCL Libraries, and NVIDIA CUDA Toolkit','yellow',attrs=['bold'])
        os.system('sudo apt-get install -y ocl-icd-libopencl1 nvidia-driver nvidia-cuda-toolkit')
        print colored('[+] Installation Complete, please reboot your machine one more time and dont freak out if the GNOME login screen crashes (access me through TTY)','green',attrs=['bold'])
    elif continue_question == "0":
        main()
    else:
        print colored('[-] Type CONTINUE to proceed! Or type "0" to return to Main Menu','red',attrs=['bold'])
        third_reboot_cycle()
    return

def fourth_reboot_cycle(): # Benchmark tests
    print colored('Before you flip out or anything thinking your system broke, lets run some tests to see if the drivers are working properly','red',attrs=['bold'])
    continue_question = str(raw_input("Type CONTINUE to proceed with benchmarking: "))
    if continue_question == "CONTINUE":
        print colored('[*] Running NVidia System-Management Interface','yellow',attrs=['bold'])
        os.system('nvidia-smi')
        print colored('[*] Running Hashcat List Interfaces','yellow',attrs=['bold'])
        os.system('hashcat -I')
        print colored('[*] Running Benchmarks, this is gonna take a while','yellow',attrs=['bold'])
        print colored('[+] Note, if the first two tests properly displayed your Video Card and Driver, then you are GOLDEN, we just need to fix your broken GNOME display','green',attrs=['bold'])
        os.system('hashcat -b')
        print colored('[+] Benchmarking complete, please go back to Main Menu and type DIAGNOSTICS to fix your screen!','green',attrs=['bold'])
        main()
    elif continue_question == "0":
        main()
    else:
        print colored('[-] Type CONTINUE to proceed! Or type "0" to return to Main Menu','red',attrs=['bold'])
        fourth_reboot_cycle()
    return

def problem_one():
    print """
    Example Photo: https://unix.stackexchange.com/questions/292308/archgnome-oh-no-something-has-gone-wrong
    I searched for a solution to this issue on my most recent attempt to install Nvidia drivers.
    https://bbs.archlinux.org/viewtopic.php?id=195880
    https://www.reddit.com/r/archlinux/comments/43v9eo/oh_no_something_has_gone_wrong/
    Basically, the default GNOME Desktop Method of video output to the screen does not support NVidia's more foreign drivers.
    It will override it's attempts to display to the screen causing errors.

    However, your NVidia Drivers, as evidenced by its recognition in both nvidia-smi and hashcat, is PERFECTLY FINE.
    You just need to fix your display...

    as long as you have access to the internet to access the APT repos from TTY

    You can either... all the fixes may or may not work.

    1. (RECOMMENDED) Fix the GNOME Desktop by reinstalling it
    2. (RECOMMENDED) Install a DIFFERENT desktop manager, like LightDM or XFCE
    3. (RECOMMENDED) Modify/Move/Delete your Display Settings /etc/X11/xorg.conf file with: "mv /etc/X11/xorg.conf /etc/X11/xorg.conf.save"
    4. (LAST RESORT) Use the APT repo to download and run nvidia-xconfig to generate a new X-Config File (Display File)
    5. (LAST RESORT) Setting autologin as root to TRUE by editing the file with: "nano /etc/gdm3/daemon.conf"

    Since the matter is so complex between each system and hardware, I decided not to make a autoinstaller
    Whatever works for me, may not work for you. It may break your own system
    """
    main()
    return

def problem_two():
    print """
    This is a well known and unfixed bug for XFCE Desktop Environments with NVidia Drivers Installed.
    https://bugs.launchpad.net/ubuntu/+source/light-locker/+bug/1320989
    The culprit is usually light-locker not giving you enough time to log back in before the screen locks.

    Since you are here in TTY, then we can do the following things.
    Force a restart of the display, and then replace lightlocker with gnome-screensaver

    1. Execute this command or Write a script that forces a reload of the display
            "service lightdm restart"
    2. Uninstall lightlocker: "sudo apt-get remove --purge light-locker"
    3. Replace with gnome-screensaver: "sudo apt-get install gnome-screensaver"
    4. Reboot your machine

    Or as a alternative you can force-no-suspend of the screen, either type this in directly or write a script:

    "sudo systemctl mask sleep.target suspend.target hibernate.target hybid-sleep.target"

    """
    main()
    return

def problem_three():
    print """
    Well at least you got past issues #1 and #2. You pretty much did everything already.

    Except one more thing. The devs behind Hashcat have altered the standards for Aircrack-ng's *.cap to hccap format.
    According to them, the folks behind Aircrack did not conform, so Hashcat guys rolled out a NEW toolkit,
    requiring you to convert to a all new format

    Here is the GitHub Link for what you need to do: https://github.com/hashcat/hashcat-utils

    1. "cd /tmp"
    2. "git clone https://github.com/hashcat/hashcat-utils"
    3. "cd /tmp/hashcat-utils/bin"
    4. "cp -r ./*.bin /usr/local/bin"

    You can now run the new Aircrack-ng to Hashcat Converter as: "cap2hccapx.bin" on terminal
    """
    main()
    return

def DIAGNOSTICS():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        "#1. GNOME Desktop: The Boot/Login Screen shows 'Oh no! Something has gone wrong' with a sad computer and a logout button",
        "#2. XFCE Desktop: Crashes to a black screen after screenlock and won't let you access anything except this TTY terminal",
        "#3. Hashcat HCCAP file format: Hashcat tells you that the Aircrack-ng to Hashcat format file is outdated"
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("What seems to be the problem?: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        problem_one()
    elif opt_Choice == "2":
        problem_two()
    elif opt_Choice == "3":
        problem_three()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        DIAGNOSTICS()
    return

tmp_dir = '/tmp'
hashcat_tmp_dir = '/tmp/hashcat-utils/bin'

def install_hashcat_utils():
    os.chdir(tmp_dir)
    print colored('[*] Git Cloning hashcat-utils repo','yellow',attrs=['bold'])
    os.system('git clone https://github.com/hashcat/hashcat-utils')
    os.chdir(hashcat_tmp_dir)
    os.system('chmod 777 ./*')
    print colored('[*] Copying ELF executables to /usr/local/bin','yellow',attrs=['bold'])
    os.system('cp -r ./*.bin /usr/local/bin')
    print colored('[+] Hashcat Utilities installation is complete, you can run them as terminal commands now under /usr/local/bin','green',attrs=['bold'])
    main()
    return

def REVERT():
    print """
    The REVERT back to open-source process is followed by these posts: https://askubuntu.com/questions/189347/how-can-i-uninstall-nvidia-proprietary-drivers

    Type CONTINUE to proceed
    """
    continue_question = str(raw_input("Type CONTINUE to proceed with REVERSING the NVIDIA driver installation: "))
    if continue_question == "CONTINUE":
        print colored('[+] Listing NVidia packages','green',attrs=['bold'])
        os.system('dpkg --get-selections | grep nvidia')
        print colored('[*] USER INTERACTION REQUIRED, need you to comment out the line that blacklisted nouveau in 5 seconds','yellow',attrs=['bold'])
        time.sleep(5)
        os.system('nano /etc/modprobe.d/blacklist-nouveau.conf')
        print colored('[*] Purging NVIDIA drivers','yellow',attrs=['bold'])
        os.system('sudo apt-get purge nvidia*')
        print colored('[*] Installing open-source nouveau drivers','yellow',attrs=['bold'])
        os.system('sudo apt-get install xserver-xorg-video-nouveau')
        print colored('[*] Moving xorg config file so a new one can be made','yellow',attrs=['bold'])
        os.system('mv /etc/X11/xorg.conf /etc/X11/xorg.conf.save')
        print colored('[+] Fully reverted. Please reboot now','green',attrs=['bold'])
    elif continue_question == "0":
        main()
    else:
        print colored('[-] Type CONTINUE to proceed! Or type "0" to return to Main Menu','red',attrs=['bold'])
        REVERT()
    return
    return
def main():
    opt_List = [
        '\n\t#0. Exit Program',
        '#1. FIRST-REBOOT CYCLE, apt-get update and dist-upgrade',
        '#2. SECOND-REBOOT CYCLE, Check for and blacklist Nouveau Kernel Modules, update initramfs, and then reboot',
        '#3. THIRD-REBOOT CYCLE, Install NVidia Drivers, OCL libraries, and CUDA Toolkits',
        '#4. FOURTH-REBOOT CYCLE, Benchmark tests. Run this in your TTY prompt if you have issues like Sad Computer on White Screen for GNOME Desktop Manager',
        '#5. FINAL PART, Install hashcat-utils automatically from github after everything is working including desktop',
        '#DIAGNOSTICS. Troubleshoot a failed installation attempt or display errors',
        '#REVERT. Revert the changes that were made and reinstall Open Source Drivers, erasing all of the effort you have done to this point'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        first_reboot_cycle()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        second_reboot_cycle()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        third_reboot_cycle()
        main()
    elif opt_Choice == "4":
        os.system('clear')
        fourth_reboot_cycle()
        main()
    elif opt_Choice == "5":
        os.system('clear')
        install_hashcat_utils()
    elif opt_Choice == "DIAGNOSTICS":
        os.system('clear')
        DIAGNOSTICS()
        main()
    elif opt_Choice == "REVERT":
        os.system('clear')
        REVERT()
        main()
    else:
        print 'You have entered a invalid option'
        main()
main()
