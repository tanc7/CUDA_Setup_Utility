# New issues found in NVIDIA Driver 379.39.

As suspected, a incompatible video card has been detected.

The GTX 1050 Ti, will not be able to be installed into Kali Linux Systems, even with updated headers. 

Meanwhile the Laptop Geforce 840M is compatible with the latest drivers. 

Furthermore you do not want to manually install NVIDIA's proprietary drivers. they are not Debian ("Kali") supported, which is a .run file. It can perma-break your Kali install forcing you to reinstall all over again.

# Proposed solution

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

