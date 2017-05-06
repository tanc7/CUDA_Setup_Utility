# New issues found in NVIDIA Driver 379.39.

As suspected, a incompatible video card has been detected.

The GTX 1050 Ti, will not be able to be installed into Kali Linux Systems, even with updated headers. 

Meanwhile the Laptop Geforce 840M is compatible with the latest drivers. 

Furthermore you do not want to manually install NVIDIA's proprietary drivers. they are not Debian ("Kali") supported, which is a .run file. It can perma-break your Kali install forcing you to reinstall all over again.

# Proposed solution

For REBOOT LOOP #2 you can change the blacklist command into a bash script instead of a python script, preventing the syntax -e error from popping up.
