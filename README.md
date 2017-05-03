# The NVIDIA CUDA GPU Setup utility for Kali Linux
# Purpose
This is my first attempt to automate the frustrating NVidia Driver Install for Kali Linux Versions 4.6 to 4.9, based upon this guide:
https://www.kali.org/news/cloud-cracking-with-cuda-gpu/

Since 2015, Kali has come a long way in making the NVidia Proprietary Drivers installable. The most recent event is the upgradable Kali Linux 4.9, where the installation process of blacklisting nouveau has been incorporated into the upgrade and repo packages.

Out of the box, my Laptop with a GeForce 840M from 2013, is able to run hashcat now. 
However, the GNOME Desktop Manager breaks, forcing me to resort to LightDM and XFCE as a alternative.

**Note that you should be a relatively experienced user of Linux before considering installing proprietary video drivers. Help is fairly lacking**: https://forums.geforce.com/default/topic/991448/geforce-drivers/a-working-way-to-make-gpu-optimization-on-kali-linux-2016-2-possible-really-/

Here is a relatively up-to-date guide that the recent dist-upgrade of Kali Linux has incorporated: https://wheresmykeyboard.com/2016/06/installing-nvidia-driver-kali-linux-2016-1-rolling/

And here is a excerpt from the previous post(profanity alert):

..."really, just about everything, to use the lovely benefits GPU acceleration provides go to Nvidia's website first to get instructions on how to install the drivers, or they of course just use apt-get install ; Both of which generally end with a broken GUI, confusing Xconfig errors, and many expletives being shouted.
Not to knock Nvidia, but TWICE I had set up appointments with their supposed Linux experts, and even after I asked them very specific questions on how to make my GTX960M card and my (very respectably looking customed up) Kali system make GPU optimized bahbees together, they still just shrugged their shoulders and directed me to their seriously non-consumer-friendly and very wrong instructions that made me and many others frothing at the mouth, jaw-on-the-floor LIVID angry considering that their FAQ on how to do it makes your system fundamentally unusable after only a few clicks and button presses....
WELL, here, my friends, is a link to the only tutorial out of the "...


# Initial Setup and Installation

>>1. cd /tmp

>>2. git clone https://github.com/tanc7/CUDA_Setup_Utility

>>3. cd CUDA_Setup_Utility

>>4. python setup.py

After that, you can run CUDA_setup_utility.py from the command line. **You really need to be able to use the command line comfortably, there is a phase in the installation where the display "breaks"** (it's really GNOME's issue though). At that point, you should **be able to use your TTY terminal to access the APT repos** and install XFCE as a alternative Desktop Manager. 

# How do you know that the NVidia Drivers Work?

In the second to last phase, there is a test-run of two apps, "nvidia-smi" and "hashcat -I" that will list whether or not your video card is recognized. If it IS RECOGNIZED, but your display is BROKEN, then you are 99% done with your setup. You must either, fix GNOME desktop, or use a alternative Desktop Manager like LightDM or XFCE.

In fact, even without a working desktop environment you should be able to run hashcat with GPU acceleration. As of April 30th 2017, hashcat is now merged together with cudahashcat and oclhashcat. Furthermore, you will need the hashcat-utils, by which I have included a auto-installer in this program for you.

# FAQ

>#1. After I installed the drivers, my screen crashes to a white screen with a sad computer and a logout button with the message "Oh no...."

This is where the display for GNOME Desktop Manager breaks. As covered in the python script, you have two choices...

      1. Fix GNOME Desktop Manager
      2. Replace GDM with another Desktop Manager like LightDM or XFCE

More than likely, your NVidia drivers are PROPERLY installed. More suggested fixes are covered in the DIAGNOSTICS part of the setup utility.

>#2. I use a alternative Desktop Manager, and it crashes to a black screen after I wake up my laptop from screenlock

Thats a bug. A bug that has not been resolved by the devs of light-locker for many years. My solution is...

      1. Uninstall light-locker
      2. Replace light-locker with GNOME screensaver

>#3. Hashcat tells me that my aircrack-ng .cap to HCCAP file is "outdated".

You need to use the new HCCAPX standard, available via the hashcat-utils toolkit. A auto-installer is included in the CUDA setup utility. From the main menu, press #5.
