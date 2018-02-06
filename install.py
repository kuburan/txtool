#!/data/data/com.termux/files/usr/bin/python2

import sys, os

path = os.getcwd()
sys.path.append(path)
apt_folder = "/data/data/com.termux/files/usr/etc/apt"
bin = "/data/data/com.termux/files/usr/bin"
share = "/data/data/com.termux/files/usr/share"

if not os.path.isfile("%s/sources.list" % (apt_folder)):
    print "\n sorry bos. txtool only available on termux.\n"
    sys.exit()

else:
    print "\n installing txtool...\n"
    os.system("mv -f txtool %s/txtool" % (bin))
    os.system("mkdir -p %s/txtool && mv -f core %s/txtool/core" %
             (share, share))
    os.system("mv -f module %s/txtool/module && mv -f other %s/txtool/other" %
             (share, share))
    os.system("apt-get install --assume-yes nmap php")
    print "\n Done !!! type command txtool to launch txtool\n"
