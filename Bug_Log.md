# CUDA setup utility successful on test rig

However, cannot determine true power because the performance is being throttled due to a underpowered PSU. The driver is throttling the performance of the rig until I can finally get my 500W Gold Standard 80+ PSU in the mail next monday. Right now its using a stock 290W power supply that came with the server. The NVIDIA-SMI probably detects inadequate power supply so its limiting its performance to prevent core damage

Average Power Consumption: 67W (out of 75W advertised "full-tilt")
Average Temperature: 65 to 80 degrees celsius
Cuda Core Utilization: 93 to 100%
Max Clock : 1700mhz range
Max Memory Clock : 3500mhz range.
Maximum Hashcat WPA2-PSK: 120+ Kilohashes/Second (120,000 passwords tried per second)
Average Hashcat WPA2-PSK: 90 Kh/s range
Size of file: Approximately 14 GB of passwords (almost 1.2 billion passwords)

# gpu   pwr  temp    sm   mem   enc   dec  mclk  pclk
# Idx     W     C     %     %     %     %   MHz   MHz
    0    59    72   100     2     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    67    76   100     2     0     0  3504  1708
    0    59    72   100     1     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    67    75   100     2     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    55    71   100     1     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    59    72   100     1     0     0  3504  1708
    0    68    75   100     1     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708
    0    65    75   100     1     0     0  3504  1708
    0    58    72   100     4     0     0  3504  1708
    0    67    75   100     4     0     0  3504  1708
    0    67    75   100     5     0     0  3504  1708
    0    67    76   100     4     0     0  3504  1708
    0    59    72   100     2     0     0  3504  1708
    0    66    74   100     1     0     0  3504  1708
    0    66    75   100     2     0     0  3504  1708
    0    66    75   100     2     0     0  3504  1708
    0    59    73   100     1     0     0  3504  1708
    0    67    74    93     5     0     0  3504  1708
    0    67    75   100     2     0     0  3504  1708
    0    66    76   100     2     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    59    72    99     3     0     0  3504  1708
    0    67    75   100     2     0     0  3504  1708
    0    67    76   100     1     0     0  3504  1708
    0    68    76   100     1     0     0  3504  1708
    0    59    72   100     2     0     0  3504  1708
    0    67    75   100     1     0     0  3504  1708


# New issues found in NVIDIA Driver 379.39 (fix on the way) -- Fixed

    As suspected, a incompatible video card has been detected. (Wrong)

    The GTX 1050 Ti, will not be able to be installed into Kali Linux Systems, even with updated headers. 

    Meanwhile the Laptop Geforce 840M is compatible with the latest drivers. 

Furthermore you do not want to manually install NVIDIA's proprietary drivers. they are not Debian ("Kali") supported, which is a .run file. It can perma-break your Kali install forcing you to reinstall all over again.

At least Kali doesnt take any more than 15 minutes to install, minus a full partition wipe and this is a brand new disk so idc.

# Proposed solution -- Implemented

For REBOOT LOOP #2 you can change the blacklist command into a bash script instead of a python script, preventing the syntax -e error from popping up.

Doesnt work. Why not just make a file to write to? All it does is write 3 lines. echo -e "blacklist nouveau\noptions nouveau modeset=0\nalias nouveau off" > /etc/modprobe.d/blacklist-nouveau.conf

LINE 1: blacklist nouveau
LINE 2: options nouveau modeset=0
LINE 3: alias nouveau off

that could easily be represented as

def write_blacklist():

  write_file = '/etc/modprobe.d/blacklist-nouveau.conf'
  
  a = open(write_file,'w')
  
  a.write('blacklist nouveau\noptions nouveau modeset=0\nalias nouveau off')
  
  a.close()
  
  return 

# Second Installation Attempt Succeeded
You must make sure that your linux headers are properly updated. For my test machine running Kali 2016.2 Linux 4.6.0, it must be dist-upgraded TWICE into Linux kali 4.9.0-kali4-amd64 #1 SMP Debian 4.9.25-1kali1 (2017-05-04) x86_64 GNU/Linux

Did not get to have a chance to fix the "bad character problem" for echo -e. But All it does really is... -- implemented the pythonic way of doing it (see above, function write_blacklist())

    1. Open a empty file called: /etc/modprobe.d/blacklist-nouveau.conf
    2. Write 3 lines
    3. Updates initramfs
    4. Reboots machine to prepare for the NVIDIA driver installation. 

Furthermore, for the GTX 1050 Ti, there is NO need to replace GNOME Desktop, unlike my Geforce 840M Laptop. It could be that since patch 379.39, because the 10-Series are flagship models they naturally have better driver support. 
