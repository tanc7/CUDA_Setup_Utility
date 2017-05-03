# CUDA_Setup_Utility
# Purpose
This is my first attempt to automate the frustrating NVidia Driver Install for Kali Linux Versions 4.6 to 4.9, based upon this guide:
https://www.kali.org/news/cloud-cracking-with-cuda-gpu/

Since 2015, Kali has come a long way in making the NVidia Proprietary Drivers installable. 

Out of the box, my Laptop with a GeForce 840M from 2013, is able to run hashcat now. However, the GNOME Desktop Manager breaks, forcing me to resort to LightDM and XFCE as a alternative.


# Initial Setup and Installation

>>1. cd /tmp

>>2. git clone https://github.com/tanc7/CUDA_Setup_Utility

>>3. cd CUDA_Setup_Utility

>>4. python setup.py

After that, you can run CUDA_setup_utility.py from the command line. You really need to be able to run from the command line, there is a phase in the installation where the display "breaks" (it's really GNOME's issue though). At that point, you should be able to use your TTY terminal to access the APT repos and install XFCE as a alternative Desktop Manager. 

# How do you know that the NVidia Drivers Work?

In the second to last phase, there is a test-run of two apps, "nvidia-smi" and "hashcat -I" that will list whether or not your video card is recognized. If it IS RECOGNIZED, but your display is BROKEN, then you are 99% done with your setup. You must either, fix GNOME desktop, or use a alternative Desktop Manager like LightDM or XFCE.

In fact, even without a working desktop environment you should be able to run hashcat with GPU acceleration. As of April 30th 2017, hashcat is now merged together with cudahashcat and oclhashcat. Furthermore, you will need the hashcat-utils, by which I have included a auto-installer in this program for you.
